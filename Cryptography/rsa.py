p, q = 0
e = 127


def rsa_generate_key_pair():
    # generate public key
    n = p * q  # mod n
    lambda_n = (p-1) * (q - 1)
    # generate private key
    # d ≡ e−1 (mod λ(n))

def rsa_encrypt(n, e):
    pass


def rsa_decrypt():
    pass
