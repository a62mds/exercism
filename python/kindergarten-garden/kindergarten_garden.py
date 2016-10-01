
class StudentListException(Exception):
    pass

class Garden(object):

    def __init__(self, layout, **kwarg):
        if kwarg:
            try:
                self._names = sorted(kwarg['students'])
            except:
                raise StudentListException('kwarg students not provided')
        else:
            self._names = ['Alice',
                           'Bob',
                           'Charlie',
                           'David',
                           'Eve',
                           'Fred',
                           'Ginny',
                           'Harriet',
                           'Ileana',
                           'Joseph',
                           'Kincaid',
                           'Larry']
        self._plants = ['Grass', 'Clover', 'Radishes', 'Violets']
        self._plant_key = {p[0] : p for p in self._plants}
        self._slot = {name : 2*self._names.index(name) for name in self._names}
        self.rows = layout.split('\n')

    def plants(self, name):
        plant_code = ''.join(c for row in self.rows
                             for c in row[self._slot[name] : self._slot[name]+2])
        return [self._plant_key[c] for c in plant_code]
