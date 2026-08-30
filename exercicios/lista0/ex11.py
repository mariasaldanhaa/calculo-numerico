import itertools

n = int(input('Informe um número inteiro: '))

A = list(range(1, n + 1))

combinacoes = list(itertools.combinations(A, 3))

for grupo in combinacoes:
    print(set(grupo))