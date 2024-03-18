#crie dois arrays: um de números pares de 0 até 51 e outro também de números pares de 100 até 50. Em seguida, os concatene e mostre os resultados ordenados

import numpy as np

array1 = np.arange(0, 52, 2)
array2 = np.arange(100, 49, -2)

array = np.concatenate((array1, array2))

print(np.sort(array))