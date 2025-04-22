import numpy as np

# a = np.arange(1, 10)
# print(a)
# soma = np.sum(a)
# print(soma)
# produto = np.prod(a)
# print(produto)
# soma_acumulada = np.cumsum(a)
# print(soma_acumulada)

# b = np.array([1, 2, 3])
# c = np.array([4, 5, 6])
# d = np.add(b, c)
# print(d)

# e = np.array([[1, 2], [3, 4]])
# f = np.array([[5, 6], [7, 8]])
# g = np.dot(e, f)
# print(g)
# h = e @ f
# print(h)
# i = np.tensordot(e, f)
# print(i)

# a = np.diag(np.arange(3))
# print(a)
# print(a[1, 1])
# print(a[1])     #sem a vírgula imprime somente a linha
# print(a[:, 2])  #imprime somente a coluna 2

# a = np.arange(10)
# print(a[2: 9: 3])      #start, end, step
# print(a.min())
# print(a.max())

# print(np.array([1, 2, 3]) + 1.5)   #somar 1,5 a cada elemento do array

# a = np.array([1.2, 1.4, 1.6, 1.8, 2.0])
# print(np.around(a))

# a = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
# print(a)
# b = a.flatten()     #cria um array unidimensional a partir de um multidimensional
# print(b)

a = np.array([1, 2, 3])
print(np.repeat(a, 3))
print(np.tile(a, 3))