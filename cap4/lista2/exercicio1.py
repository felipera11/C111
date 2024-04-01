import numpy as np

np.random.seed(5)

#gera um array de float com 10 elementos positivos e negativos entre 0 e 1
arrRandom = np.random.rand(10) * 2 - 1

#multiplica por 100 e salva somente a parte inteira
arrFinal = (arrRandom*100).astype(int)
print(arrFinal)