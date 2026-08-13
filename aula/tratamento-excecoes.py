# exemplo de tratamneto de excecoes

while True:
    try:
        quant = int(input('Informe  quantidade de números: '))
        break
    except:
        print('Número inválido! Tente novamente.')

soma = 0
for cont in range(quant):
    while True:
        try:
            n = float(input('Informe um número: '))
            soma = soma + n
            break
        except:
            print('Número inválido! Tente novamenete.')

print('A média é ', soma / quant) 