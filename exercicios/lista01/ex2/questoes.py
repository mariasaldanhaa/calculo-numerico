def imprimir(n):
    if abs(n) >= 1:
        print(round(n, 2)) 
        print((int((n * 100))) /100)
    else:
        print(round(n, 3)) 
        print((int((n * 1000))) /1000)
    
# letra a
imprimir(1.1598)
# arredondamento = 1.16
# truncamento = 1.15
print("\n")
# letra b
imprimir(7.3999)
# arredondamento = 7.4
# truncamento = 7.39
print("\n")
# letra c
imprimir(-5.9012)
# arredondamento = -5.9
# truncamento = -5.9
print("\n")
# letra d
imprimir(1.1615)
# arredondamento = 1.16
# truncamento = 1.16
print("\n")
# letra e
imprimir(3.1355985)
# arredondamento = 3.14
# truncamento = 3.13
print("\n")
# letra f
imprimir(8.394559)
# arredondamento = 8.39
# truncamento = 8.39
print("\n")
# letra g
imprimir(-9.907142)
# arredondamento = -9.91
# truncamento = -9.9
print("\n")
# letra h
imprimir(0.1615221)
# arredondamento = 0.162
# truncamento = 0.161