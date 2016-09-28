
prod = lambda numlist: reduce(lambda x, y: x * y, numlist, 1)

def largest_product(numstr, ns):
    if not 0 <= ns:
        raise ValueError('Invalid substring length: {}'.format(ns))
    nums = lambda ii: map(int, list(numstr[ii : ii + ns]))
    num_substrs = len(numstr) - ns + 1
    return max(prod(nums(ii)) for ii in range(num_substrs))
