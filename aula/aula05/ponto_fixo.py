import numpy as np

def f(x):
    return x * np.exp(x) - 10

def g1(x):
    return x - 0.5 * f (x)

x=1.7; print('k, x, g1(x)')
for k in range(5) :
    gx=g1(x);xa=x; x=g1(x)
    print('{k}, {x:.5f}, '.format(k=k+1, x=xa)+
          '{gx:.5f} '.format(gx=gx))