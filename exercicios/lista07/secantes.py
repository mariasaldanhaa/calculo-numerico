import sympy as sy
import pandas as pd


def secantes(fx_, intervalo, epsilon, n):
    x = list(fx_.free_symbols)[0]
    f = sy.lambdify(x, fx_)

    x_anterior = intervalo[0]
    x_atual = intervalo[1]

    resultados = []

    for k in range(1, n + 1):
        f_anterior = f(x_anterior)
        f_atual = f(x_atual)

        x_novo = x_atual - f_atual * (x_atual - x_anterior) / (f_atual - f_anterior)
        erro = abs(x_novo - x_atual) / max(abs(x_novo), 1)

        resultados.append([k, x_novo, x_atual, f(x_novo), f_atual, erro])

        if f(x_novo) == 0 or erro < epsilon:
            break

        x_anterior = x_atual
        x_atual = x_novo

    iteracoes = pd.DataFrame(
        resultados,
        columns=['Iteração', 'x', 'x anterior', 'f(x)', 'f(x anterior)', 'Erro']
    )

    return x_novo, iteracoes
