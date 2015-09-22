# XOR 2 equal length buffers
def xor_buf(buf_a, buf_b):
    buf_ret = [chr(ord(a)^ord(b)) for a,b in zip(buf_a, buf_b)]
    return "".join(buf_ret)

# XOR 1 buffer with against a looped, shorter buffer
def lxor_buf(buf_a, buf_l):
    loop_buf = buf_l * (len(buf_a)/len(buf_l)) + buf_l[:(len(buf_a) % len(buf_l))]
    return "".join(xor_buf(buf_a,loop_buf))
