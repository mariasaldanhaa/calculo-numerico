import random

lista = [random.randint(1, 10) for espaco in range(100)]

contagens = [lista.count(num) for num in range(1, 11)]

print("-- RESULTADO --")
for i, quantidade in enumerate(contagens, start=1):
    print(f"O número {i} apareceu {quantidade} vezes.")