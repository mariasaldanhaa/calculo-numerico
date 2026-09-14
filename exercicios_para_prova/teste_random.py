import random

numero = random.randint(1, 10)
print(numero)

frutas = ["maçã", "banana", "uva", "laranja"]

escolhida = random.choice(frutas)
print(escolhida)

numeros = [1, 2, 3, 4, 5]

random.shuffle(numeros)
print(numeros)

numero = random.random()
print(numero)

numero = random.uniform(5, 10)
print(numero)

numeros = [1, 2, 3, 4, 5]
escolhidos = random.sample(numeros, 3)
print(escolhidos)