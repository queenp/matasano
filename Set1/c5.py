#!/usr/bin/python
from helpers import *
import sys

PLAINSTRING = "Burning 'em, if you ain't quick and nimble\nI go crazy when I hear a cymbal"

def main():
    # Easy peasy because I implemented a looped xor anyway for the single char case
    xored = lxor_buf(PLAINSTRING, "ICE")
    print xored.encode('hex')
    sys.exit(0)

if __name__ == "__main__":
    main()
