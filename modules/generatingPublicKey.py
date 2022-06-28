import random
import math

def primesMethod(n):
    out = list()
    sieve = [True] * (n+1)
    for p in range(2, n+1):
        if (sieve[p] and sieve[p]%2==1):
            out.append(p)
            for i in range(p, n+1, p):
                sieve[i] = False
    return out

def getFirstPrime():
    firstPrime = random.choice(primesMethod(300))
    return firstPrime

def getSecondPrime(firstPrime):
    while True:
        secondPrime = random.choice(primesMethod(300))
        if secondPrime != firstPrime:
            return secondPrime
        continue

def multiplication(p, q):
    n = p * q
    return n

def EulerFunction(p, q):
    phi = (p - 1) * (q - 1)
    return phi

def exponent(phi):
    e = 2
    while e < phi:
        if math.gcd(e, phi) == 1:
            break
        else:
            e += 1
    return e