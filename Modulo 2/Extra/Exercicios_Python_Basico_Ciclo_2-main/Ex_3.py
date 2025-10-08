# Utilize um loop while e um loop for para adicionar itens na lista.
# Peça para que o usuário digite quantos filmes deseja adicionar, e também os nomes dos filmes



# ------------------------------------------ ESCREVA SEU CÓDIGO ABAIXO -----------------------------------------------------------

filmes = [] # Não apague esta lista

# LOOP WHILE

quantidade = int(input("Quantos filmes deseja adicionar? "))
i = 0

while i < quantidade:
    nome = input("Digite o nome do filme: ")
    filmes.append(nome)
    i += 1

print("Filmes adicionados:", filmes)





# LOOP FOR


quantidade = int(input("Quantos filmes deseja adicionar? "))

for i in range(quantidade):
    nome = input("Digite o nome do filme: ")
    filmes.append(nome)

print("Filmes adicionados:", filmes)


