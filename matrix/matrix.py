def is_integer(num):
    try:
        val = int(num)
        return True
    except ValueError:
        return False

class Matrix:
    def __init__(self, rows, columns):
        assert rows and columns, "Invalid matrix, rows and columns must be provided" #debe ser usado para las precondiciones de todos los métodos
        self.rows = rows
        self.columns = columns
        self.values = []
        for i in range(rows):
            row = []
            for j in range(columns):
                row.append(0)
            self.values.append(row)
    
    def add(self, i, j, value): #falta validacion de los rangos
        self.values[i][j] = value

    def __mul__(self, value):
        assert is_integer(value), "Invalid value, integer must be provided"
        for row in range(self.rows):
            for column in range(self.columns):
                self.values[row][column] = self.values[row][column] * value
        return self
        
        
    def __str__(self):
        output = ''
        for row in self.values:
            for value in row:
                output += f'{value} '
            output += '\n'
        return output

    def __eq__(self, otherMatrix):
        return self.rows == otherMatrix.rows and self.columns == otherMatrix.columns

    def __contains__(self, value):
        for row in self.values:
            if value in row:
                return True
        return False

    def __iter__(self, item): #pendiente
        return True 
