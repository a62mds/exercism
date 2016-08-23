# -*- coding: utf-8 -*-
#!/usr/bin/env python
from re import sub

# Adapted from rosettacode.org/wiki/Run-length_encoding#Python
def encode(inp):
    # Do not explicitly include char '1' in encoded string when single char is
    # encountered.
    # re.sub(rgx, rule, str) maps string str to a new string with all substrings
    # of str that match rgx replaced according to rule. In this case, the
    # rule is provided by to_enc, which says to replace a substr consisting of
    # n >= 1 identical chars by str(n)+char, except in the case n = 1. In this
    # case, including the char '1' is unnecessary, and a char that is not
    # prepended by a digit is handled accordingly.
    count  = lambda s: len(s.group(0))  # holds the number of identical chars
    char   = lambda s: s.group(1)       # holds the char
    to_enc = lambda s: char(s) if count(s) == 1 else str(count(s)) + char(s)
    return sub(r'(.)\1*', to_enc, inp)


# Directly from rosettacode.org/wiki/Run-length_encoding#Python
def decode(inp):
    # Replace substrings matching (digits)(other_char) by digits many concat'd
    # other_char's
    from_enc = lambda s: s.group(2) * int(s.group(1))
    return sub(r'(\d+)(\D)', from_enc, inp)
