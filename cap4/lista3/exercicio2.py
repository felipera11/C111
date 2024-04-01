import numpy as np

arr = np.loadtxt('space.csv', delimiter=';', dtype='str', encoding='utf-8', skiprows=1)

#Array de gastos
gastos = arr[:, -2].astype(float)

#Gasto total
gastoTotal = gastos[gastos > 0].sum()

#Quantidade de missões com gastos maiores que 0
availableMissions = gastos[gastos > 0].size

#Média de gastos
average = gastoTotal / availableMissions
print(round(average,2), ' milhões de dólares\n')