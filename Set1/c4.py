#!/usr/bin/python
import sys
from helpers import *

def main():
    with open(sys.argv[1],'r') as f:
        highscore = float('inf') # cheap and dirty hack for bigger than everything
        plain = ""
        for line in f:
            # again straight to byte representation
            ctext = line.rstrip('\n').decode('hex')

            # not very memory efficient, but convenient
            scores = {chr(i):score_freq(lxor_buf(ctext,chr(i))) for i in range(0,256)}

            best = min(scores,key=scores.get)
            if scores[best] < highscore:
                highscore = scores[best]
                plain = lxor_buf(ctext, best)
        print plain

if __name__ == "__main__":
    main()
