def erro(x, aproximado):
    erroAbsoluto = abs(x - aproximado)
    erroRelativo = erroAbsoluto / abs(x)
    
    print(f"Erro absoluto de {x} e {aproximado}: {erroAbsoluto:.8f}")
    print(f"Erro relativo de {x} e {aproximado}: {erroRelativo:.8f}")
    
# letra a
erro(1.00001, 1)
print("\n")
# letra b
erro(100001, 100000)
print("\n")
# letra c
erro(32.65483, 34.1645)
print("\n")
# letra d
erro(5.87135, 5.87049)
print("\n")

# Erro absoluto de 1.00001 e 1: 0.00001000
# Erro relativo de 1.00001 e 1: 0.00001000


# Erro absoluto de 100001 e 100000: 1.00000000
# Erro relativo de 100001 e 100000: 0.00001000


# Erro absoluto de 32.65483 e 34.1645: 1.50967000
# Erro relativo de 32.65483 e 34.1645: 0.04623114


# Erro absoluto de 5.87135 e 5.87049: 0.00086000
# Erro relativo de 5.87135 e 5.87049: 0.00014647