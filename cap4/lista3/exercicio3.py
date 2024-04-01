import numpy as np

arr = np.loadtxt('space.csv', delimiter=';', dtype='str', encoding='utf-8', skiprows=1)

#Quantidade de Missões executadas nos EUA
localMissoes = arr[:,2]
USAMissions = np.char.count(localMissoes, 'USA').sum()
print(USAMissions, ' missões executadas nos EUA\n')