# Simple Crypto
A Python mini-utility for symmetric "shift" file encryption.
It works on the principle of Caesar's byte cipher: each byte is shifted by `key` (0-255) in a round-robin fashion.
---
## Features
* **Any file type**  – text, image, archive…

* **CLI one-liner**  – all configuration via command line arguments.

* **Zero-deps**  – only standard Python library ≥3.8.

* **Cross-platfor**  – Windows / macOS / Linux.

> **Important** 
> This is my educational example: the algorithm does not protect against serious cryptanalysis. Use > > only for practice or masking data without high value.

---
## Installation (developer option)

```bash
# 1. Clone the project
git clone https://github.com/Filitin/my-first-projects.git
cd my-first-projects

# 2. (Optional) create a virtual environment
python -m venv .venv
# Linux/macOS
source .venv/bin/activate
# Windows (PowerShell)
.venv\Scripts\activate

# 3. Install the package in editable mode
pip install -e .
```
---
# Quick start
## Encrypt any file
    python -m simple_crypto.cli encrypt secret.txt 42 -o secret.enc
## Deciphering
    python -m simple_crypto.cli decrypt secret.enc 42 -o secret.txt
