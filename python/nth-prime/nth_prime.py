#!/usr/bin/env python
import math


def is_prime(nn):
    if nn == 2:
        return True
    elif nn % 2 == 0:
        return False
    upper_bnd = int(math.floor(math.sqrt(nn))) + 1
    for ii in range(3, upper_bnd, 2):
        if nn % ii == 0:
            return False
    return True

def nth_prime(nn):
    count, num = 0, 1
    while True:
        num += 1
        if is_prime(num):
            count += 1
        if count == nn:
            return num


# :-)
