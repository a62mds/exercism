#!/usr/bin/env python

NORTH = 0
WEST  = 1
SOUTH = 2
EAST  = 3

class Robot(object):

    def __init__(self, brng=None, x=None, y=None):
        self.dirs = [NORTH, WEST, SOUTH, EAST]
        self.bearing = NORTH if brng is None else self.verify_is_dir(brng)
        self.x = 0 if x is None else self.verify_is_coord(x)
        self.y = 0 if y is None else self.verify_is_coord(y)

    def verify_is_dir(self, input):
        if input in self.dirs:
            return input
        else:
            raise Exception('Invalid direction')

    def verify_is_coord(self, input):
        if isinstance(input, (int, long)):
            return input
        else:
            raise Exception('Coordinates must be integers')

    def turn_left(self):
        self.bearing = (self.bearing + 1) % len(self.dirs)

    def turn_right(self):
        self.bearing = (self.bearing - 1) % len(self.dirs)

    def advance(self):
        up    = lambda x, y: (x, y+1)
        left  = lambda x, y: (x-1, y)
        down  = lambda x, y: (x, y-1)
        right = lambda x, y: (x+1, y)
        move = {NORTH : up, WEST : left, SOUTH : down, EAST : right}
        self.x, self.y = move[self.bearing](self.x, self.y)

    def simulate(self, cmds):
        obey = {'L' : self.turn_left, 'R' : self.turn_right, 'A' : self.advance}
        for cmd in cmds:
            obey[cmd]()

    @property
    def coordinates(self):
        return (self.x, self.y)
