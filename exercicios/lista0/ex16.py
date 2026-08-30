#  corrigido em sala

lista = input('Digite uma lista de números separados por espaços: ')
lista = [int(num) for num in lista.split()]

lista_sr = []

for num in lista:
    existe = False

    for num_r in lista_sr:
        if num == num_r:
            existe = True
            break
    if not existe:
        lista_sr.append(num)

print('Lista sem repetições: ', lista_sr)