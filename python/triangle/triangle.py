#!/usr/bin/env python

class TriangleError(Exception):
    pass

class Triangle(object):
    @classmethod
    def verify_valid_length(cls, *args):
        for s in args:
            if not (isinstance(s, (int, float)) and s > 0):
                raise TriangleError('Invalid length: {}'.format(s))
        return args
    @classmethod
    def satisfies_triangle_inequality(cls, x, y, z):
        x, y, z = sorted(Triangle.verify_valid_length(x, y, z))
        return z <= x + y
    @classmethod
    def is_nondegenerate(cls, x, y, z):
        x, y, z = sorted(Triangle.verify_valid_length(x, y, z))
        return z != x + y
    @classmethod
    def verify_valid_triangle(cls, x, y, z):
        if not Triangle.is_nondegenerate(x, y, z):
            raise TriangleError('Non-degenerate triangle')
        if not Triangle.satisfies_triangle_inequality(x, y, z):
            raise TriangleError('Does not satisfy triangle inequality')
    def __init__(self, x, y, z):
        self.x, self.y, self.z = Triangle.verify_valid_length(x, y, z)
        Triangle.verify_valid_triangle(self.x, self.y, self.z)
    def __str__(self):
        return '({0}, {1}, {2})'.format(self.x, self.y, self.z)
    @property
    def x(self):
        return self._x
    @x.setter
    def x(self, val):
        self._x = Triangle.verify_valid_length(val)[0]
    @property
    def y(self):
        return self._y
    @y.setter
    def y(self, val):
        self._y = Triangle.verify_valid_length(val)[0]
    @property
    def z(self):
        return self._z
    @z.setter
    def z(self, val):
        self._z = Triangle.verify_valid_length(val)[0]
    def kind(self):
        x, y, z = sorted([self.x, self.y, self.z])
        if x == y == z:
            return 'equilateral'
        elif x == y or y == z:
            return 'isosceles'
        else:
            return 'scalene'
