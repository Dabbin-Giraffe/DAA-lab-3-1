import time
import random as rd

sizes = [2, 4, 8, 16, 32, 64, 128, 256, 512]


class Matrix_normal:

    size: int
    matrix1: list
    matrix2: list

    def __init__(self, size) -> None:
        self.size = size
        self.matrix1 = self.matrix_generator(self.size)
        self.matrix2 = self.matrix_generator(self.size)

    def matrix_generator(self, size: int) -> list:

        matrix = [[rd.randint(1, 100) for i in range(size)]
                  for j in range(size)]

        return matrix

    def multiply(self) -> list:
        matrix1 = self.matrix1
        matrix2 = self.matrix2
        size = self.size

        c = [[0 for x in range(size)] for i in range(size)]
        for i in range(size):
            for j in range(size):
                for k in range(size):
                    c[i][j] += matrix1[i][k] + matrix2[k][j]

        return c

    def time_it(self):

        start = time.perf_counter()
        result = self.multiply()
        # print(result)
        end = time.perf_counter()
        return float(end-start)


class Matrix_strassen:

    size: int
    matrix1: list
    matrix2: list

    def __init__(self, size) -> None:
        self.size = size
        self.matrix1 = self.matrix_generator(self.size)
        self.matrix2 = self.matrix_generator(self.size)

    def matrix_generator(self, size: int) -> list:

        matrix = [[rd.randint(1, 100) for i in range(size)]
                  for j in range(size)]

        return matrix

    def split(self, matrix: list) -> list:
        size2 = len(matrix)
        return matrix[:size2][:size2], matrix[:size2][size2:], matrix[size2:][:size2], matrix[size2:][size2:]

    def add(self, mat1: list, mat2: list) -> list:

        size = len(mat1)
        result = [[mat1[i][j]+mat2[i][j]
                   for j in range(size)] for i in range(size)]

        return result

    def sub(self, mat1: list, mat2: list) -> list:

        size = len(mat1)
        result = [[mat1[i][j]-mat2[i][j]
                   for j in range(size)] for i in range(size)]

        return result

    def combine(self, c11, c12, c21, c22) -> list:
        size = len(c11)

        result = [[0 for _ in range(size*2)] for _ in range(size*2)]

        for i in range(size):
            for j in range(size):
                result[i][j] = c11[i][j]
                result[i][j + size] = c12[i][j]
                result[i + size][j] = c21[i][j]
                result[i + size][j + size] = c22[i][j]

        return result

    def strassen(self, x, y):
        if len(x) == 1:
            return x*y

        a, b, c, d = self.split(x)
        e, f, g, h = self.split(y)

        a1 = self.strassen(a, self.sub(f, h))
        a2 = self.strassen(self.add(a, b), h)
        a3 = self.strassen(self.add(c, d), e)
        a4 = self.strassen(d, self.sub(g, e))
        a5 = self.strassen(self.add(a, d), self.add(e, h))
        a6 = self.strassen(self.sub(b, d), self.add(g, h))
        a7 = self.strassen(self.sub(a, c), self, self.add(e, f))

        c11 = self.sub(self.add(self.add(a5, a4), a6), a2)
        c12 = self.add(a1, a2)
        c21 = self.add(a3, a4)
        c22 = self.sub(self.add(a1, a5), self.add(a3, a7))

        final = self.combine(c11, c12, c21, c22)

        return final

    def time_it(self):
        start = time.perf_counter()
        result = self.strassen(self.matrix1, self.matrix2)
        end = time.perf_counter()

        return end-start


time_normal = {}
time_strassen = {}

for i in sizes:

    normal = Matrix_normal(i)
    time_normal[i] = normal.time_it()
    
    strassen = Matrix_strassen(i)
    time_strassen[i] = strassen.time_it()
    


print(time_normal)
