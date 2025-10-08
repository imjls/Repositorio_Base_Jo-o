# Calcule a média das notas utilizando um loop while e também um loop for


# ------------------------------------------ ESCREVA SEU CÓDIGO ABAIXO -----------------------------------------------------------

notas = ['9.5', '10', '6.75', '5.5']

# LOOP WHILE

i = 0
soma = 0
while i < len(notas):
    soma += float(notas[i])
    i += 1
media = soma / len(notas)
print("Média (while):", media)




# LOOP FOR

soma = 0
for nota in notas:
    soma += float(nota)
media = soma / len(notas)
print("Média (for):", media)
