# Utilize um loop while e um loop for para contar de 0 até o número que o usuário digitar:

# ------------------------------------------ ESCREVA SEU CÓDIGO ABAIXO -----------------------------------------------------------

# LOOP WHILE


numero = int(input("Digite um número: "))
contador = 0

while contador <= numero:
    print(contador)
    contador += 1




# LOOP FOR


numero = int(input("Digite um número: "))

for i in range(numero + 1):
    print(i)