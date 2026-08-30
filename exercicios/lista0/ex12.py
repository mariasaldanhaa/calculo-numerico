import random

n = int(input('Informe o número total de elementos: '))
sorteados = int(input('Informe o  número de elementos que devem ser sorteados: '))

lista = list(range(1, n + 1))
print(f"\nLista original: {lista}")

random.shuffle(lista)

sorteio = lista[:sorteados]

print(f"Elementos sorteados: {sorteio}")