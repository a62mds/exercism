#!/usr/bin/env python

class Allergies(object):

    def __init__(self, score):
        self.alrgs = {'eggs' : 0, 
                      'peanuts' : 1,
                      'shellfish' : 2,
                      'strawberries' : 3,
                      'tomatoes' : 4,
                      'chocolate' : 5,
                      'pollen' : 6,
                      'cats' : 7}
        self.score = score % (2**len(self.alrgs))

    @property
    def binary_score(self):
        bin_score = map(int, list(format(self.score, 'b')))
        return [0] * (len(self.alrgs) - len(bin_score)) + bin_score

    @property
    def lst(self):
        return [a for a in self.alrgs 
                if self.binary_score[len(self.alrgs)-1 - self.alrgs[a]]]

    def is_allergic_to(self, candidate):
        return candidate in self.lst        
