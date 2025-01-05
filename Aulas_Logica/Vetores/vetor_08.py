alturas = []
media_altura = 0


for i in range(5):
    alturas.append(float(input(f"Digite a altura do {i+1}º jogador: ")))

media_altura = sum(alturas)/len(alturas)

print("\n...Relatório...\n")
print(f"A média de altura dos jogadores é de {media_altura:.2f}m.")
for altura_list in alturas:
    if altura_list < media_altura:
        print(f"As alturas abaixo da média são: {altura_list:.2f}m")