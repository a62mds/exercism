# Functional version
def parse_binary(bin_str):
    # Validate the input
    if not (isinstance(bin_str, str) and all(d in ['0','1'] for d in bin_str)):
        raise ValueError('Invalid binary string: {:s}'.format(bin_str))
    # Reverse the binary string so that it may be read from left to right
    reverse = lambda seq: seq[::-1]
    indexed_bin_dgts = enumerate(reverse(bin_str))
    pows_of_2 = map(lambda (i, d): 2**i if d == '1' else 0, indexed_bin_dgts)
    return sum(pows_of_2)
