#!/usr/bin/env python

def slices(digit_string, substr_len):
    # Validity checks
    if substr_len <= 0:
        raise ValueError('Substring length must be positive')
    elif substr_len > len(digit_string):
        raise ValueError('Substring length must be less than or equal to\
                         length of input string')
    # Return list of contiguous slices of specified length
    individual_digits_of = lambda digit_string: map(int, list(digit_string))
    contiguous_slices_of = lambda lst: slice(lst, substr_len)
    list_of = lambda string: list(string)
    return list_of(contiguous_slices_of(individual_digits_of(digit_string)))

# Generator function for generating subsequences of a given input sequence
# with specified length
def slice(string, substr_len):
    num_substrs = len(string) - substr_len + 1
    for first_char in range(num_substrs):
        yield string[first_char : first_char + substr_len]
