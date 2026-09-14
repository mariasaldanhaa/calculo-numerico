n1 = "425.135"
n2 = "10011001101.1101"
n3 = "12FA7.4C8"

def paraDecimal(numero, base):
    partes = numero.split(".")

    inteira = partes[0]
    decimal = partes[1]

    somaInteiro = 0
    somaDecimal = 0

    for posicao in range(len(inteira)):
        algarismo = int(inteira[posicao], base)
        somaInteiro = somaInteiro + (algarismo * (base ** (len(inteira) - 1 - posicao)))

    for posicao in range(len(decimal)):
        algarismo = int(decimal[posicao], base)
        somaDecimal = somaDecimal + (algarismo * (base ** (-(posicao + 1))))

    return somaInteiro + somaDecimal
    
resultadoN1 = paraDecimal(n1, 8)
resultadoN2 = paraDecimal(n2, 2)
resultadoN3 = paraDecimal(n3, 16)

print(f"Resultado de {n1} para decimal: {resultadoN1:.8f}")
print(f"Resultado de {n2} para decimal: {resultadoN2:.8f}")
print(f"Resultado de {n3} para decimal: {resultadoN3:.8f}")

# Resultado de 425.135 para decimal: 277.18164062
# Resultado de 10011001101.1101 para decimal: 1229.81250000
# Resultado de 12FA7.4C8 para decimal: 77735.29882812