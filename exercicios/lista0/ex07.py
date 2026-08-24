n1 = int(input("Informe um número inteiro: "))
n2 = int(input("Informe um número inteiro: "))

a =  n1
b = n2

while b != 0:
    resto = a % b
    a = b
    b = resto

print(f"MDC({n1}, {n2}): {a}")