n = "1010010.011"

def comecarPelaDireita(n, tamanho):
    partes = n.split(".")
    inteira = partes[0]
    resultadoInteiro = []
    
    if len(inteira) % 2 != 0:
        acrescentar = "0" + inteira
        
        for i in range(0, len(acrescentar), tamanho):
            resultadoInteiro.append(acrescentar[i:i + tamanho])

    else:
        for i in range(0, len(inteira), tamanho):
            resultadoInteiro.append(inteira[i:i + tamanho])

    return resultadoInteiro

def comecarPelaEsquerda(n, tamanho):
    partes = n.split(".")
    decimal = partes[1]
    resultadoDecimal = []
    
    if len(decimal) % 2 != 0:
        acrescentar = decimal + "0"
        
        for i in range(0, len(acrescentar), tamanho):
            resultadoDecimal.append(acrescentar[i:i + tamanho])
    
    else:
        for i in range(0, len(decimal), tamanho):
            resultadoDecimal.append(decimal[i:i + tamanho])
    
    return resultadoDecimal

def converterBase(n, base):
    if base == 4:
        tamanho = 2
    elif base == 8:
        tamanho = 3
    elif base == 16:
        tamanho = 4
    
    listaInteiro = [int(x, 2) for x in (comecarPelaDireita(n, tamanho))]
    resultadoInteiro = "".join(map(str, listaInteiro))
    
    listaDecimal = [int(x, 2) for x in (comecarPelaEsquerda(n, tamanho))]
    resultadoDecimal = "".join(map(str, listaDecimal))
    
    resultado = resultadoInteiro + "." + resultadoDecimal
    
    return resultado

print(f"{n} em quaternário: {converterBase(n, 4)}")
print(f"{n} em octal: {converterBase(n, 8)}")
print(f"{n} em hexadecimal: {converterBase(n, 16)}")

# resultado
# 1010010.011 em quaternário: 1102.12
# 1010010.011 em octal: 242.30 (corrigir)
# 1010010.011 em hexadecimal: 52.6