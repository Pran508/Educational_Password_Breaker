from __future__ import annotations

import argparse
import hashlib
import itertools
import string
import sys
import time

SUPPORTED = ("md5", "sha1", "sha224", "sha256", "sha384", "sha512")

def hash_word(word: str, algo: str, salt: str = "") -> str:
    """Hash 'salt + word' with the chosen algorithm and return the hex digest."""
    h = hashlib.new(algo)
    h.update((salt + word).encode("utf-8"))
    return h.hexdigest()

def dictionary_attack(target: str, algo: str, wordlist_path: str, salt: str = "") -> str | None:
    """Try every word in a wordlist. Returns the plaintext if found, else None."""
    target = target.lower()
    with open(wordlist_path, "r", encoding="utf-8", errors="ignore") as f:
        for line in f: 
            word - line.rstrip("\n")
            if hash_word(word, algo, salt) == target:
                return word
    return None



