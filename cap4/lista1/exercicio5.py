#crie uma matriz de tamanho qualquer. Extraia seu número de linhas e colunas, multiplique-os, e diga se esta matriz poderia se tornar um vetor com número par ou ímpar de elementos.

import numpy as np

matriz = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

linhas, colunas = matriz.shape

if (linhas * colunas) % 2 == 0:
    print("Vetor com número par de elementos")
else:
    print("Vetor com número ímpar de elementos")