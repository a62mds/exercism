#!/usr/bin/env python

from collections import deque


num_rails = 4
ciphertext = 'abcdefghijkl'
print('len(ciphertext) = {}'.format(len(ciphertext)))
index_delta = 2 * (num_rails - 1)
indices = range(len(ciphertext))

def deque_chunks(l, chunk_length):
    """
    Generator that splits a list l into chunks of length chunk_length,
    with each chunk returned as a deque
    """
    for ii in range(0, len(l), chunk_length):
        yield deque(l[ii : ii + chunk_length])

index_chunks = [deque(indices[ii:ii+index_delta]) for ii in indices[::index_delta]]
#index_chunks = deque_chunks(indices, index_delta)

print list(index_chunks)

def conditional_increment(x, exp):
    if x == exp:
        return x + 1
    else:
        return x

row_indices = [[chunk.popleft() for chunk in index_chunks]]
exp_len = index_delta - 2
for row in range(1, num_rails):
    row_indices.append([])
    removed = 0
    for chunk in index_chunks:
        if len(chunk) > 0:
            row_indices[row].append(chunk.popleft())
            removed = conditional_increment(removed, 0)
        if len(chunk) == exp_len and exp_len > 0:
            row_indices[row].append(chunk.pop())
            removed = conditional_increment(removed, 1)
    exp_len -= removed

print row_indices
print('Done.')
