def f(x):
    return x**3 - 9*x**2 + 22*x - 15

# iteracao 0 
i=0; a=2; b=3; x=(a+b)/2; xa=float("nan"); e=abs((x-xa)/max(x, 1))
print("It, ", "a, ", "b, ", "x, ", "f(x), ", "Erro, ", "Sinal")
print([i, a, b, x, f(x), e, f(a)*f(x)])

print("\n")

# iteracao 1
i+=1; b=x; xa=x; x=(a+b)/2; e=abs((x-xa)/max(x, 1))
print("It, ", "a, ", "b, ", "x, ", "f(x), ", "Erro, ", "Sinal")
print([i, a, b, x, f(x), e, f(a)*f(x)])

print("\n")

# iteraco 2
i+=1; a=x; xa=x; x=(a+b)/2; e=abs((x-xa)/max(x, 1))
print("It, ", "a, ", "b, ", "x, ", "f(x), ", "Erro, ", "Sinal")
print([i, a, b, x, f(x), e, f(a)*f(x)])

print("\n")

# iteracao 3
i+=1; b=x; xa=x; x=(a+b)/2; e=abs((x-xa)/max(x, 1))
print("It, ", "a, ", "b, ", "x,", "f(x), ", "Erro, ", "Sinal")
print([i, a, b,x,f(x), e,f(a)*f(x)])

print("\n")

# iteracao 4
i+=1; a=x; xa=x; x=(a+b)/2; e=abs((x-xa)/max(x, 1))
print("It,", "a, ", "b, ", "x, ", "f(x), ", "Erro, ", "Sinal")
print([i, a, b,x,f(x), e,f(a)*f(x)])