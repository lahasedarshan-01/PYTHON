import numpy as np


A = np.random.randint(1,10,(3,3))
B = np.random.randint(1,10,(3,3))

print("Matrix A:")
print(A)

print("\nMatrix B:")
print(B)


add = A + B
print("\nAddition of Matrices:")
print(add)


mul = np.dot(A,B)
print("\nMultiplication of Matrices:")
print(mul)