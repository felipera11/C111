import numpy as np

#Lendo arquivo de texto
arr = np.loadtxt('space.csv', delimiter=';', dtype='str', encoding='utf-8', skiprows=1)

#Quantidade de Falhas
failureCount = np.char.find(arr[:,-1], 'Success').sum() * (-1)

#Quantidade Total
totalCount = arr[:,-1].size

#Porcentagem de Sucesso
porcentagem = ((1-(failureCount/totalCount))*100)
print(round(porcentagem,2), "% de sucesso\n")