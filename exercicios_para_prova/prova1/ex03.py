lista = []
soma = 0

for i in range(10):
    numeros = int(input(f"Informe um número inteiro {i}: "))
    lista.append(numeros)
    
    soma += numeros

media = soma / 10
print(f"Média dos valores: {media:.2f}")

for j in range(10):
    if lista[j] > media:
        print(f"Acima da média: {lista[j]}")