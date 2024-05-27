#1) por meio do dataset space.csv, trace um grafico em barras mostrando quantas empresas espaciais os eua e a china possuem
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('space.csv', delimiter=';')

us_companies = df[df['Location'].str.contains('USA')]
china_companies = df[df['Location'].str.contains('China')]

num_us_companies = us_companies['Company Name'].nunique()
num_china_companies = china_companies['Company Name'].nunique()

countries = ['USA', 'China']
num_companies = [num_us_companies, num_china_companies]

plt.figure(figsize=(8, 6))
plt.bar(countries, num_companies, color=['blue', 'red'])
plt.xlabel('País')
plt.ylabel('Número de Empresas Espaciais')
plt.title('Número de Empresas Espaciais nos EUA e na China')
plt.show()

#--------------------------------------------------------------

#2) por meio do dataset paises.csv, trace dois graficos de linhas em um mesmo plano cartesiano, um mostrando a taxa de mortalidade (Deathrate) e outro a taxa de natalidade (Birthrate) dos paises da america do norte (NORTHERN AMERICA)
df = pd.read_csv('paises.csv', delimiter=';')

north_america = df[df['Region'] == 'NORTHERN AMERICA']

countries = north_america['Country']
birthrate = north_america['Birthrate']
deathrate = north_america['Deathrate']

plt.figure(figsize=(10, 6))
plt.plot(countries, birthrate, label='Taxa de Natalidade')
plt.plot(countries, deathrate, label='Taxa de Mortalidade')
plt.xlabel('País')
plt.ylabel('Taxa')
plt.title('Taxa de Natalidade e Mortalidade na América do Norte')
plt.legend()
plt.show()