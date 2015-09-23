#!/usr/bin/python
# Ohh, La, Vigenere

import sys
from helpers import *
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend

KEY = "YELLOW SUBMARINE"


# I really ought to contribute to pyca again at some point

def main():
    ctext_b64 = ""

    with open("7.txt",'r') as f:
        ctext_b64 = f.read().replace('\n','')
    ctext_buf = ctext_b64.decode('base64')

    alg = algorithms.AES(KEY)
    mode = modes.ECB()
    backend = default_backend()

    cipher = Cipher(alg, mode, backend)
    dec = cipher.decryptor()
    print dec.update(ctext_buf) + dec.finalize()

if __name__ == "__main__":
    main()
