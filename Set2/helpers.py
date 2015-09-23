def PKCS7_pad(plain,blocksize):
    pad_len = blocksize - (len(plain)% blocksize)
    pad = chr(pad_len) * pad_len if not len(plain) % blocksize == 0 else chr(0) * blocksize
    return plain + pad
