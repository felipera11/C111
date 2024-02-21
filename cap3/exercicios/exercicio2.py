loja1 = {"iPhone", "Samsung Galaxy", "Google Pixel"}
loja2 = {"Samsung Galaxy", "OnePlus", "Xiaomi"}

todos_os_modelos = loja1.union(loja2)
modelos_disponiveis_em_ambas = loja1.intersection(loja2)

#todos os modelos disponíveis para compra
print("\nTotal de modelos disponíveis para compra:")
for modelo in todos_os_modelos:
    print(modelo)

#modelos disponíveis em ambas as lojas
print("Modelos disponíveis em ambas as lojas:")
for modelo in modelos_disponiveis_em_ambas:
    print(modelo)