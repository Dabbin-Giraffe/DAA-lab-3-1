import time
import matplotlib.pyplot as plt
import numpy as np

sizes = [2, 4, 8, 16, 32,64,128,256,512,1024]
# sizes = [2, 4, 8, 16]

def matrix_generator(param: int) -> list:
        matrix = np.random.randint(0,100, size=(param, param))
        return matrix


class Matrix_normal:

    size: int
    matrix1: np.array
    matrix2: np.array

    def __init__(self, size,matrix1,matrix2) -> None:
        self.size = size
        self.matrix1 = matrix1
        self.matrix2 = matrix2

    def matrix_generator(self, param: int) -> list:
        matrix = np.random.randint(100, size=(param, param))
        return matrix

    def multiply(self) -> np.array:
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
    matrix1: np.array
    matrix2: np.array

    def __init__(self, size,matrix1,matrix2) -> None:
        self.size = size
        self.matrix1 = matrix1
        self.matrix2 = matrix2

    def split(self,matrix: np.array) -> tuple:
        size2 = matrix.shape[0]//2
        return matrix[:size2, :size2], matrix[:size2, size2:], matrix[size2:, :size2], matrix[size2:, size2:]


    def strassen(self,x, y):

        arr_len = x.shape[0]

        if arr_len <= 2:
            return np.dot(x, y)

        a, b, c, d = self.split(x)
        e, f, g, h = self.split(y)

        a1 = self.strassen(a, f-h)
        a2 = self.strassen(a+b, h)
        a3 = self.strassen(c+d, e)
        a4 = self.strassen(d, g-e)
        a5 = self.strassen(a+d, e+h)
        a6 = self.strassen(b-d, g+h)
        a7 = self.strassen(a-c, e+f)

        c11 = a5+a4-a2+a6
        c12 = a1+a2
        c21 = a3+a5
        c22 = a1+a5-a3-a7

        final = np.vstack((np.hstack((c11, c12)), np.hstack((c21, c22))))

        return final
    
    def time_it(self):
        start = time.perf_counter()
        self.strassen(self.matrix1, self.matrix2)
        end = time.perf_counter()
        return end-start


time_normal = {}
time_strassen = {}

for i in sizes:

    matrix1,matrix2 = matrix_generator(i),matrix_generator(i)


    normal = Matrix_normal(i,matrix1,matrix2)
    time_normal[i] = normal.time_it()
    
    strassen = Matrix_strassen(i,matrix1,matrix2)
    time_strassen[i] = strassen.time_it()


print(f"Naive method : {time_normal}")    
print(f"strassen method : {time_strassen}")    

plt.plot(time_normal.keys(),time_normal.values(),"blue",label="Naive method")
plt.xlabel("Size of Matrices")
plt.ylabel("Time taken for multiplication in seconds")
plt.plot(time_strassen.keys(),time_strassen.values(),"green",label = "Strassen method")
plt.title("Time taken for matrix Multiplication for different algorithms")
plt.legend()
plt.show()

