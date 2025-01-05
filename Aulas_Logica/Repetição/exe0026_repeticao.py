def main():
    print("Nossos Serviços: \n")
    serv_pet = ["1 - banho", "2 - tosa","3 - Banho e tosa","4 - outros "]
    string_formatada = "\n".join(serv_pet)
    print(string_formatada)

servico = 0
soma_banho = 0
soma_tosa = 0
somabanho_tosa = 0
soma_outros = 0

main()

for i in range (5):
    codigo_servico = int(input(f"Digite o código do serviço {i+1}: "))

    if codigo_servico == 1:
        soma_banho+=1
    elif codigo_servico == 2:
        soma_tosa+=1
    elif codigo_servico == 3:
        somabanho_tosa+=1
    elif codigo_servico == 4:
        soma_outros+=1
    else:
        print("Código inválido!")

print(f"Serviços do dia: \n")
print(f"Banho: {soma_banho} \t")
print(f"Tosa: {soma_tosa} \t")
print(f"Banho e Tosa: {somabanho_tosa} \t")
print(f"Outros: {soma_outros} \t")