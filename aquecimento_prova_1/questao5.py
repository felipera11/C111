import numpy as np

arr = np.loadtxt('paises.csv', delimiter=';', dtype='str', encoding='utf-8', skiprows=1)

#Buscando as missões da latin_arr (Indice 1)
latin_arr = arr[arr[:,1] == 'LATIN AMER. & CARIB    ']

#Buscando a missão mais cara
max_gdp = latin_arr[latin_arr[:,-2].astype(float).argmax()]

max_gdp = max_gdp[0]

print(max_gdp, '\n')