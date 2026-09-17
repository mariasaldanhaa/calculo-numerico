# exemplo com lista

soma = 0
lista_precos = []
print('Informe o preço dos produtos')
for cont in range(10):
    mensagem = 'Produto ' + str(cont + 1) + ': '
    preco = float(input(mensagem))
    soma = soma + preco
    lista_precos.append(preco) # adiciona x no final da lista
media = soma / 10
print('A média de preço é {m:.2f}'.format(m=media))
print('Os produtos com preço acima da média são:')
for cont in range(10):
    if lista_precos[cont] > media:
        print('Produto', cont + 1, ', preço: ', lista_precos[cont])