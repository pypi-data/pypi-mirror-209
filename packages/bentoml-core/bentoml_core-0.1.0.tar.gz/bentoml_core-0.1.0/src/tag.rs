
use std::{hash::{Hash, Hasher}, collections::hash_map::DefaultHasher};

use pyo3::{prelude::*, exceptions::PyValueError, types::PyType};
use regex::Regex;
use lazy_static::lazy_static;

#[pyclass]
#[derive(Clone, Debug)]
pub struct Tag {
    #[pyo3(get)]
    name: String,
    #[pyo3(get)]
    version: Option<String>,
}

lazy_static! {
    static ref TAG_REGEX: Regex = Regex::new(r"^[a-z0-9]([-._a-z0-9]*[a-z0-9])?$").unwrap();
}
const TAG_MAX_LENGTH: usize = 63;

fn validate_tag_str(value: &str) -> PyResult<()> {
    if value.len() > TAG_MAX_LENGTH {
        return Err(PyValueError::new_err(format!("Tag length must be less than or equal to {} characters", TAG_MAX_LENGTH)));
    }
    if !TAG_REGEX.is_match(value) {
        return Err(PyValueError::new_err("A tag's name or version must consist of alphanumeric characters, '_', '-', or '.', and must start and end with an alphanumeric character".to_string()));
    }
    Ok(())
}

impl Hash for Tag {
    fn hash<H: Hasher>(&self, state: &mut H) {
        self.name.hash(state);
        self.version.hash(state);
    }
}

#[pymethods]
impl Tag {
    #[new]
    pub fn new(name: String, version: Option<String>) -> PyResult<Self> {
        let lname = name.to_lowercase();
        validate_tag_str(&lname)?;
        let lversion = match version {
            Some(v) => {
                let lv = v.to_lowercase();
                validate_tag_str(&lv)?;
                Some(lv)
            },
            None => None,
        };
        Ok(Self { name: lname, version: lversion })
    }

    pub fn __str__(&self) -> PyResult<String> {
        match &self.version {
            Some(v) => Ok(format!("{}:{}", self.name, v)),
            None => Ok(self.name.clone()),
        }
    }

    pub fn __repr__(&self) -> PyResult<String> {
        match &self.version {
            Some(v) => Ok(format!("Tag(name={}, version={})", self.name, v)),
            None => Ok(format!("Tag(name={})", self.name)),
        }
    }

    pub fn __eq__(&self, other: &PyAny) -> PyResult<bool> {
        let other_tag = other.extract::<Tag>()?;
        Ok(self.name == other_tag.name && self.version == other_tag.version)
    }

    pub fn __lt__(&self, other: &PyAny) -> PyResult<bool> {
        let other_tag = other.extract::<Tag>()?;
        if self.name == other_tag.name {
            match (&self.version, &other_tag.version) {
                (Some(sv), Some(ov)) => return Ok(sv < ov),
                (_, None) => return Ok(false),
                (None, Some(_)) => return Ok(true),
            }
        }
        return Ok(self.name < other_tag.name);
    }

    pub fn __hash__(&self) -> u64 {
        let mut s = DefaultHasher::new();
        self.hash(&mut s);
        s.finish()
    }

    #[classmethod]
    pub fn from_taglike(_cls: &PyType, taglike: &PyAny) -> PyResult<Self> {
        if let Ok(tag) = taglike.extract::<Tag>() {
            return Ok(tag);
        }
        if let Ok(s) = taglike.extract::<&str>() {
            let mut parts = s.split(':');
            let name = parts.next().unwrap();
            let version = parts.next();
            let tag = Tag::new(name.to_string(), version.map(|v| v.to_string()))?;
            return Ok(tag);
        }
        return Err(PyValueError::new_err("Tag must be a string or a Tag".to_string()))
    }
}