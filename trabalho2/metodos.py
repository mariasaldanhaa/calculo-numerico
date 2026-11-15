import numpy as np

def jacobi(A, b, x0, tol, n):
    d = len(A)
    x = np.copy(x0)
    xant = np.copy(x0)
    for k in range(n):
        for i in range(d):
            x[i] = b[i]
            for j in range(d):
                if j != i:
                    x[i] = x[i] - A[i, j] * xant[j]
            x[i] = x[i] / A[i, i]
        erro = np.max(np.abs(x - xant))
        if erro < tol:
            break
        xant = np.copy(x)
    return x, k + 1, erro 

def gauss_seidel(A, b, x0, tol, n):
    d = len(A)
    x, x_ = np.copy(x0), np.copy(x0)
    for k in range(n):
        for i in range(d):
            x[i] = b[i]
            for j in range(i):
                x[i] = x[i] - A[i][j] * x[j]
            for j in range(i + 1, d):
                x[i] = x[i] - A[i][j] * x_[j]
            x[i] = x[i] / A[i, i]
        erro = np.max(np.abs(x - x_))
        if erro < tol:
            break
        x_ = np.copy(x)
    return x, k + 1, erro