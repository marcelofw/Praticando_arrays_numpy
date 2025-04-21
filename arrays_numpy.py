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

# a = np.array([1, 2, 3])
# print(a.shape)
# b = np.array([[1, 3], [5, 2]])
# print(b.shape)
# print(b[0])     #primeira linha da matriz
# print(b[1])     #segunda linha da matriz
# c = np.array([[1, 2, 4], [1, 3, 7]])
# print(c.shape)

# a = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])
# print(a[0])
# print(a[1:3])
# indices = [1, 4, 6, 7]
# print(a[indices])
# mascara_bool = (a % 2 == 0)     #máscara booleana
# print(a[mascara_bool])
# print(mascara_bool)
# a[1] = 200
# print(a)

# try:
#     a[0] = "Será que adiciona string no array?"
# except:
#     print("Operação não permitida.")

# b = np.array(["tentando", "criar", "array", "de", "strings"])
# print(b)
# print(np.char.upper(b))

# a = np.array([1, 2, 3, 4, 5])
# print(type(a))
# print(a.cumsum())
# print(a.cumprod())

# b = np.arange(0, 50, 5)
# print(b)

# a = np.zeros(5)
# print(a)

# a = np.eye(5)
# print(a)

# a = np.diag(np.array([1, 2, 3, 4]))
# print(a)

# a = np.array([True, False, True, False, True])
# print(a)

# a = np.linspace(0, 10)      #linspace(início, fim, num) -> num = 50 por padrão
# print(a)
# b = np.linspace(0, 10, 15)
# print(b)

# a = np.logspace(0, 5, 10)
# print(a)

# matriz_a = np.array([[1, 2, 3], [4, 5, 6]])
# print(matriz_a)
# print(matriz_a.shape)

# zeros = np.ones((2, 3))     #2 linhas, 3 colunas
# print(zeros)

# lista = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# a = np.matrix(lista)
# print(a)
# print(a[1, 2])      #[linha, coluna]
# print(a[0:2, 2])

a = np.array([[1, 2, 3], [4, 5, 6]], dtype = float)
print(a)






















