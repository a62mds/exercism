

class Matrix(object):

    def __init__(self, defn):
        self.rows = [map(int, row.split()) for row in defn.split('\n')]
        self.ncols = len(self.rows[0])
        if not all(len(row) == self.ncols for row in self.rows):
            raise ValueError('Rows not all same length')
        self.columns = [[row[col] for row in self.rows] for col in range(self.ncols)]
