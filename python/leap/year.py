#!/usr/bin/env python

def is_leap_year(year):
    cond1 = (divides(4, year) and divides(400, year))
    cond2 = (divides(4, year) and not divides(100, year))
    return cond1 or cond2

def divides(divisor, dividend):
    return dividend % divisor == 0
