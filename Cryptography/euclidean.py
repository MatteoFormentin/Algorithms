# EUCLIDEAN ALGORITHM
# Calculate the gcd between two number using sequential remindewr calculation
# 0 - a = q_0 * b + r_0
# 1 - b = q_1 * r_0 + r_1
# 2 - r_0 = q_2 * r_1 + r_2
# 3 - r_1 = q_3 * r_2 + r_3
# n - r_n-2 = q_n * r_n-1 + r_n
# Until r_n = 0, then r_n-1 is the gcd

import math as Math


def euclidean(a, b):
    if a < b:  # a must be greater than b
        temp = a
        a = b
        b = temp

    if a % b == 0:
        return b

    k = 0
    r_prec_prec = b  # Derived from the equations, just to compact the alg
    r_prec = a

    while True:
        k += 1
        r = r_prec % r_prec_prec

        if r == 0:
            break
        else:
            r_prec_prec = r_prec
            r_prec = r

    return r_prec
