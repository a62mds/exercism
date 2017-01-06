# Imperative OOP style solution
from collections import deque

increment_if_equal = lambda x, exp: x + 1 if x == exp else x

class RailFenceCipher(object):

    def __init__(self, num_rails):
        self.num_rails = num_rails
        self.period = 2 * (self.num_rails - 1)

    def encoded_indices(self, plaintext):
        # List of numerical indices of the chars in plaintext
        input_indices = range(len(plaintext))
        # Split indices into "cycles"---chunks of the plaintext with length
        # equal to the number of chars required to travel down and back up the
        # fence again
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
        for cycle in input_indices[::self.period]:
            cycle_indices = deque(input_indices[cycle : cycle + self.period])
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
        # For each of the remaining rails, calculate its expected length based
        # on the number of chars popped in the previous iteration and the
        # previous value of the expected length. This is used to guard against
        # popping from the right of a short partial cycle (see partial cycle in
        # the example above or clarification---shouldn't pop from right of last
        # cycle). Create an empty list in output_cycles to store the current
        # rail's index sequence. For each plaintext cycle in index_cycles, if
        # cycle is nonempty, pop the element from the left and append to the
        # current rail's index sequence
        expected_length = self.period - 2
        for rail in range(1, self.num_rails):
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
        output_indices = []
        for index_cycle in output_cycles:
            for _index in index_cycle:
                output_indices.append(_index)
        return output_indices

    def to_ciphertext(self, plaintext):
        return self.encoded_indices(plaintext)

    def to_plaintext(self, ciphertext):
        pt_indices = []
        ct_indices = self.encoded_indices(ciphertext)
        for ct_index in range(len(ciphertext)):
            pt_indices.append(ct_indices.index(ct_index))
        return pt_indices

    def translate(self, input_text, index_translator):
        translated_indices = index_translator(input_text)
        output_text = ''
        for index in translated_indices:
            output_text += input_text[index]
        return output_text

    def encode(self, plaintext):
        return self.translate(plaintext, self.to_ciphertext)

    def decode(self, ciphertext):
        return self.translate(ciphertext, self.to_plaintext)

####

def encode(plaintext, num_rails):
    return RailFenceCipher(num_rails).encode(plaintext)

def decode(ciphertext, num_rails):
    return RailFenceCipher(num_rails).decode(ciphertext)
