import pandas as pd

#1) Carregue o dataset paises.csv. Em seguida, mostre:
# a) quais os paises da oceania
# b) quantos paises sao da oceania

paises = pd.read_csv('paises.csv', delimiter=';')

oceania = paises[paises['Region'] == 'OCEANIA']

# a
print("Paises da Oceania:")
print(oceania['Country'])

# b
print("Quantidade de paises da Oceania:")
print(len(oceania))

print("\n")

#2) mostre a media da taxa de alfabetizacao (Literacy(%)) do planeta
media = paises['Literacy (%)'].mean()

print("Media da taxa de alfabetizacao do planeta:")
print(media)

print("\n")

#3) encontre o nome e a regiao do pais que possui a maior populaçao
maior_populacao = paises['Population'].max()
pais = paises[paises['Population'] == maior_populacao]

print("Pais com maior populacao:")
print(pais['Country'])
print("Regiao:")
print(pais['Region'])

print("\n")

#4) busque o nome de todos os países do dataset que nao possuem costa maritima (Coastline (coast/area ratio) == 0) e guarde-os em um arquivo chamado 'noCoast.csv'
noCoast = paises[paises['Coastline (coast/area ratio)'] == 0]
noCoast.to_csv('noCoast.csv', index=False)

print("Paises sem costa maritima:")
print(noCoast['Country'])