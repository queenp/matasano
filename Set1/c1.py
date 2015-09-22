#!/usr/bin/python

import sys
import argparse

def main():
    arg1 = sys.argv[1]
    print arg1.decode('hex').encode('base64')

if __name__ == "__main__":
    main()
