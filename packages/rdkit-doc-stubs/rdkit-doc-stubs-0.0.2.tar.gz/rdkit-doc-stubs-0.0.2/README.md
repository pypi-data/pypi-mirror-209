# rdkit-doc-stubs
This repository needs to build the stubs for the RDKit package on the first start to avoid license issues.

Sources are the RDKit documentation and mypy's stubgen.
On run of the install script, the documentation is downloaded and parsed.
While stubgen is run on the RDKit package. The stubs are then merged and
installed into the site-packages directory.

## Usage
```
pip install rdkit-doc-stubs
python -m rdkit-stubs.install
```