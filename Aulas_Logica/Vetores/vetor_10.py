numeros = []
pares = []
impares = []

for i in range(10):
    numero = int(input(f"Digite o {i+1}º número inteiro: "))
    numeros.append(numero)

for num in numeros:
    if num % 2 == 0:
        pares.append(num)
    else:
        impares.append(num)

print(f"Lista de números:", numeros)
print(f"Lista de números impares:", impares)
print(f"Lista de números pares:", pares)