import sympy as sy
import numpy as np
from matplotlib import pyplot as plot

x = sy.Symbol ('x')
fx = x*sy. exp(x) - 10
print('f(x):', fx)
g1x = x-0.5*fx
print('g1(x):', g1x)
dg1x = sy.diff(g1x, x)
print('g1\'(x):', dg1x)

fx = sy.lambdify(x, fx)
g1x = sy.lambdify(x, g1x)
dg1x = sy.lambdify(x, dg1x)

interval = np.linspace(1, 2)
plot.plot(interval, fx(interval),
label='f(x)')
plot.plot(interval, g1x(interval),
label='g1(x)')
plot.plot(interval, dg1x(interval),
label='g\'1(x)')
plot.grid()
plot.legend()
plot.show()