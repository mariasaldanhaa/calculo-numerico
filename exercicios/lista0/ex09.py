import sys

print("--- CALCULADORA ---")
print("0 - SAIR" )
print("1 - SOMA" )
print("2 - MULTIPLICAÇÃO" )
print("3 - DIVISÃO" )
print("4 - SUBTRAÇÃO" )
print("5 - POTÊNCIA" )

opcao = int(input("Infome a sua escolha: "))

while opcao < 0 or opcao > 5:
    print("--- CALCULADORA ---")
    print("0 - SAIR" )
    print("1 - SOMA" )
    print("2 - MULTIPLICAÇÃO" )
    print("3 - DIVISÃO" )
    print("4 - SUBTRAÇÃO" )
    print("5 - POTÊNCIA" )
    print("Ops! Digite novamente.")
    opcao = int(input("Infome a sua escolha: "))


if opcao == 0:
    print("Saindo...")
    sys.exit()

n1 = int(input("Informe o primeiro número: "))
n2 = int(input("Informe o segundo número: "))

match opcao:
    case 1:
        resultado = n1 + n2
        print(f"RESULTADO: {resultado}")
    case 2:
        resultado = n1 * n2
        print(f"RESULTADO: {resultado}")
    case 3:
        resultado = n1 / n2
        print(f"RESULTADO: {resultado:.2f}")
    case 4:
        resultado = n1 - n2
        print(f"RESULTADO: {resultado}")
    case 5:
        resultado = n1 ** n2
        print(f"RESULTADO: {resultado}")