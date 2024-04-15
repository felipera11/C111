import numpy as np

arr = np.loadtxt("brands.csv", delimiter=";", dtype=str,encoding='utf-8',skiprows=1)

#questao 1
print("")
print("-----------Questão 1-----------")

value_2021 = arr[arr[:, 0] == "Microsoft", 10]
value_2022 = arr[arr[:, 0] == "Microsoft", 9]
valorizacao = float(value_2022) - float(value_2021)

print(f"Valorização da Microsoft de 2021 para 2022: ${valorizacao:.2f}")

#questao 2
print("")
print("-----------Questão 2-----------")

A_arr = arr[np.char.startswith(arr[:, 0], "A")]
A_arr = A_arr[:, 0]
A_arr = np.sort(A_arr)

print(f"Marcas que começam com a letra 'A' em ordem alfabética: {A_arr}")

#questao 3
print("")
print("-----------Questão 3-----------")

total_empresas = arr.shape[0]
empresas_usa = arr[arr[:, 3] == "United States"]

porcentagem_usa = (empresas_usa.shape[0] / total_empresas) * 100

print(f"Porcentagem de empresas dos Estados Unidos: {porcentagem_usa}%")

#questao 4
print("")
print("-----------Questão 4-----------")

sliced_arr = arr[:, 0:3]
after_2000 = sliced_arr[sliced_arr[:, 2].astype(int) > 2000]
after_2000 = after_2000[:, 0:1]

print(f"Marcas criadas após o ano 2000: {after_2000}")

#questao 5
print("")
print("-----------Questão 5-----------")

anos = np.unique(arr[:, 2], return_counts=True)
mais_empresas = anos[0][anos[1].argmax()]

print(f"Ano com mais empresas fundadas: {mais_empresas}")