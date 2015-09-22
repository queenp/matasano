#!/usr/bin/python
import string
import sys
from collections import Counter
from helpers import *

# A fast/lazy/stupid way to turn up some good candidates by eyeball.
# No good for searching through bulk for xored strings amongst binary chaff
# OUTPUT:
# $ ./c3.py 1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736
# 47 : \pptvqx?R\8l?svtz?~?opjq{?py?}~|pq
# 4a : Q}}y{|u2_Q5a2~{yw2s2b}g|v2}t2psq}|
# 4d : Vzz~|{r5XV2f5y|~p5t5ez`{q5zs5wtvz{
# 4f : Txx|~yp7ZT0d7{~|r7v7gxbys7xq7uvtxy
# 50 : Kggcafo(EK/{(dacm(i(xg}fl(gn(jikgf
# 51 : Jffb`gn)DJ.z)e`bl)h)yf|gm)fo)khjfg
# 53 : Hdd`bel+FH,x+gb`n+j+{d~eo+dm+ijhde
# 55 : Nbbfdcj-@N*~-adfh-l-}bxci-bk-olnbc
# 56 : Maaeg`i.CM)}.bgek.o.~a{`j.ah.loma`
# 58 : Cooking MC's like a pound of bacon
# 59 : Bnnjhof!LB&r!mhjd!`!qntoe!ng!c`bno
# 5a : Ammikle"OA%q"nkig"c"rmwlf"md"`caml
# ....
def brute_xor(buff):
    for x in range(0,256):
        candidate = lxor_buf(buff,chr(x))
        if not len([c for c in candidate if c not in string.printable]) > 0:
            print chr(x).encode('hex') + " : " + candidate


def main():
    ciphertext = sys.argv[1].decode('hex') # straight to binary buffer
    best_cand = ""
    best_xor = ""
    for x in range(0,256):
        candidate = lxor_buf(ciphertext,chr(x))
        if best_cand == "" or score_freq(candidate) < score_freq(best_cand):
            best_cand = candidate
            best_xor = hex(x)
    print best_xor + " : " + best_cand

if __name__ == "__main__":
    main()
