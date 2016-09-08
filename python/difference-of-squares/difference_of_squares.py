#!/usr/bin/env python

sq = lambda n: n * n
square_of_sum = lambda n: sq(sum(n for n in range(1, n+1)))
sum_of_squares = lambda n: sum(sq(n) for n in range(1, n+1))
difference = lambda n: abs(sum_of_squares(n) - square_of_sum(n))
