#!/usr/bin/env python
from itertools import count
from itertools import takewhile


def multiples_of(num, ubnd=100):
    # Generator expression for multiples
    mults = (num * ii for ii in count(1))
    # Returns an iterator that that runs through all multiples of num greater
    # than 0 and less than the specified upper bound
    return takewhile(lambda m: 0 < m < ubnd, mults)

def sum_of_multiples(ubnd, nums):
    # Generate nested lists of multiples of all numbers in nums
    mults = (multiples_of(num, ubnd) for num in nums)
    # Flatten the nested lists and get rid of duplicates
    uniq_mults = set(m for mlist in mults for m in mlist)
    # Return the sum
    return sum(uniq_mults)
