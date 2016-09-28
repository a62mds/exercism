#!/usr/bin/env python
from re import sub

def abbreviate(phrase):
    # Replace any punctuation with whitespace
    phrase = sub(r'[^\w]+', r' ', phrase)
    # Insert a single space before any mid-word capital letters
    phrase = sub(r'(?<=[a-z])([A-Z])', r' \1', phrase)
    # Split phrase at whitespace
    words = phrase.split()
    # Get first letter from each word and capitalize
    letters = [w[0].upper() for w in words]
    # Join letters into string and return
    return ''.join(letters)
