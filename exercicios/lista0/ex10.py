import itertools

numeros = int(input("Digite a quantidade de elementos: "))

while numeros < 0:
    numeros = int(input("Digite a quantidade de elementos: "))

if numeros >= 0 and numeros <= 2:
    print("Não existe combinações formando grupos de 3 números.")
else:
    A = list(range(1, numeros + 1))
    combinacoes = list(itertools.combinations(A, 3))

    for cont in combinacoes:
        print(cont)