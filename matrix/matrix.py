class Matrix(object):
    def __init__(self, matrix_string):
        matrix_rows_string = (matrix_string.splitlines())
        self.matrix = [list(map(int, row.split())) for row in matrix_rows_string]

    def row(self, index):
        return self.matrix[index-1]

    def column(self, index):
        return [row[index-1] for row in self.matrix]
