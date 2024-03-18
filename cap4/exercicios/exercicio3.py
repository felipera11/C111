#ordene os arrays resultantes da Questao 2 de forma decrescente

import numpy as np

#Questao 2

array1 = np.arange(0, 52, 2)
array2 = np.arange(100, 49, -2)

array = np.concatenate((array1, array2))

#Questao 3

array = np.sort(array)[::-1]

print(array)