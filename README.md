# DES Key Recovery — Controlled Demo

> **Educational & ethical use only.** This repository demonstrates, in a **controlled and authorized** setting, how to validate candidate keys against a DES-encrypted ciphertext. It is a didactic artifact for a computer security course / portfolio.

## ⚖️ Legal Disclaimer

This repository and its code are intended **solely for educational and demonstration purposes**. Use them **only**:
- on data/systems you fully own, or
- on systems where you have **explicit, written authorization**.

Any other use (including attempts to access, test, or compromise third-party systems or data) may violate criminal/civil law. The author and contributors accept **no liability** for misuse. This is **not** legal advice; consult a qualified lawyer for your jurisdiction.

---

## 🧭 What this project shows

- A **safe demo** of candidate-based key checking for DES (single DES, 8-byte key).
- Reproducible, minimal Python code to:
  - decode a Base64 ciphertext,
  - try a **small, pre-defined** set of candidate keys (no blind brute-force),
  - verify a plausible plaintext under strict, ethical constraints.

**Key facts (demo context)**  
- Cipher algorithm: **DES** (8-byte key).  
- Ciphertext (Base64): `dpi4c+NIZxM=`  
- Plaintext: an 8-character Italian word (didactic assumption).  
- Scope: **candidate-list validation** only, not exhaustive search.

> The intent is to show *methodology* (reasoning about keyspace, linguistic/structural hints, safe verification), not to provide offensive tooling.

---

## 📂 Repository structure

.
├─ demo_safe_decrypt.py # safe demo script (single-file, minimal deps)
└─ old_attempts/ # older/experimental attempts (historical context)

## ▶️ Quickstart (local run)

**Prerequisites:** Python 3.10+.

```bash
# 1) Clone
git clone https://github.com/patan3saro/des-key-recovery-demo.git
cd des-key-recovery-demo

# 2) (Optional but recommended) create a virtual environment
python3 -m venv .venv && source .venv/bin/activate   # (Windows: .venv\Scripts\activate)

# 3) Install minimal dependency
python -m pip install --upgrade pip
python -m pip install pyDes

# 4) Run the demo
python demo_safe_decrypt.py


** 🧪 Reproducibility & safety notes**

No mass brute forcing. The script is intentionally constrained to a limited candidate set for classroom use.

Deterministic behavior. Same inputs ⇒ same output.

Clear boundaries. The code refuses to run in “unbounded” modes; edits are on you and at your responsibility.



**🧱 Limitations (by design)**

Not an all-purpose cracking tool; no exhaustive search.

No GPU/parallel rigs; concurrency, if any, is limited and kept didactic.

Assumes a short, curated candidate list derived from authorized hints.
