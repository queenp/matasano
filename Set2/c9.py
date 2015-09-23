#!/usr/bin/python
from helpers import *
import sys


def main():
    plain = sys.argv[1]
    blocksize = int(sys.argv[2])
    print repr(PKCS7_pad(plain,blocksize))


if __name__ == "__main__":
    main()
