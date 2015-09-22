def xor_buf(buf_a, buf_b):
    buf_r = [chr(ord(a)^ord(b)) for a,b in zip(buf_a, buf_b)]
    return "".join(buf_r)

