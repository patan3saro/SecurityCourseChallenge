# Security Challenge

A challenge from a computer security course: several controlled attempts to decipher a ciphertext using DES and candidate-key strategies (dictionary, heuristics, etc.). This repository is an **educational demo** intended for portfolio / interview purposes and for authorized lab exercises only. It demonstrates methodology, reproducibility and safe experimentation — **not** tools for unauthorized access.

---

## Key facts 
- **Cipher algorithm:** DES (single DES, 8-byte key).  
- **Ciphertext (Base64):** `dpi4c+NIZxM=`  
- **Plaintext:** a single Italian word of **length 8** (for the demo: `patatine`).  
- **Key:** exactly **8 characters** (for the demo: `mmalgeri`).  
- The demo shows how a candidate list and linguistic heuristics reduce the effective search space (controlled experiment).

> ⚠️ IMPORTANT: Use this repository only on local test data or on targets for which you have explicit written authorization.

---

## Overview
This repository contains:
- a safe demonstration script that tests **only** keys provided in a candidate list (`candidates.txt`),
- instructions for a one-click run (`run_demo.sh`),
- minimal Docker support for reproducible execution,
- documentation of the experimental methodology and ethical constraints.

This challenge is framed as a classroom exercise: the goal is to show how to reason about keyspace, apply filtering strategies (e.g., language patterns), and verify candidates against a known test vector — all while following ethical constraints.

---

## Quick summary for interviewers (one-minute)
- Purpose: show methodology for reducing keyspace and validating candidate keys against the DES-encrypted Base64 ciphertext `dpi4c+NIZxM=`.
- Demo plaintext (test): `patatine` (8 characters).
- Demo key (test): `mmalgeri` (8 characters).
- Safety: the script reads `candidates.txt` and tries only listed keys; it does **not** enumerate the entire 8-character space.
- One-click run: `./run_demo.sh`.

---

## Files in this repo
- `README.md` — this file.
- `demo_safe_decrypt.py` — safe demo script (tries only candidates from `candidates.txt`).
- `candidates.txt` — example candidate list (one key per line). Contains `mmalgeri` for the demo.
- `run_demo.sh` — one-click runner (creates venv, installs minimal deps, runs demo).
- `Dockerfile` — optional, minimal container for reproducible run.
- `AUTHORIZATION.md` — template/guidance for authorization (do not publish sensitive proof).
- `LICENSE` — choose and add a license (MIT recommended for examples).

---

## Skills demonstrated
- Advanced Python scripting (argparse, file I/O, exception handling).
- Applied cryptography fundamentals (DES key size, padding, Base64 handling, `pyDes` usage).
- Experimental research methodology (candidate filtering, controlled verification, reproducibility).
- Reproducible engineering (virtualenv, `run_demo.sh`, Docker).
- Performance & concurrency concepts (theory of `concurrent.futures` / threading and ethical tradeoffs).
- Documentation & ethics: how to document scope, limitations and authorization.

---

## One-click run for interviewers (local)
**Prerequisites:** Python 3.10+ and `git`.

1. Clone and enter repo:
```bash
git clone <repo-url>
cd <repo>


2. Make runner executable and run

chmod +x run_demo.sh
./run_demo.sh

#What run_demo.sh does

creates a Python virtual environment (.venv_demo),

installs pyDes (minimal dependency),

runs demo_safe_decrypt.py --candidates candidates.txt.

#Expected sample output
[INFO] Trying candidate key: mmalgeri
[FOUND] key='mmalgeri' -> plaintext: 'patatine'
[RESULT] Demo finished. For educational purposes only.

# Quick run for interviewers (Docker)

docker build -t challenge-demo .
docker run --rm challenge-demo


## Conducted Inquiry
After an authorized and methodical analysis of the hints and patterns provided with the course challenge, I reduced the unconstrained 8-character search space to a small, meaningful candidate set by applying linguistic heuristics and iterative pruning. In this controlled demo the test plaintext patatine (8 characters) was recovered using the candidate key mmalgeri (8 characters). This result is included solely for reproducibility and educational purposes.

Keywords

SecurityCourseChallenge, cryptanalysis, ethical-security, reproducible-research, DES, pyDes, base64, python, virtualenv, docker, candidate-filtering, italian-words

##Ethics & legal notice (must read)

This repository is for educational/demo purposes only.

Do not use these scripts on systems you do not own or for which you do not have explicit, written authorization.

If you conduct real security tests, keep authorization documents out of public repos; include only a short summary in AUTHORIZATION.md.



