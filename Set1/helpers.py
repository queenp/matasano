from collections import Counter, defaultdict

# list of characters in text ordered by frequency from most common to least
expected_order = ' etaoinsrhldcumfgpyw\r\nb,.vk-"_\'x)(;0j1q=2:z/*!?$35>{}49[]867\\+|&<%@#^`~'

def allowed(buff, allowable = expected_order):
    return (len([c for c in buff.lower() if c not in allowable]) == 0)

# XOR 2 equal length buffers
def xor_buf(buf_a, buf_b):
    buf_ret = [chr(ord(a)^ord(b)) for a,b in zip(buf_a, buf_b)]
    return "".join(buf_ret)

# XOR 1 buffer with against a looped, shorter buffer
def lxor_buf(buf_a, buf_l):
    loop_buf = buf_l * (len(buf_a)/len(buf_l)) + buf_l[:(len(buf_a) % len(buf_l))]
    return "".join(xor_buf(buf_a,loop_buf))

# digest a candidate to dict of chars and frequencies
def char_freq_count(cand):
    counts = Counter(cand)
    return counts

# Score based on ordering of common letters. Lower is more "normative" English.
# This scoring mechanism *seriously* exaggerates unusual chars.
# Which is good because failed decryption probably has glaring incorrectnesses
def score_freq(cand):
    points = defaultdict(lambda: 100)
    for i in range(len(expected_order)):
        points[expected_order[i]] = i
    score = 0
    for c in cand.lower():
        score += points[c]
    return score

# Solve most probable xor char for a single char xor
def solve_xorc(buff):
    score = float('inf')
    best = ''
    for i in range(0,256):
        x = score_freq(lxor_buf(buff,chr(i)))
        if x < score:
            score = x
            best = chr(i)
    return best

# Return a stripe of a buffer's ith characters mod q
def stripe_buf(buff,i,q):
    return "".join([c for idx, c in enumerate(buff) if idx%q==i])

# My bitwise maths is probably inelegant here. For shame
def hamming_weight(some_string):
    weight = 0
    i = 0
    for c in some_string:
        i = ord(c)
        while i > 0:
            weight += (i & 0b1)
            i = i >> 1
    return weight

def hamming(str_1, str_2):
    x = xor_buf(str_1,str_2)
    return hamming_weight(x)

# find repeated key size by statistical analysis
def find_r_keysizes(ctext,search_range):
    scores = collections.defaultdict(float)
    for keylen in search_range:
        sample_1 = ctext[:4*keylen]
        sample_2 = ctext[4*keylen:8 * keylen]
        scores[keylen] = float(hamming(sample_1,sample_2))/keylen
    return sorted(scores.items(), key=lambda x: x[1])

def crack_vigenere(buf,key_size_range):
    # get candidate repeated key sizes, ordered by probability
    keysizes = find_r_keysizes(buf, key_size_range)
    key = ''
    for (size,_) in keysizes:
        for i in range(size):
            stripe = stripe_buf(buf,i,size)
            key = key + solve_xorc(stripe)
        # easily achievable score for almost any plain text
        if float(score_freq(lxor_buf(buf,key)))/len(buf) < 20:
            return (lxor_buf(buf,key))
