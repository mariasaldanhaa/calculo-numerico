import numpy as np

mat1 = np.array([[71, 41], [51, 30]], dtype='double')
mat2 = np.array([[71, 41], [52, 30]], dtype='double')

print(np.linalg.cond(mat1, 1))
print(np.linalg.cond(mat1, 2))
print(np.linalg.cond(mat1, np.inf))

print(np.linalg.cond(mat2, 1))
print(np.linalg.cond(mat2, 2))
print(np.linalg.cond(mat2, np.inf))