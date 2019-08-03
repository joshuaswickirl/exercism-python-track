class Matrix(object):
    def __init__(self, matrix_string):
        matrix_rows_string = (matrix_string.split('\n'))
        self.matrix = []
        for row in matrix_rows_string:
            self.matrix.append(list(map(int, row.split())))
        print(self.matrix)

    def row(self, index):
        return self.matrix[index-1]

    def column(self, index):
        column = []
        for row in self.matrix:
            column.append(row[index-1])
        return column
