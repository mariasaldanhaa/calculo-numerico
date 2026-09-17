import numpy as np
import matplotlib.pyplot as plot


def f(x):
    return x**3 - 9*x**2 + 22*x - 15


def fl(x):
    return 3*x**2 - 18*x + 22


interval = np.linspace(1, 6)
plot.plot(interval, f(interval))
plot.plot(interval, fl(interval))
plot.grid()
plot.show()