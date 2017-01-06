# Fast method for computing all integer factors of an integer n. Obtained from
# http://stackoverflow.com/questions/6800193/what-is-the-most-efficient-way-of-finding-all-the-factors-of-a-number-in-python
def factors(n):
    return set(reduce(list.__add__,
                ([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0)))

def is_perfect(n):
    return n == sum(f for f in factors(n) if f != n)
