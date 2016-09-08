#!/usr/bin/env python

def detect_anagrams(word, candidates):
    is_permutation = lambda str1, str2: sorted(str1) == sorted(str2)
    is_anagram = lambda str1, str2: is_permutation(str1, str2) and not str1==str2
    return [cand for cand in candidates if is_anagram(word.lower(), cand.lower())]
