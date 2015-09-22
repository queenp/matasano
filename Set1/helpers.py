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
