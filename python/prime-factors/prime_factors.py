from itertools import repeat
from sympy.ntheory import factorint


def prime_factors(num):
    primes = factorint(num)
    return sorted(list(ii for k in primes for ii in repeat(k, primes[k])))
