# lista inicializada com numeros de 0 a 9
lista = [n for n in range(9)]
print(lista)

# leitura de string e com split

texto = input('Informe uma lista de números (separado com espaços): ')
lista = [int(x) for x in texto.split()]
print(lista)
print(len(lista))

# Lista com números de 1 a 10
lista = list(range(1, 11))
# Último elemento
print(lista[-1])
# Segundo ao terceiro elemento
print(lista[1:3])
 # Até o quinto elemento
print(lista[:5])
# Do terceiro elemento até o final
print(lista[2:])

# copia e o operador in

# Lista com números de 1 a 10
lista = list(range(1, 11))
# Copia do sexto ao último elemento
lista2 = lista[5:]
print(lista2)
# Copia a lista completa
lista2 = lista[:]
print(lista2)
# Testa se 5 está na lista
print(5 in lista)
# Testa se 20 está na lista
print(20 in lista)