#!/usr/bin/env python
from collections import deque

text = 'EXERCISMISAWESOME'
num_rails = 5
period = 2 * (num_rails - 1)


is_not_empty = lambda c: len(c) > 0
is_not_first = lambda c, cs: cs.index(c) > 0
is_not_short = lambda c, cs: max(len(cc) for cc in cs) == len(c)
increment_if_equal = lambda x, exp: x + 1 if x == exp else x

def encoded_indices(plaintext):
    # List of numerical indices of the chars in plaintext
    input_indices = range(len(plaintext))
    # Split indices into "cycles"---chunks of the plaintext with length equal to
    # the number of chars required to travel down and back up the fence again
    #   - e.g.: len(plaintext) = 16
    #           num_rails = 4
    #     ______cycle 1______     ______cycle 2______    partial cycle
    #    /                   \   /                   \  /            \
    #    0   1   2   3   4   5 | 6   7   8   9  10  11 |12  13  14  15
    # 0  x   .   .   .   .   . | x   .   .   .   .   . | x   .   .   .
    # 1  .   x   .       .   x | .   x   .   .   .   x | .   x   .   .
    # 2  .   .   x   .   x   . | .   .   x   .   x   . | .   .   x   .
    # 3  .   .   .   x   .   . | .   .   .   x   .   . | .   .   .   x
    # Store cycles as deques for nice popleft and pop
    input_cycles = []
    for cycle in input_indices[::period]:
        cycle_indices = deque(input_indices[cycle : cycle + period])
        input_cycles.append(cycle_indices)
    # Generate list of lists of the indices of the chars, organized by rail
    #   - following the above example:
    #       output_cycles = [[0, 6, 12],        rail 0
    #                        [1, 5, 7, 11, 13], rail 1
    #                        [2, 4, 8, 10, 14], rail 2
    #                        [3, 9]]            rail 3
    # Remove first char from each plaintext cycle to generate index sequence for
    # the first rail
    output_cycles = [[]]
    for cycle in input_cycles:
        output_cycles[0].append(cycle.popleft())
    # For each of the remaining rails, calculate its expected length based on
    # the number of chars popped in the previous iteration and the previous
    # value of the expected length. This is used to guard against popping from
    # the right of a short partial cycle (see partial cycle in the example above
    # for clarification---shouldn't pop from right of last cycle). Create an
    # empty list in output_cycles to store the current rail's index sequence.
    # For each plaintext cycle in index_cycles, if cycle is nonempty, pop the
    # element from the left and append to the current rail's index sequence.
    #   1) popleft as long as
    #   - in the first iteration, a full cycle has length equal to the original
    #     period
    expected_length = period - 2
    for rail in range(1, num_rails):
        output_cycles.append([])
        num_popped = 0
        for cycle in input_cycles:
            if len(cycle) > 0:
                output_cycles[rail].append(cycle.popleft())
                num_popped = increment_if_equal(num_popped, 0)
            if len(cycle) == expected_length > 0:
                output_cycles[rail].append(cycle.pop())
                num_popped = increment_if_equal(num_popped, 1)
        expected_length -= num_popped
    ###
    print(output_cycles)
    output_indices = []
    for index_cycle in output_cycles:
        for _index in index_cycle:
            output_indices.append(_index)
    return output_indices



def translate(input_text, index_translator):
    translated_indices = index_translator(input_text)
    output_text = ''
    for _index in translated_indices:
        output_text += input_text[_index]
    return output_text

def to_ciphertext(plaintext):
    return encoded_indices(plaintext)

def encode(plaintext):
    return translate(plaintext, to_ciphertext)

print(encoded_indices(text))
print(encode(text))
