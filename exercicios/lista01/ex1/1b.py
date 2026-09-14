n = "126.485"

def converterBase(n, base):
    partes = n.split(".")
    
    inteira = int(partes[0])
    decimal = float("0." + partes[1])
    
    listaInteiro = []
    listaDecimal = []
    
    simbolos = "0123456789ABCDEF"
    
    while inteira > 0:
        resto = inteira % base
        algarismo = simbolos[resto]
        listaInteiro.insert(0, algarismo)
        inteira = inteira // base
    
    for i in range(8):
        decimal = decimal * base
        algarismo = int(decimal)
        listaDecimal.append(simbolos[algarismo])
        decimal = decimal - algarismo
    
    resultadoInteiro = "".join(map(str, listaInteiro))
    resultadoDecimal = "".join(map(str, listaDecimal))

    resultado = resultadoInteiro + "." + resultadoDecimal
    
    return resultado

print(f"{n} em binário: {converterBase(n, 2)}")
print(f"{n} em quaternário: {converterBase(n, 4)}")
print(f"{n} em octal: {converterBase(n, 8)}")
print(f"{n} em hexadecimal: {converterBase(n, 16)}")

# resultado
# 126.485 em binário: 1111110.01111100
# 126.485 em quaternário: 1332.13300220
# 126.485 em octal: 176.37024365
# 126.485 em hexadecimal: 7E.7C28F5C2