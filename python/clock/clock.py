#!/usr/bin/env python


class Clock:

    # Private member variable that stores all existing clock objects
    _instances = []

    # If clock object with same time already exists, do not instantiate
    # new clock object; return existing
    def __new__(cls, hr, mn):
        for ins in _instances:
            if cls.instance == ins:
                return ins
        return cls.instance

    # Initialize clock object with properly formatted hours and minutes
    def __init__(self, hr, mn):
        self.hr = (hr + (mn // 60)) % 24
        self.mn = mn % 60

    # Define equality of two clock objects
    def __eq__(self, other):
        return self.hr == other.hr and self.mn == other.mn

    # Define how clock object is converted to a string
    def __str__(self):
        return "{0:02d}:{1:02d}".format(self.hr, self.mn)

    # Add two clock objects
    def add(self, mins):
        return Clock(self.hr, self.mn + mins)
