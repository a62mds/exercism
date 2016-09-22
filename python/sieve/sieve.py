#!/usr/bin/env python

def sieve(ubnd):
    cands = range(2, ubnd+1)
    for cand in cands:
        is_not_mult = lambda num: num % cand != 0 or num == cand
        cands = filter(is_not_mult, cands)
    return cands
