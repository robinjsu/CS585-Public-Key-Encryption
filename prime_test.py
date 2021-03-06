import os
import secrets
import random
import constant as c

# p - 1 = 2^u * r
def decompose(p):
    power = 0
    exp = 0
    while True:
        exp = pow(2,power)
        dividend = (p-1) // exp
        if dividend % 2 == 1:
            return power, dividend
        power += 1

# based on the Miller-Rabin algorithm written in pseudocode in Paar textbook, pg. 191 
# and Wikipedia:https://en.wikipedia.org/wiki/Miller%E2%80%93Rabin_primality_test
def mr_prime(p, s):
    if p % 2 == 0:
        return False
    u, r = decompose(p)
    for i in range(s):
        a = random.randrange(2, p-2)
        z = pow(a,r,p)
        if z == 1 or z == p-1:
            continue
        for j in range(u-1):
            z = pow(z,2,p)
            if z == (p-1):
                break
        else:
            return False
    return True

def miller_rabin(p):
    return mr_prime(p, c.MR_ROUNDS)
     