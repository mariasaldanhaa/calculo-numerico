import numpy as np

def linha_pivo(M, c):
    m = abs(M[c, c])
    lp = c
    n = len(M)

    for la in range(c, n):
        if (abs(M[la, c]) > m):
            m = abs(M[la, c])
            lp = la

    return lp

def troca_linhas(M, l, l_):
    if l != l_:
        aux = np.copy(M[l])
        M[l] = M[l_]
        M[l_] = aux
        print(f'\nL{l + 1} <-> L{l_ + 1}')
        print(M)

def zeros_diag(M):
    n = len(M)

    for k in range(n):
        if (abs(M[k, k]) == 0):
            return True

    return False

def gauss_pivo(E):
    n = len(E)

    for c in range(n - 1):
        print(f'\nColuna  {c + 1} :')
        lp = linha_pivo(E, c)
        troca_linhas(E, lp, c)
        p = E[c, c]

        for l in range(c + 1, n):
            print(f'\nL{l + 1} <- L{l + 1} - {E[l, c]} / {p} * L{c + 1}')
            E[l] = E[l] - E[l, c] / p * E[c]
            print(E)

def resolve_diag_sup(A, b):
    n = len(A)
    x = np.zeros(n)
    x[n - 1] = b[n - 1] / A[n - 1, n - 1]

    for l in range(n - 2, -1, -1):
        s = 0

        for c in range(l + 1, n):
            s = s + x[c] * A[l, c]

        x[l] = (b[l] - s) / A[l, l]

    return x

def resolve_diag_inf(A, b):
    n = len(A)
    y = np.zeros(n)
    y[0] = b[0] / A[0, 0]

    for l in range(1, n):
        s = 0

        for c in range(l):
            s = s + y[c] * A[l, c]

        y[l] = (b[l] - s) / A[l, l]

    return y

def fatora_lu(A):
    U = np.array(A, dtype=float)
    n = len(U)
    L = np.identity(n)

    for c in range(n - 1):
        # pivo zero, nao da pra dividir
        if U[c, c] == 0:
            print('Matriz U com zeros na diagonal principal')
            print('Não é possível executar a fatoração')
            return None, None

        for l in range(c + 1, n):
            L[l, c] = U[l, c] / U[c, c]

            for k in range(c, n):
                U[l, k] = U[l, k] - L[l, c] * U[c, k]

    # o ultimo pivo tambem pode ser zero
    if zeros_diag(U):
        print('Matriz U com zeros na diagonal principal')
        print('Não é possível executar a fatoração')
        return None, None

    return L, U

def titulo(txt):
    print('-' * 50)
    print(txt)
    print('-' * 50)

def resolve(mat):
    E = np.array(mat, dtype=float)
    n = len(E)

    titulo('Matriz estendida')
    print(mat)

    titulo('Escalonamento')
    gauss_pivo(E)

    if zeros_diag(E):
        print('\nZeros na diagonal principal: o sistema não possui solução')
        return

    titulo('Solução')
    print(resolve_diag_sup(E[:, :n], E[:, n]))

    A = np.array(mat, dtype=float)[:, :n]
    b = np.array(mat, dtype=float)[:, n]

    titulo('Normas (1, 2, inf)')
    print(np.linalg.norm(A, 1), np.linalg.norm(A, 2), np.linalg.norm(A, np.inf))

    titulo('Condicionamento (1, 2, inf)')
    print(np.linalg.cond(A, 1), np.linalg.cond(A, 2), np.linalg.cond(A, np.inf))

    titulo('Fatoração LU')
    L, U = fatora_lu(A)
    if L is not None:
        y = resolve_diag_inf(L, b)
        print(L)
        print(U)
        print(resolve_diag_sup(U, y))