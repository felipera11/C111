import numpy as np

np.random.seed(10)

mtzRandom = np.random.randint(1,50,16).reshape(4,4)


#Mostra os elementos únicos de mtzRandom
print(np.unique(mtzRandom))

#Mostra os elementos que aprecem duas vezes

unicos, contagem = np.unique(mtzRandom, return_counts=True)
dicionario = dict(zip(unicos, contagem))

print([chave for chave, valor in dicionario.items() if valor == 2])