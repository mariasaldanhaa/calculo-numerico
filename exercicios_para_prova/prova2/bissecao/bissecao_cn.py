import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# metodo da bissecao - usado para encontrar a raiz real de uma funcao
# Para avaliar a precisao:
# e = 10^-2
# I) |x - r| < e
# II) |f(x)| < e

# Fazer (I) sem conhecer r:
# |b-a| < e
# |x-r| < |b-a| < e

# -- algoritmo --
# se b-a < e, escolhe qualquer x pertencente a [a, b].
# se b-a >= e, seja m = a+b/2.
# se f(a) f(m) < 0, troque b por m. Se f(m) f(b) < 0, 
# troque a por m.
# volte para o passo 2

# a = ponto inicial do intervalo
# b = ponto final do intervalo
# m = ponto médio

# exemplo 1:
# f(x) = x^3 - 3x + 1 tem uma unica raiz em (0, 1). Calcule-a
# com precisao e = 10^-1

# exemplo 2: f(x) = x ln x - 2 tem uma unica raiz em (2, 3). Calcule-a com precisao
# e = 10^-1

def grafico(a, b, f):
    x = np.linspace(a, b, 100)
    y = f(x)
    plt.plot(x, y)
    plt.show()

def bissecao(a, b, epsilon, f):
    historico = []

    iteracoes = int(np.ceil((np.log10(b - a) - np.log10(epsilon)) / np.log10(2)))
    ponto_medio = (a + b) / 2
    f_a, f_b, f_m = f(a), f(b), f(ponto_medio)

    historico.append({
        "Iteração": 1, "a": a, "b": b, "m": ponto_medio, "f(a)": f_a, 
        "f(b)": f_b, "f(m)": f_m, "b - a": b - a
    })

    for cont in range(2, iteracoes + 1):
        if (np.multiply(f_a, f_m) < 0):
            b = ponto_medio

        elif (np.multiply(f_m, f_b) < 0):
            a = ponto_medio

        ponto_medio = (a + b) / 2
        f_a, f_b, f_m = f(a), f(b), f(ponto_medio)

        historico.append({
            "Iteração": cont, "a": a, "b": b, "m": ponto_medio, "f(a)": f_a, 
            "f(b)": f_b, "f(m)": f_m, "b - a": b - a
        })

    df = pd.DataFrame(historico)

    return df