# Functional solution
from string import ascii_lowercase


_hex_digits = map(str, range(10)) + list(ascii_lowercase[0:6])
_hex_to_dec = {v : k for k, v in enumerate(_hex_digits)}

def hexa(hex_str):
    lower_hex_str = hex_str.lower()
    if not (isinstance(hex_str, str) and
            all(c in _hex_digits for c in lower_hex_str)):
        raise ValueError("Invalid hex string: {:s}".format(hex_str))
    reverse = lambda seq: seq[::-1]
    indexed_hex_dgts = enumerate(reverse(lower_hex_str))
    pows_of_16 = map(lambda (i, d): _hex_to_dec[d] * 16**i, indexed_hex_dgts)
    return sum(pows_of_16)
