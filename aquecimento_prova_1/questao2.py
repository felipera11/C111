import numpy as np

arr = np.loadtxt('paises.csv', delimiter=';', dtype='str', encoding='utf-8', skiprows=1)

regions = np.unique(arr[:, 1])
print("Diferentes Regiões do planeta:", regions)