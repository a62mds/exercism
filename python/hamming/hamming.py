#!/usr/bin/env python


def distance(str1, str2):
    if len(str1) != len(str2):
        raise ValueError('Strands not of equal length')

    return sum([1 for (n1, n2) in zip(str1, str2) if n1 != n2])