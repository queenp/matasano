#!/usr/bin/python
import string
import sys
from helpers import lxor_buf

def main():
    ciphertext = sys.argv[1].decode('hex') # straight to binary buffer
    for x in range(0,256):
        candidate = lxor_buf(ciphertext,chr(x))
        if not len([c for c in candidate if c not in string.printable]) > 0:
            print chr(x).encode('hex') + " : " + candidate

if __name__ == "__main__":
    main()
