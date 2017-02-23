#!/usr/bin/env python

_first_words = 'This is '

_verse = [('that lay in ',      'the house that Jack built'),
          ('that ate ',         'the malt'),
          ('that killed ' ,     'the rat'),
          ('that worried ',     'the cat'),
          ('that tossed ',      'the dog'),
          ('that milked ',      'the cow with the crumpled horn'),
          ('that kissed ',      'the maiden all forlorn'),
          ('that married ',     'the man all tattered and torn'),
          ('that woke ',        'the priest all shaven and shorn'),
          ('that kept ',        'the rooster that crowed in the morn'),
          ('that belonged to ', 'the farmer sowing his corn'),
          ('',                  'the horse and the hound and the horn')]

def rhyme():
    rym = ''
    for v in range(len(_verse)):
        rym += verse(v) + ('' if v == len(_verse)-1 else '\n\n')
    return rym

def verse(n):
    if n > len(_verse) or 0 > n:
        raise ValueError('Invalid verse number')
    def line_ending(v):
        return '.' if v == 0 else '\n'
    vrs = _first_words + _verse[n][1] + line_ending(n)
    for v in range(n-1, -1, -1):
        vrs += _verse[v][0] + _verse[v][1] + line_ending(v)
    return vrs
