numeros = []

while True:
    numero = float(input("Informe um número: "))
    
    numeros.append(numero)
    
    resposta = input("Deseja continuar? (s/n): ")
    
    if resposta.lower() == 'n':
        break

print(f"Maior número: {max(numeros)}")
print(f"Menor número: {min(numeros)}")