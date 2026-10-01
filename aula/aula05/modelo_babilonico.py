def g(x):
    return x/2 + 5 / (2*x)

x=2

print('k, x, xa, g(x), Erro')
for k in range(5):
    xa=x; x=g(x);e=abs((x-xa)/max(x, 1))
    fx=g(x)
    e=e
    print(f'{k}, {x:.10f}, '+
          f'{xa:.10f}, {fx:.10f}, {e:.10f}')