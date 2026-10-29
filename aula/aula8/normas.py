import numpy as np

mat = np. array ([
[ 3, -5,7],
[ 1, -2, 4],
[-8, 1, -7]
], dtype='double')

print(np.linalg.norm(mat, 1))
print(np.linalg.norm(mat, 2))
print(np.linalg.norm(mat, np.inf))