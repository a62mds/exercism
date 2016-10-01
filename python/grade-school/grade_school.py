class School(object):

    def __init__(self, name):
        self.name = name
        self.grades = range(1, 9)
        self.roster = {grade : tuple() for grade in self.grades}

    def add(self, student, grade):
        self.roster[grade] = self.roster[grade] + (student,)

    def grade(self, gr):
        return self.roster[gr]

    def sort(self):
        sort_names = lambda d: map(lambda k: (k, tuple(sorted(d[k]))), d)
        grade_not_empty = lambda (n, g): True if g else False
        return filter(grade_not_empty, sort_names(self.roster))
