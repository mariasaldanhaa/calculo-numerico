import sys
import numpy as np

eps = sys.float_info.epsilon

mat = np. array ([
[eps, 2, 4],
[ 1, eps, 3]
], dtype='double')
print('Matriz original')
print(mat)

# L2 <- L2 - L1 / eps
mat [1, :] = mat[1, :] -mat[0,:] / eps
print('nL2 <- L2 - L1 / eps')
print(mat)

y = mat [1,2] / mat [1,1]
x = (mat[0,2]-(mat[0,1]*y))/mat[0,0]

print('\nSolução:')
print(f'x={x}')
print(f'y={y}')