import numpy as np
import time
import random

x = np.random.randint(0,10,(4,4))
y = np.random.randint(0,10,(4,4))

def split(matrix: np.array) -> tuple:
        size2 = matrix.shape[0]//2
        return matrix[:size2,:size2], matrix[:size2,size2:], matrix[size2:,:size2], matrix[size2:,size2:]


def strassen(x, y):
    
        arr_len = x.shape[0]
        
        if arr_len <= 2:
            return np.dot(x,y)

        a, b, c, d = split(x)
        e, f, g, h = split(y)

        a1 = strassen(a, f-h)
        a2 = strassen(a+b,h)
        a3 = strassen(c+d,e)
        a4 = strassen(d,g-e)
        a5 = strassen(a+d,e+h)
        a6 = strassen(b-d,g+h)
        a7 = strassen(a-c,e+f)

        c11 = a5+a4-a2+a6
        c12 = a1+a2
        c21 = a3+a5
        c22 = a1+a5-a3-a7

        final = np.vstack((np.hstack((c11,c12)),np.hstack((c21,c22))))

        return final

def time_it(x,y):
        start = time.perf_counter()
        strassen(x,y)
        end = time.perf_counter()

        return end-start


print(time_it(x,y))