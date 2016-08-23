#!/usr/bin/env python

def to_rna(dna):
    transcriber = {'G':'C', 'C':'G', 'T':'A', 'A':'U'}
    return ''.join([transcriber[n] for n in dna])