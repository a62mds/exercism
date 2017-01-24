def is_palindrome((number, factors)):
    return str(number) == str(number)[::-1]

def products_of(rng):
    return [(x*y, (x, y)) for x in rng for y in rng]

def palindrome_products(max_factor=9, min_factor=0):
    candidate_factors = range(max(min_factor, 1), max_factor+1)
    candidate_products = products_of(candidate_factors)
    return filter(is_palindrome, candidate_products)

def smallest_palindrome(max_factor=9, min_factor=0):
    return min(palindrome_products(max_factor=max_factor, min_factor=min_factor))

def largest_palindrome(max_factor=9, min_factor=0):
    return max(palindrome_products(max_factor=max_factor, min_factor=min_factor))
