import numpy as np

# arr1 = np.array([1, 12, 39, 49, 20, 87])
# print(arr1)
# lista1 = [1, 2, 3, 4]
# arr2 = np.array(lista1)
# print(arr2)
# print(lista1)

# a = np.array([1, 2, 3])
# b = np.array([4, 5, 6])
# print(a + b)
# print(a * b)    #produto vetorial
# print(a @ b)    #produto escalar
# print(type(a))

# a = np.array([1, 2, 3])             #1D array (vetor)
# b = np.array([[1, 2], [3, 4]])      #2D array (matriz)
# c = np.array([[[1], [2], [3], [4]]])#3D array
# print(a.ndim)
# print(b.ndim)
# print(c.ndim)

a = np.array([1, 2, 3])
print(a.shape)
b = np.array([[1, 3], [5, 2]])
print(b.shape)
print(b[0])     #primeira linha da matriz
print(b[1])     #segunda linha da matriz
c = np.array([[1, 2, 4], [1, 3, 7]])
print(c.shape)


