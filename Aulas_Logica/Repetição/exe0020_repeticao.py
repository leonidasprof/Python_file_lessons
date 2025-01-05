num = 1
while num != 0:
    num = int(input("digite um número: "))
    if num > 0:
        print("Esse número é maior que zero! ")
    elif num == 0:
        print("Esse número é igual a zero! ")
    else:
        print("Esse número é menor que zero! ")

print("Fim da execução ")