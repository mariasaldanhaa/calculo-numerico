import sympy as sy
import pandas as pd

def newton_raphson(fx_, intervalo, TOL, n):
    x = sy.Symbol('x')
    flx_ = sy.diff(fx_, x)

    f = sy.lambdify(x, fx_)
    fl = sy.lambdify(x, flx_)

    a, b = intervalo
    x = (a + b) / 2
    x_anterior = float('nan')

    dados = []

    for k in range(1, n + 1):
        if k == 1:
            epsilon = float('nan')
        else:
            epsilon = abs(x - x_anterior) / max(abs(x), 1)

        dados.append([k, x, f(x), epsilon])

        if f(x) == 0 or (k > 1 and epsilon < TOL):
            break

        x_anterior = x
        x = x - f(x) / fl(x)

    iteracoes = pd.DataFrame(
        dados, columns=['k', 'x', 'f(x)', 'epsilon']
    )

    return x, iteracoes