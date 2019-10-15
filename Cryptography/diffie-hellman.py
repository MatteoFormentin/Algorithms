# Diffie-Hellman Key Establishment protocol
# How it Works: A choose a secret a send g^a mod p to B, which reply with g^b mod p with b secret.
# Since B^a mod p = A^b mod p = K they have both the data needed to calculate the key K.

import math as Math


# Simulate A
def establish_key(a, b, g, p):
    A = g ** a % p
    B = reply_establish_key(b, g, p, A)  # Send A to B, B reply with B value
    K = B ** a % p
    return K 


# Simulate B
def reply_establish_key(b, g, p, A):
    B = g ** b % p
    K = A ** b % p
    return B  # Send B to A
