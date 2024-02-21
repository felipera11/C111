# # Coleções
# # Tuplas //////////////////////////////////////////////////////////////////////////////////////////
# # É uma coleção imutável

# nomes = ('Goku','Vegeta','Trunks','Gohan')
# print(nomes)

# #Slicing
# print(nomes[0])
# print(nomes[:2])
# print(nomes[1:3])
# print(nomes[-2])


# # Listas //////////////////////////////////////////////////////////////////////////////////////////
# # É uma coleção mutável

# nomes = ['Goku','Vegeta','Trunks','Gohan']

# #ADD
# nomes.append('Piccolo')

# #UPDATE
# nomes[0] = 'Bulma'

# #DELETE
# del nomes[1]
# nomes.remove('Trunks')

# #SELECT
# print(nomes)



# # Conjuntos (Sets) ////////////////////////////////////////////////////////////////////////////////
# # É uma coleção mutável e não ordenada de elementos únicos

# nomes = {'Goku','Vegeta','Trunks','Gohan'}

# # ADD
# nomes.add('Bulma')
# nomes.add('Goku')

# # DELETE
# nomes.remove('Trunks')

# # UPDATE (não é possível atualizar um item específico, mas é possível adicionar um novo item)

# # SELECT
# print(nomes)


# # Dicionários /////////////////////////////////////////////////////////////////////////////////////
# # É uma coleção mutável e não ordenada de itens. Cada item é uma dupla chave-valor
# # Usa índices customizados

pessoa = {'nome':'Goku','idade':30,'altura':1.80}

# ADD
pessoa['sexo'] = 'M'

# DELETE
del pessoa['idade']

# UPDATE
pessoa['nome'] = 'Son Goku'

pessoa2 = {'nome':'Vegeta','idade':35,'altura':1.70}
pessoa3 = {'nome':'Trunks','idade':20,'altura':1.60}
pessoa4 = {'nome':'Gohan','idade':25,'altura':1.75}

# Lista de dicionários (Coleção de outra coleção)
pessoas = [pessoa,pessoa2,pessoa3,pessoa4]
print(pessoas[0]['nome'])