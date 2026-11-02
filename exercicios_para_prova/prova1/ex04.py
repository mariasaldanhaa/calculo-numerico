import math

def fatorial(numero):
    resultado = math.factorial(numero)
    return resultado

def main():
    numero = int(input("Digite um número inteiro: "))
    resultado = fatorial(numero)
    print(resultado)
    
main()