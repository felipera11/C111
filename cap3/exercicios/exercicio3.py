
nome = input("Digite o nome do aluno: ")

media = float(input("Digite a média do aluno: "))
    
situacao = "AP" if media >= 60 else "RP"

aluno = {"nome": nome, "média": media, "situação": situacao}

print(aluno)