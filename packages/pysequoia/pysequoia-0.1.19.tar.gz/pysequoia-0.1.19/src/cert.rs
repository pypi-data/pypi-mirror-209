use std::sync::{Arc, Mutex, MutexGuard};

use once_cell::sync::Lazy;
use openpgp::cert::prelude::*;
use openpgp::packet::signature::subpacket::NotationDataFlags;
use openpgp::packet::signature::SignatureBuilder;
use openpgp::packet::{signature, UserID};
use openpgp::policy::{Policy, StandardPolicy};
use openpgp::serialize::SerializeInto;
use openpgp::types::SignatureType;
use openpgp::Packet;
use pyo3::prelude::*;
use sequoia_openpgp as openpgp;

use crate::decrypt;
use crate::notation::Notation;
use crate::signer::PySigner;
use crate::user_id::UserId;

static DEFAULT_POLICY: Lazy<Arc<Mutex<Box<dyn Policy>>>> =
    Lazy::new(|| Arc::new(Mutex::new(Box::new(StandardPolicy::new()))));

#[derive(Clone)]
#[pyclass]
pub struct Cert {
    cert: openpgp::cert::Cert,
    policy: Arc<Mutex<Box<dyn Policy>>>,
}

impl From<openpgp::cert::Cert> for Cert {
    fn from(cert: openpgp::cert::Cert) -> Self {
        Self {
            cert,
            policy: Arc::clone(&DEFAULT_POLICY),
        }
    }
}

impl Cert {
    pub fn cert(&self) -> &openpgp::cert::Cert {
        &self.cert
    }

    pub fn policy(&self) -> MutexGuard<Box<dyn Policy>> {
        self.policy.lock().unwrap()
    }
}

#[pymethods]
impl Cert {
    #[staticmethod]
    pub fn from_file(path: String) -> PyResult<Self> {
        use openpgp::parse::Parse;
        Ok(openpgp::cert::Cert::from_file(path)?.into())
    }

    #[staticmethod]
    pub fn from_bytes(bytes: &[u8]) -> PyResult<Self> {
        use openpgp::parse::Parse;
        Ok(openpgp::cert::Cert::from_bytes(bytes)?.into())
    }

    #[staticmethod]
    pub fn generate(user_id: &str) -> PyResult<Self> {
        Ok(
            openpgp::cert::CertBuilder::general_purpose(None, Some(user_id))
                .generate()?
                .0
                .into(),
        )
    }

    pub fn merge(&self, new_cert: &Cert) -> PyResult<Cert> {
        let merged_cert = self.cert().clone().merge_public(new_cert.cert().clone())?;
        Ok(merged_cert.into())
    }

    pub fn add_user_id(&mut self, value: String, mut certifier: PySigner) -> PyResult<Cert> {
        let cert = self.cert.clone();
        let userid = UserID::from(value);
        let builder = signature::SignatureBuilder::new(SignatureType::PositiveCertification);
        let binding = userid.bind(&mut certifier, &cert, builder)?;

        let cert = cert.insert_packets(vec![Packet::from(userid), binding.into()])?;
        Ok(Cert {
            cert,
            policy: Arc::clone(&self.policy),
        })
    }

    pub fn revoke_user_id(&mut self, user_id: &UserId, mut certifier: PySigner) -> PyResult<Cert> {
        let cert = self.cert.clone();
        let userid = UserID::from(user_id.__str__());
        let builder = signature::SignatureBuilder::new(SignatureType::CertificationRevocation);
        let binding = userid.bind(&mut certifier, &cert, builder)?;

        let cert = cert.insert_packets(vec![Packet::from(binding)])?;
        Ok(Cert {
            cert,
            policy: Arc::clone(&self.policy),
        })
    }

    pub fn set_expiration(
        &mut self,
        expiration: chrono::DateTime<chrono::Utc>,
        mut certifier: PySigner,
    ) -> PyResult<Cert> {
        let cert = self.cert.clone();
        let signature = cert.set_expiration_time(
            &**self.policy(),
            None,
            &mut certifier,
            Some(expiration.into()),
        )?;

        let cert = cert.insert_packets(signature)?;
        Ok(Cert {
            cert,
            policy: Arc::clone(&self.policy),
        })
    }

