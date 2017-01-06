#!/usr/bin/env python

def is_list(ll):
    return type(ll) is list

def is_maximal(element, lst):
    return all(element >= other for other in lst)

def is_minimal(element, lst):
    return all(element <= other for other in lst)

def saddle_points(matrix):
    # Validate the input matrix
    if not is_list(matrix) and all(is_list(row) for row in matrix):
        raise ValueError('matrix must be a list of lists')
    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise ValueError('matrix rows must be the same length')
    # Build list of saddle points
    saddle_pts = []
    for ii in range(len(matrix)):
        row = matrix[ii]
        for jj in range(len(row)):
            col = [rr[jj] for rr in matrix]
            el = row[jj]
            if is_maximal(el, row) and is_minimal(el, col):
                saddle_pts.append((ii, jj))
    return set(saddle_pts)
