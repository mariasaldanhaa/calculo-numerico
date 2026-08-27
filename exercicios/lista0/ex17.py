# corrigido em sala

def input_int(mensagem):
    while True:
        try:
            num = int(input(mensagem))
            return num
        except ValueError:
            print('Número inválido! Digite novamente.')

def input_float(mensagem):
    while True:
        try:
            num = float(input(mensagem))
            return num
        except ValueError:
            print('Número inválido! Digite novamente.')

print('Teste das funções: ')
num_int = input_int('Digite um número inteiro: ')
num_float = input_float('Digite um número inteiro: ')
print('Número inteiro digitado: ', num_int)
print('Número real digitado: ', num_float)