    #[getter]
    pub fn expiration(&self) -> PyResult<Option<chrono::DateTime<chrono::Utc>>> {
        Ok(self
            .cert
            .primary_key()
            .with_policy(&**self.policy(), None)?
            .key_expiration_time()
            .map(|exp| exp.into()))
    }

    pub fn __str__(&self) -> PyResult<String> {
        let armored = self.cert.armored();
        Ok(String::from_utf8(armored.to_vec()?)?)
    }

    pub fn __repr__(&self) -> String {
        format!("<Cert fingerprint={}>", self.cert.fingerprint())
    }

    #[getter]
    pub fn fingerprint(&self) -> PyResult<String> {
        Ok(format!("{:x}", self.cert.fingerprint()))
    }

    #[getter]
    pub fn user_ids(&self) -> PyResult<Vec<UserId>> {
        let policy = &**self.policy();
        let cert = self.cert.with_policy(policy, None)?;
        cert.userids()
            .revoked(false)
            .map(|ui| UserId::new(ui, policy))
            .collect()
    }

    pub fn set_notations(
        &self,
        mut certifier: PySigner,
        notations: Vec<Notation>,
    ) -> PyResult<Self> {
        let policy = self.policy();
        let cert = self.cert.with_policy(&**policy, None)?;

        let ua = cert.userids().next().unwrap();
        let mut builder = SignatureBuilder::from(ua.binding_signature().clone());

        let cert = if !notations.is_empty() {
            builder = builder.set_notation(
                notations[0].key(),
                notations[0].value(),
                NotationDataFlags::empty().set_human_readable(),
                false,
            )?;

            for notation in &notations[1..] {
                builder = builder.add_notation(
                    notation.key(),
                    notation.value(),
                    NotationDataFlags::empty().set_human_readable(),
                    false,
                )?;
            }

            let new_sig = builder.sign_userid_binding(&mut certifier, None, ua.userid())?;

            self.cert.clone().insert_packets(vec![new_sig])?
        } else {
            self.cert.clone()
        };

        Ok(cert.into())
    }

    pub fn signer(&self, password: Option<String>) -> PyResult<PySigner> {
        if let Some(key) = self
            .cert
            .keys()
            .secret()
            .with_policy(&**self.policy(), None)
            .alive()
            .revoked(false)
            .for_signing()
            .next()
        {
            let mut key = key.key().clone();
            if let Some(password) = password {
                key = key.decrypt_secret(&(password[..]).into())?;
            }
            let keypair = key.into_keypair()?;
            Ok(PySigner::new(Box::new(keypair)))
        } else {
            Err(anyhow::anyhow!("No suitable signing subkey for {}", self.cert).into())
        }
    }

    pub fn certifier(&self, password: Option<String>) -> PyResult<PySigner> {
        if let Some(key) = self
            .cert
            .keys()
            .secret()
            .with_policy(&**self.policy(), None)
            .alive()
            .revoked(false)
            .for_certification()
            .next()
        {
            let mut key = key.key().clone();
            if let Some(password) = password {
                key = key.decrypt_secret(&(password[..]).into())?;
            }
            let keypair = key.into_keypair()?;
            Ok(PySigner::new(Box::new(keypair)))
        } else {
            Err(anyhow::anyhow!("No suitable certifying key for {}", self.cert).into())
        }
    }

    pub fn decryptor(&self, password: Option<String>) -> PyResult<decrypt::PyDecryptor> {
        if let Some(key) = self
            .cert
            .keys()
            .secret()
            .with_policy(&**self.policy(), None)
            .alive()
            .revoked(false)
            .for_transport_encryption()
            .for_storage_encryption()
            .next()
        {
            let mut key = key.key().clone();
            if let Some(password) = password {
                key = key.decrypt_secret(&(password[..]).into())?;
            }
            let keypair = key.into_keypair()?;
            Ok(decrypt::PyDecryptor::new(Box::new(keypair)))
        } else {
            Err(anyhow::anyhow!("No suitable decryption subkey for {}", self.cert).into())
        }
    }
}
