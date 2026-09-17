def fatorial(num):
    if num <= 1:
        return 1
    else:
        return num * fatorial(num - 1)

n = int(input('Informe um número: '))
print('O fatorial de', n, 'é', fatorial(n))