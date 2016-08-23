#!/usr/bin/env python

import re
import string


def is_pangram(sentence):
    sentence_letters = [x.lower() for x in sentence if x.isalpha()]
    return list(string.ascii_lowercase) == sorted(set(sentence_letters))