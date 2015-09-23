#!/usr/bin/python
# Ohh, La, Vigenere

import sys
import collections
from helpers import *

# find repeated key size by statistical analysis
def find_r_keysizes(ctext,search_range):
    scores = collections.defaultdict(float)
    for keylen in search_range:
        sample_1 = ctext[:4*keylen]
        sample_2 = ctext[4*keylen:8 * keylen]
        scores[keylen] = float(hamming(sample_1,sample_2))/keylen
    return sorted(scores.items(), key=lambda x: x[1])

def main():
    ctext_b64 = ""

    with open("6.txt",'r') as f:
        ctext_b64 = f.read().replace('\n','')

    ctext_buf = ctext_b64.decode('base64')

    # get candidate repeated key sizes, ordered by probability
    keysizes = find_r_keysizes(ctext_buf, range(2,41))
    key = ''
    for (size,_) in keysizes:
        for i in range(size):
            stripe = stripe_buf(ctext_buf,i,size)
            key = key + solve_xorc(stripe)
        # easily achievable score for almost any plain text
        if float(score_freq(lxor_buf(ctext_buf,key)))/len(ctext_buf) < 20:
            print(lxor_buf(ctext_buf,key))
            break;

if __name__ == "__main__":
    main()
