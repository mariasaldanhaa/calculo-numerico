a = int(input("Informe um número inteiro: "))
b = int(input("Informe um número inteiro: "))
c = int(input("Informe um número inteiro: "))

delta = b**2 - 4 * a * c

print(f"O valor de delta é: {delta}.")

if (delta > 0): 
    print("A equação possui duas raízes.")
elif (delta == 0): 
    print("A equação possui uma raiz.")
else:
    print("A equação não possui raízes.")