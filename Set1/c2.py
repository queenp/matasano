#!/usr/bin/python

import sys
from helpers import xor_buf

def main():
    arg1 = sys.argv[1].decode('hex') # straight to binary buffer
    arg2 = sys.argv[2].decode('hex') # likewise
    print xor_buf(arg1,arg2)
    print xor_buf(arg1,arg2).encode('hex')

if __name__ == "__main__":
    main()
