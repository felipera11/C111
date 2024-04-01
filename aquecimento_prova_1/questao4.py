import numpy as np

arr = np.loadtxt('paises.csv', delimiter=';', dtype='str', encoding='utf-8', skiprows=1)

north_america = arr[arr[:, 1] == 'NORTHERN AMERICA                   ']

print(len(north_america))