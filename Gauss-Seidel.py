import numpy as np
from scipy.linalg import solve

def gauss(A, b, x, n):

    L = np.tril(A)
    U = A - L
    for i in range(n):
        x = np.dot(np.linalg.inv(L), b - np.dot(U, x))
        print (str(i).zfill(3))
        print(x)
    return x

A = np.array([[-1., -2., 0.], [0., 2.0, -5.0], [1., 1., 1.0]])
b = [1., 0., 50.]
x = [1, 1, 1]

# 20 iteraciones
n = 50

print (gauss(A, b, x, n))
print (solve(A, b))
