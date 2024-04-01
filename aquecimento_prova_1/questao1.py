import numpy as np

arr = np.loadtxt('paises.csv', delimiter=';', dtype='str', encoding='utf-8', skiprows=1)

sliced_arr = arr[:, 0:4]

print(sliced_arr)