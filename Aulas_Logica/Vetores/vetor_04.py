palavras = []

for i in range(5):
    palavras.append(input(f"Digite a {i+1}ª palavra: "))

    palavras.sort()

    i += 1

print(f"Palavras em ordem alfabética: ")
for palavra in palavras:
    print(palavra)