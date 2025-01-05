from typing import List


lista_par = []
lista_impar = []
lista_inteiro = []


for i in range(10):
    num_inteiro = int(input(f"Digite o {i+1}º número inteiro: "))
    lista_inteiro.append(num_inteiro)

for num in lista_inteiro:
    if num % 2 == 0:
        lista_par.append(num)
    else:
        lista_impar.append(num)

print(f"\n......Resultados:\n")
print(f"......1ª lista: {lista_inteiro} ")
print(f"\n......lista de números pares: {lista_par}")
print(f"\n......lista impar: {lista_impar}")