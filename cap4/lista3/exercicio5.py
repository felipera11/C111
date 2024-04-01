import numpy as np

arr = np.loadtxt('space.csv', delimiter=';', dtype='str', encoding='utf-8', skiprows=1)

#Separando as missões de cada empresa (incide 1) e cada quantidade
companies, counts = np.unique(arr[:,1], return_counts=True)

print('Quantidade de missões por empresa:')
for i in range(companies.size):
    print(companies[i], ':', counts[i])