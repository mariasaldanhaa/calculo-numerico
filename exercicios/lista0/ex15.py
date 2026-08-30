# corrigido em sala

print('--- Ordenação de lista ---')

entrada = input('Digite uma lista de caracteres: ')
lista = list(entrada)

passagem = 1
n = len(lista)

while True:
    print(f"\nPassagem {passagem}")
    print(f"Estado inicial: {lista}")

    troca = False

    for i in range(n - passagem):
        if lista[i] > lista[i + 1]:
            aux = lista[i]
            lista[i] = lista[i + 1]
            lista[i + 1] = aux
            troca = True
            print('   Troca: ', lista)
    if not troca:
        break
    passagem += 1

print('Lista ordenada: ', lista)