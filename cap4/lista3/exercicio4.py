import numpy as np

arr = np.loadtxt('space.csv', delimiter=';', dtype='str', encoding='utf-8', skiprows=1)

#Buscando as missões da SpaceX (Indice 1)
spacex = arr[arr[:,1] == 'SpaceX']

#Buscando a missão mais cara
mostExpensive = spacex[spacex[:,-2].astype(float).argmax()]

print(mostExpensive, '\n')