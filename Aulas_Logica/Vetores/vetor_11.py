nome = True
contador = 1
saltos = []

while nome != "sair":
    print(f"Atleta", contador)
    nome = input("Digite o nome do Atleta: ").capitalize()
    if nome == "sair":
        break
    else:
        for i in range(5):
            print(i+1,"º Salto")
            distancia = float(input("Digite a distância em metros: "))
            saltos.append(distancia)
    media = sum(saltos) / len(saltos)

    print("\n\t******Resultado******")
    print("Atleta:", nome)

    for i in range(5):
        print(i + 1, "º Salto:", saltos[i],"m")

    print("Media dos saltos:", round(media, 2),"m")
    print("\n")
    contador += 1