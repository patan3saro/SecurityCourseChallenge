#!/usr/bin/env python3
"""
DES key search (lowercase-only keys) + plaintext dictionary match.

WARNING: Run only on data you own or when explicitly authorized.
"""

import base64
import itertools
import multiprocessing as mp
import re
from typing import Set, Optional

import pyDes  # pip install pyDes

# --- CONFIG ---
DICTIONARY_PATH = r"C:\Users\Utente\Desktop\660000_parole_italiane.txt"
CIPHER_B64 = "dpi4c+NIZxM="    # ciphertext (base64)
KEY_LENGTH = 8                # assumed key length (DES key = 8 bytes)
CHARSET = "abcdefghijklmnopqrstuvwxyz"
NUM_PROCESSES = max(1, mp.cpu_count() - 1)
CHUNK_SIZE = 2000             # tune: how many candidates per task batch
VERBOSE = True

# --- helpers ---
_non_alpha_re = re.compile(r"[^A-Za-zÀ-ú]+")  # split tokens (includes accented letters)


def load_dictionary(path: str) -> Set[str]:
    s = set()
    try:
        with open(path, "r", encoding="utf-8", errors="ignore") as f:
            for L in f:
                w = L.strip()
                if w:
                    s.add(w.lower())
        if VERBOSE:
            print(f"[+] Loaded {len(s):,} words from dictionary.")
    except FileNotFoundError:
        if VERBOSE:
            print(f"[!] Dictionary file not found at: {path}. Continuing with empty set.")
    return s


def des_decrypt_with_key(key_bytes: bytes, cipher_b64: str) -> Optional[bytes]:
    """
    Try to decrypt; return plaintext bytes or None on failure.
    Note: pyDes.des expects an 8-byte key for DES.
    """
    try:
        k = pyDes.des(key_bytes, pyDes.ECB, padmode=pyDes.PAD_PKCS5)
        cipher = base64.b64decode(cipher_b64)
        return k.decrypt(cipher)
    except Exception:
        return None


def plaintext_matches_dictionary(plaintext_bytes: bytes, dictionary: Set[str]) -> bool:
    """
    Decode plaintext (utf-8, replace errors), split into tokens and check
    if any token is present in the dictionary.
    Also check whole-text match.
    """
    try:
        txt = plaintext_bytes.decode("utf-8", errors="replace").strip()
    except Exception:
        return False
    if not txt:
        return False

    low = txt.lower()
    # whole-text exact match
    if low in dictionary:
        return True
    # token-based match
    tokens = [t for t in _non_alpha_re.split(low) if t]
    for tok in tokens:
        if tok in dictionary:
            return True
    return False


def worker_batch(candidates_chunk, cipher_b64, dictionary, found_event, result_queue):
    """
    Try a chunk of candidate keys. If found, set found_event and push result.
    """
    if found_event.is_set():
        return
    for pwd in candidates_chunk:
        if found_event.is_set():
            return
        key = pwd.encode("utf-8", errors="ignore")
        if len(key) != 8:
            continue  # DES needs 8-byte key
        pt = des_decrypt_with_key(key, cipher_b64)
        if pt is None:
            continue
        if plaintext_matches_dictionary(pt, dictionary):
            # put result and signal others to stop
            result_queue.put((pwd, pt))
            found_event.set()
            return


def candidate_generator(charset, length):
    """Yield candidate strings (lazy)."""
    for tpl in itertools.product(charset, repeat=length):
        yield "".join(tpl)


def run_search():
    dictionary = load_dictionary(DICTIONARY_PATH)
    manager = mp.Manager()
    found_event = manager.Event()
    result_queue = manager.Queue()

    gen = candidate_generator(CHARSET, KEY_LENGTH)

    # Create process pool
    pool = mp.Pool(processes=NUM_PROCESSES)
    tasks = []
    submitted = 0

    try:
        # Submit chunks of candidates to the pool
        while True:
            if found_event.is_set():
                break
            # build a chunk
            chunk = []
            try:
                for _ in range(CHUNK_SIZE):
                    chunk.append(next(gen))
            except StopIteration:
                # exhausted generator
                if not chunk:
                    break
            submitted += len(chunk)
            if VERBOSE and submitted % (CHUNK_SIZE * 50) == 0:
                print(f"[+] Submitted ~{submitted:,} candidates...")
            # submit async
            tasks.append(pool.apply_async(worker_batch, (chunk, CIPHER_B64, dictionary, found_event, result_queue)))

        # wait for either a result or completion
        pool.close()
        # Wait until a result is found or all tasks finish
        while True:
            if not result_queue.empty():
                pwd, pt = result_queue.get()
                if VERBOSE:
                    print(f"[FOUND] key: {pwd}")
                    print(f"[PLAINTEXT] {pt.decode('utf-8', errors='replace')!r}")
                break
            all_done = all(t.ready() for t in tasks)
            if all_done:
                if VERBOSE:
                    print("[!] All tasks finished; no match found.")
                break
            # small sleep to avoid busy loop
            import time
            time.sleep(0.1)

    finally:
        # tidy up
        try:
            pool.terminate()
        except Exception:
            pass
        pool.join()


if __name__ == "__main__":
    # quick safety check: how large is keyspace?
    keyspace = len(CHARSET) ** KEY_LENGTH
    if VERBOSE:
        print(f"[+] Keyspace size: {len(CHARSET)}^{KEY_LENGTH} = {keyspace:,} combos")
    # For big keyspaces, be careful: you might want to reduce KEY_LENGTH or CHARSET for tests
    run_search()
