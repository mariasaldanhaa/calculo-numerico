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