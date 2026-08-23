numeros = []

print("Digite os números que desejar. Para encerrar, digite '0'.")

while True:
    numero = int(input("Informe um número inteiro: "))

    if numero == 0:
        break

    numeros.append(numero)


if len(numeros) > 0:
    maiorNota = max(numeros)
    menorNota = min(numeros)

    print(f"Números: {numeros}")
    print(f"Maior nota: {maiorNota}")
    print(f"Menor nota: {menorNota}")
else:
    print("Nenhum número foi digitado!")