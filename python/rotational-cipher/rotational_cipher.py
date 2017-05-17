from string import ascii_lowercase as abcs
from string import ascii_uppercase as ABCs


charsets = [abcs, ABCs]

def charset_of(char):
    for charset in charsets:
        if char in charset:
            return charset
    raise TypeError

def char_shift(char, shift):
    try:
        charset = charset_of(char)
        shifted_index = (charset.index(char) + shift) % len(charset)
        return charset[shifted_index]
    except TypeError:
        return char

def rotate(plaintext, shift_key):
    return ''.join(map(lambda c: char_shift(c, shift_key), plaintext))
