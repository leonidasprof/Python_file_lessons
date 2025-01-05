total_homens = 0
idade_meulher_mais_velha = 0
soma_idades = 0
total_mulheres_mais20 = 0
cont = 1

while cont<=5:
    idade = int(input("digite a idade: "))
    genero = input("Digite o gênero (M/F): ").upper()

    if genero == "M":
        total_homens += 1

    elif genero == "F":
        if idade > idade_meulher_mais_velha:
            idade_meulher_mais_velha = idade

        if idade > 20:
            total_mulheres_mais20 += 1

    soma_idades += idade
    cont += 1

media_idade = soma_idades / 5

print(f"\nQuantidade de homens cadastrados: {total_homens}")
print(f"Idadde da mulher mais velha: {idade_meulher_mais_velha}")
print(f"Média de idade do grupo: {media_idade:.2f}")
print(f"Quantidade de mulheres com mais de 20 anos: {total_mulheres_mais20}")
