#!/usr/bin/env python
from random import choice
from string import ascii_uppercase as ltrs
from string import digits as dgts

class Robot(object):

    _name_db = []

    def __init__(self):
        self._name = self.gen_name()
        Robot._name_db.append(self._name)

    def pick(self, n, seq):
        return [choice(seq) for _ in range(n)]

    def gen_name(self):
        num_ltrs = 2
        num_dgts = 3
        name = ''.join(self.pick(num_ltrs, ltrs) + self.pick(num_dgts, dgts))
        return name if name not in Robot._name_db else self.gen_name()

    def reset(self):
        tmp_name, self._name = self._name, self.gen_name()
        Robot._name_db.remove(tmp_name)

    @property
    def name(self):
        return self._name
