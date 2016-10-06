from itertools import cycle
from random import choice
from string import ascii_lowercase as abcs


class SimpleCipher(object):
    def __init__(self):
        pass
    @staticmethod
    def strip_invalid(plaintext):
        return ''.join(c.lower() if c.isalpha() else '' for c in plaintext)
    @staticmethod
    def transcribe(shifts, chars):
        _indices = [abcs.index(c) for c in chars]
        _shifted = [(i + s) % len(abcs) for i, s in zip(_indices, shifts)]
        return ''.join(abcs[ii] for ii in _shifted)
    def encode(self, shifts, plaintext):
        return self.transcribe(shifts, self.strip_invalid(plaintext))
    def decode(self, deshifts, ciphertext):
        return self.transcribe(deshifts, ciphertext)

class Caesar(SimpleCipher):
    def __init__(self):
        self.shift = abcs.index('d')
    def encode(self, plaintext):
        shifts = [self.shift for _ in range(len(plaintext))]
        return SimpleCipher.encode(self, shifts, plaintext)
    def decode(self, ciphertext):
        deshifts = [-self.shift for _ in range(len(ciphertext))]
        return SimpleCipher.decode(self, deshifts, ciphertext)

class Cipher(SimpleCipher):
    @staticmethod
    def genkey(length):
        return ''.join(choice(abcs) for _ in range(length))
    @staticmethod
    def validate(key):
        if not all(c.isalpha() and c.islower() for c in key):
            raise ValueError('Key contains illegal chars (use a-z only)')
        else:
            return key
    def __init__(self, *key):
        self.key = self.validate(*key) if key else self.genkey(100)
    def encode(self, plaintext):
        _shifts = cycle(abcs.index(c) for c in self.key)
        shifts = [_shifts.next() for _ in range(len(plaintext))]
        return SimpleCipher.encode(self, shifts, plaintext)
    def decode(self, ciphertext):
        _deshifts = cycle(-abcs.index(c) for c in self.key)
        deshifts = [_deshifts.next() for _ in range(len(ciphertext))]
        return SimpleCipher.decode(self, deshifts, ciphertext)
