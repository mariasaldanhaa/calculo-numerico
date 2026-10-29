import numpy as np

# Matriz estendida do sistema
mat = np. array ([
[1, 1, 1,1],
[4,4, 2,2],
[2,1,-1,0]
], dtype='double')
print('Matriz original')
print(mat)

# L2 <- L2 - 4 * L1

mat [1, :] = mat [1, :] - 4 * mat [0, :]
print('\nL2 <- L2 - 4 * L1')
print (mat)

# L3 <- L3 - 2 * L1
mat [2, :] = mat [2, :] - 2 * mat [0, :]
print('\nL3 <- L3 - 2 * L1')
print(mat)

# L2 <- > L3
aux = np. copy(mat [1, :])
mat [1,:] = np.copy(mat [2, :])
mat [2,:] = np.copy(aux)
print('\nL2 <- > L3')
print(mat)

# z = -2/-2
z = mat [2,3] / mat [2,2]

# y = (-2 - (-3z) / 1
y = (mat[1,3] -(mat[1,2]* z)) / mat[1,1]

# x = (1 - (z + y)) / 1
x= (mat[0,3]-(mat[0,1]*y+mat[0,2]*z))/ mat[0,0]

print('nSolução:')
print(f'x={x}')
print(f'y={y}')
print(f'z={z}')