#!/usr/bin/env python
from string import ascii_uppercase as abcs


def make_diamond(letter):
    abcs_enum = {v : k for k, v in enumerate(abcs)}
    line_length = 2*abcs_enum[letter] + 1
    letter_spaces = (line_length//2+1, line_length//2-1)
    lines = []
    for line_number in range(abcs_enum[letter]+1):
        line_letter = abcs[line_number]
        letter_spaces = (letter_spaces[0]-1, letter_spaces[1]+1)
        line = ''
        for sp in range(line_length):
            line += line_letter if sp in letter_spaces else ' '
        lines.append(line)
    return '\n'.join(lines + lines[:-1][::-1]) + '\n'
