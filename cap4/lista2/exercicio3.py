import numpy as np

np.random.seed(10)

mtzRandom = np.random.randint(1,50,16).reshape(4,4)


col = mtzRandom.sum(axis=0)/4
lin = mtzRandom.sum(axis=1)/4


print(f'Maior elemento da média das colunas: {col.max()}')
print(f'Maior elemento da média das linhas: {lin.max()}')