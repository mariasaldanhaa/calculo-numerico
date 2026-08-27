import mat

print('Teste de funções')

num = int(input('Digite um número inteiro: '))

if mat.impar(num):
    print('O número é ímpar.')
else:
    print('O número é par.')

print('A área do círculo é: ', mat.area_circulo)