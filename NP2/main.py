import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('world_happiness.csv', delimiter=',')

#questao 1

top_5_happy_df = df.sort_values(by='Healthy life expectancy', ascending=False).head(5)

plt.bar(top_5_happy_df['Country name'], top_5_happy_df['Healthy life expectancy'])
plt.xlabel('País')
plt.ylabel('Expectativa de Vida Saudável')
plt.title('"Expectativa de Vida Saudável" dos 5 Países Mais Felizes do Mundo')
plt.show()

#questao 2

top_20_unhappy_regions_df = df.sort_values(by='Ladder score', ascending=True).head(20)

group_regions = top_20_unhappy_regions_df.groupby('Regional indicator')
group_regions_sum = group_regions['Ladder score'].sum()

plt.pie(group_regions_sum, labels=group_regions_sum.index)
plt.title('Regiões dos 20 Países Mais Infelizes do Mundo')
plt.show()

#questao 3

top_5_happy_latin_caribe_df = df[df['Regional indicator'] == 'Latin America and Caribbean'].sort_values(by='Ladder score', ascending=False).head(5)

plt.scatter(top_5_happy_latin_caribe_df['Country name'], top_5_happy_latin_caribe_df['Ladder score'], s=top_5_happy_latin_caribe_df['Log GDP per capita']*500)
plt.xlabel('País')
plt.ylabel("Índice de Felicidade")
plt.title('Os 5 Países Mais Felizes da América Latina e Caribe')
plt.show()

#questao 4

brazil_freedom = df[df['Country name'] == 'Brazil']['Freedom to make life choices'].values[0]

latin_caribe_freedom = df[df['Regional indicator'] == 'Latin America and Caribbean']['Freedom to make life choices'].mean()

plt.bar(['Brasil', 'América Latina e Caribe'], [brazil_freedom, latin_caribe_freedom])
plt.xlabel('Local')
plt.ylabel('Liberdade de Escolha de vida')
plt.title('Liberdade de Escolha de Vida: Brasil x América Latina e Caribe')
plt.show()