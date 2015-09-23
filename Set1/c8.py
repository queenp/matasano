#!/usr/bin/python
# Ohh, La, Vigenere

import sys
from textwrap import wrap
from collections import Counter
from helpers import *

BLOCK_SIZE = 16 #bytes

# I really ought to contribute to pyca again at some point

def main():
    ctext_b64 = ""

    with open("8.txt",'r') as f:
        lines=0
        for line in f:
            lines += 1
            c_line = line.replace('\n','')
            # Easy way to split by BLOCK_SIZE
            # Warning: don't do this on actual binary strings
            blocks = wrap(c_line, BLOCK_SIZE*2)
            cnt = Counter(blocks)
            # split line into BLOCK_SIZEd chunks, check for uniqueness.
            for x in cnt:
                if cnt[x] > 1:
                    print "ECB found: " + c_line
                    print "Duplicate: " + x
        print

if __name__ == "__main__":
    main()
