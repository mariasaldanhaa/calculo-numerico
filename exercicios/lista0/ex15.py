# corrigido em sala

print('--- Ordenação de lista ---')

lista = input('Digite uma lista de caracteres: ')
lista = list(lista)
passagem = 1

while True:
    print('Passagem ', passagem)
    print(lista)

    troca = False

    for i in range(len(lista) - 1):
        if lista[i] > lista[i + 1]:
            aux = lista[i]
            lista[i] = lista[i + 1]
            lista[i + 1] = aux
            troca = True
            print('   Troca: ', lista)
        if troca:
            break
        passagem += 1

print('Lista ordenada: ', lista)