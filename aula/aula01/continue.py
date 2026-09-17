# exemplo de instrucao continue

s = 0
for c in range(10):
    n = float(input('Informe um número: '))
    if n < 0:
        continue
    s = s + n
print('Soma dos números: ', s)
