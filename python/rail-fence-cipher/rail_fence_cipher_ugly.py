# Imperative OOP style solution
from collections import deque
from collections import namedtuple


# Data type for storing information about encrypted characters
EncChar = namedtuple('EncChar', 'row col char')

class RailFenceCipher(object):

    # Successor and predecessor operations
    succ = staticmethod(lambda x: x + 1)
    pred = staticmethod(lambda x: x - 1)

    def __init__(self, num_rails):
        self.num_rails = num_rails

    def fenced(self, plaintext):
        """
        Imperative style function that takes a string and returns a list of
        triples (row, col, char)---one for each char in the plaintext string.
        Taking the fence positions as a rectangular array, the row and col
        values are assigned in the obvious way
        """
        # Switches between successor and predecessor operations in order to
        # follow the zig-zag pattern
    	switch = lambda op: self.succ if op == self.pred else self.pred
        # Initialize a list of EncChars
    	ct = []
        # Initialize row index
    	row = -1
        # Begin with successor operation
    	op = self.succ
        # Build list of EncChars
    	for col in range(len(plaintext)):
            # update the row index accordingly and append (row, col, char) to
            # the list of EncChars
    		row = op(row)
    		ct.append(EncChar(row, col, plaintext[col]))
            # if applying op to row results in either a negative number or a
            # number larger than the number of rails, switch the operation
    		if op(row) not in range(self.num_rails):
    			op = switch(op)
        return ct

    def defenced(self, ciphertext):
        # Define a lambda for incrementing only if a value is as expected
        increment_if_equal = lambda x, exp: x + 1 if x == exp else x

        index_spacing = 2 * (self.num_rails - 1)
        indices = range(len(ciphertext))
        index_chunks = [deque(indices[ii:ii+index_spacing])
                        for ii in indices[::index_spacing]]

        row_indices = [[chunk.popleft() for chunk in index_chunks]]
        exp_len = index_spacing - 2
        for row in range(1, self.num_rails):
            row_indices.append([])
            removed = 0
            for chunk in index_chunks:
                if len(chunk) > 0:
                    row_indices[row].append(chunk.popleft())
                    removed = increment_if_equal(removed, 0)
                if len(chunk) == exp_len and exp_len > 0:
                    row_indices[row].append(chunk.pop())
                    removed = increment_if_equal(removed, 1)
            exp_len -= removed
        return [ii for chunk in row_indices for ii in chunk]

    def encode(self, plaintext):
        # For sorting list of EncChars by row and column
        #   -> row0, col0
        #      row0, col1
        #         ...
        #      row0, col(last)
        #      row1, col0
        #         ...
        #      row1, col(last)
        #      row(last), col0
        #         ...
        #      row(last), col(last)
        esort = lambda enc_char: (enc_char.row, enc_char.col)
        # Build encrypted string one char at a time
        ciphertext = ''
        for enc_char in sorted(self.fenced(plaintext), key=esort):
            ciphertext = ciphertext + enc_char.char
        return ciphertext

    def decode(self, ciphertext):
        indices = self.defenced(ciphertext)
        plaintext = list(ciphertext)
        for ii in range(len(indices)):
            plaintext[indices[ii]] = ciphertext[ii]
        return ''.join(c for c in plaintext)

####

def encode(plaintext, num_rails):
    return RailFenceCipher(num_rails).encode(plaintext)

def decode(ciphertext, num_rails):
    return RailFenceCipher(num_rails).decode(ciphertext)
