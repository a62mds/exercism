from math import floor
from math import sqrt

sq = lambda x: x * x
succ = lambda n: n + 1

def get_elem(seq, n):
    return '' if n >= len(seq) else seq[n]

def take(seq, start, num):
    return seq[start : start + num]

def encode(msg):
    if not msg:
        return msg
    # Remove all whitespace and non alphanumeric chars
    normalize = lambda cs: ''.join(c.lower() if c.isalnum() else '' for c in cs)
    n_msg = normalize(msg)
    # Get the number of rows and columns of the crypto-square
    num_rows = int(floor(sqrt(len(n_msg))))
    num_cols = num_rows if len(n_msg) == sq(num_rows) else succ(num_rows)
    # Breaks the normalized string into rows (kind of like storing a matrix in
    # row-major order)
    rows = [take(n_msg, ii, num_cols) for ii in range(0, len(n_msg), num_cols)]
    # Converts the row-major storage into column-major storage
    cols = [''.join(get_elem(r, c) for r in rows) for c in range(num_cols)]
    # Join columns and return encrypted msg
    return ' '.join(cols)
