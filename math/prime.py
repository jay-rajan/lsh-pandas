# Sieve of Eratosthenes
# David Eppstein, UC Irvine, 28 Feb 2002

from __future__ import generators


def prime_generator():
    closure = {}  # map composite integers to primes witnessing their compositeness
    q = 2  # first integer to test for primality
    while 1:
        if q not in closure:
            yield q  # not marked composite, must be prime
            closure[q * q] = [q]  # first multiple of q not already marked
        else:
            for p in closure[q]:  # move each witness to its next multiple
                closure.setdefault(p + q, []).append(p)
            del closure[q]  # no longer need D[q], free memory
        q += 1
