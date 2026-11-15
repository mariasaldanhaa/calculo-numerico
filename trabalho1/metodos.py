import numpy as np
import pandas as pd

cenarios = {
    "base": {"a": 0.3, "tr": 25, "cm": 1.3e-5, "D": 1000},
    "freio fraco": {"a": 0.15, "tr": 25, "cm": 1.3e-5, "D": 1000},
    "ecp": {"a": 0.3, "tr": 5, "cm": 1.3e-5, "D": 1000}
}

def f(v, a, tr, cm, D):
    return v * tr + (1 / (2 * cm)) * np.log1p(cm * v ** 2 / a) - D

def f_(v, a, tr, cm, D):
    return tr + v / (a + cm * v ** 2)

def newtonRaphson(v_min, v_max, TOL, n, a, tr, cm, D):
    historico = []
    x = (v_min + v_max) / 2
    x_ = float('nan')

    for k in range(1, n + 1):
        erro = abs((x - x_) / (max(x, 1)))

        historico.append({
            "k": k, "x": x, "f(x)": f(x, a, tr, cm, D), "erro": erro,
        })

        if (f(x, a, tr, cm, D) == 0 or erro < TOL):
            break

        x_ = x
        x = x - (f(x, a, tr, cm, D) / f_(x, a, tr, cm, D))

    df = pd.DataFrame(historico)
    print(df)
    return x

def secante(v_min, v_max, TOL, n, a, tr, cm, D):
    historico = []
    x_ = v_min
    x__ = v_max

    for k in range(1, n + 1):
        x = x_ - f(x_, a, tr, cm, D) * ((x_ - x__) / (f(x_, a, tr, cm, D) - f(x__, a, tr, cm, D)))
        erro = abs((x - x_) / (max(x, 1)))

        historico.append({
            "k": k, "x": x, "f(x)": f(x, a, tr, cm, D), "erro": erro
        })

        if (f(x, a, tr, cm, D) == 0 or erro < TOL):
            break

        x__ = x_
        x_ = x

    df = pd.DataFrame(historico)
    print(df)
    return x

def posicaoFalsa(a, b, TOL, n, a_f, tr, cm, D):
    historico = []
    x_ = float('nan')

    for k in range(1, n + 1):
        x = (a * f(b, a_f, tr, cm, D) - b * f(a, a_f, tr, cm, D)) / (f(b, a_f, tr, cm, D) - f(a, a_f, tr, cm, D))
        erro = abs((x - x_) / (max(x, 1)))
        x_ = x

        historico.append({
            "k": k, "a": a, "b": b, "erro": erro, "x": x, "f(x)": f(x, a_f, tr, cm, D),
            "f(x) x f(a)": f(x, a_f, tr, cm, D) * f(a, a_f, tr, cm, D)
        })

        if (f(x, a_f, tr, cm, D) == 0 or erro < TOL):
            break

        if (f(x, a_f, tr, cm, D) * f(a, a_f, tr, cm, D) > 0):
            a = x
        else:
            b = x
    df = pd.DataFrame(historico)
    print(df)
    return x