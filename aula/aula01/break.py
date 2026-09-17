# exemplo de instrucao break

s = 0
while True:
    n = float(input('Informe um número: '))
    if n == 0:
        break
    s = s + n
print('Soma dos números: ', s)