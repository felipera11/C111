import numpy as np

arr = np.loadtxt('paises.csv', delimiter=';', dtype='str', encoding='utf-8', skiprows=1)

taxa_literacy = arr[:, 9].astype(float)
media_taxa_literacy = np.mean(taxa_literacy)

print("Media taxa de alfabetismo: " + str(media_taxa_literacy) + "%")