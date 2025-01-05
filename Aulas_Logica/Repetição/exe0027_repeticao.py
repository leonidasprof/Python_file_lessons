qt_homens = 0
idade_velhas = 0
soma_idade = 0
qt_mulheres_20 = 0

for i in range(5):
    genero = input(f"Digite o gênero da {i+1} pessoa (F ou M): ")
    idade = int(input(f"Digite a idade da {i+1} pessoa: "))

    if genero == "M":
       qt_homens += 1
    else:
        if idade > idade_velhas:
            idade_velhas = idade
        if idade > 20:
            qt_mulheres_20 += 1

    soma_idade += idade

print(f"Total de homens: {qt_homens}")
print(f"Idade da mulher mais velha: {idade_velhas}")
print(f"Média de idade do grupo: {soma_idade / 5}")
print(f"total de mulheres com mais de 20 anos: {qt_mulheres_20}")

