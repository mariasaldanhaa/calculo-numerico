import numpy as np

def f(x):
    return x * np.exp(x) - 10

def g2(x):
    return x - 0.05 * f(x)

x=1.7; print('k, x, g2(x), f(x)')
for k in range(5):
    gx=g2(x); xa=x; x=g2(x)
    print('{k}, {x:.5f}, '.format(k=k+1, x=xa) +
        '{gx:.5f} '.format (gx=gx))