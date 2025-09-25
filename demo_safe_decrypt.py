#!/usr/bin/env python3
"""
Brute-force DES (educational demo).
- Keys: 8 chars, lowercase English letters only (a-z)
- Ciphertext: base64 encoded
- Plaintext is checked against a built-in set of Italian words
⚠️ Use only on your own data or when explicitly authorized.
"""

import base64
import itertools
import pyDes

# --- CONFIG ---
CIPHER_B64 = "dpi4c+NIZxM="  # ciphertext to crack
KEY_LENGTH = 8
CHARSET = "abcdefghijklmnopqrstuvwxyz"

# Dizionario di esempio (puoi aggiungere altre parole italiane qui)
ITALIAN_DICT = {
    "patatine", "anatra", "cane", "gatto", "casa",
    "amore", "pane", "vino", "mare", "sole"
}


def des_decrypt_with_key(key_str: str, cipher_b64: str) -> str | None:
    """Decrypt ciphertext with candidate key, return plaintext string or None."""
    try:
        key_bytes = key_str.encode("utf-8")
        if len(key_bytes) != 8:  # DES richiede 8 byte
            return None
        k = pyDes.des(key_bytes, pyDes.ECB, padmode=pyDes.PAD_PKCS5)
        ct = base64.b64decode(cipher_b64)
        pt_bytes = k.decrypt(ct)
        pt = pt_bytes.decode("utf-8", errors="ignore").strip().lower()
        return pt
    except Exception:
        return None


def run_search():
    total = len(CHARSET) ** KEY_LENGTH
    print(f"[+] Keyspace size: {len(CHARSET)}^{KEY_LENGTH} = {total:,} combinations")
    for tpl in itertools.product(CHARSET, repeat=KEY_LENGTH):
        key = "".join(tpl)
        pt = des_decrypt_with_key(key, CIPHER_B64)
        if pt and pt in ITALIAN_DICT:
            print(f"[FOUND] key = '{key}' -> plaintext = '{pt}'")
            return
    print("[!] No key found in search space")


if __name__ == "__main__":
    run_search()
