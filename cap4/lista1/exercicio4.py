#crie uma matriz formada por uns de tamanho 3x4. Em seguida, transforme-a em um array 1D

import numpy as np

matriz = np.ones((3, 4))

array = matriz.flatten()

print(array)