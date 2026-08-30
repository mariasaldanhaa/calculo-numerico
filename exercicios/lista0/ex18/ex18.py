import mat

print('--- Teste de funções ---')

num = int(input('Digite um número inteiro: '))

if mat.impar(num):
    print('O número é ímpar.')
else:
    print('O número é par.')

raio = float(input('\nDigite o raio do círculo: '))

print(f'A área do círculo é: {mat.area_circulo(raio):.2f}')