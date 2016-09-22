#!/usr/bin/env python
from string import ascii_lowercase as abcs


ekey = dict(zip(abcs, reversed(abcs)))
dkey = {v : k for k, v in ekey.iteritems()}

def decode(encstr):
    subst = lambda c: dkey[c] if c.isalpha() else c
    return ''.join(map(subst, ''.join(encstr.split())))

def encode(rawstr):
    subst = lambda c: ekey[c] if c.isalpha() else c
    encstr = ''.join(map(subst, ''.join(c.lower() for c in rawstr if c.isalnum())))
    return ' '.join(encstr[i:i+5] for i in xrange(0, len(encstr), 5))
