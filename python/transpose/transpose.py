from itertools import zip_longest


def transpose(char_matrix):
    char_rows = tuple(char_matrix.split('\n'))
    trans_rows = zip_longest(*char_rows, fillvalue=' ')
    return '\n'.join(''.join(row) for row in trans_rows).strip()
