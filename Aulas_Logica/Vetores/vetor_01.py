#criando vetor
valores = [4, 7, -23, 67]

#Substituindo valor
valores[2] = 8

#adicionando novo valor
valores.append(1)

#adcionando em um índice específico
valores.insert(0, 100)

#ordem crescente
valores.sort()

#ordem decrescente
valores.sort(reverse=True)

#contar valores
print(len(valores))

#remover último valor pelo índice
valores.pop()

#remover valor específico pelo índice
valores.pop(0)

#remover valor pelo conteúdo
valores.remove(8)

print(valores)
print(len(valores))
