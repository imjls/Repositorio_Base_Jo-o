# Dada a lista numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# Crie um dicionário com duas chaves: "pares" e "ímpares", onde cada chave terá uma lista com os números correspondentes.


# ------------------------------------------ ESCREVA SEU CÓDIGO ABAIXO -----------------------------------------------------------

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

resultado = {"pares": [], "ímpares": []}

for n in numeros:
    if n % 2 == 0:
        resultado["pares"].append(n)
    else:
        resultado["ímpares"].append(n)

print(resultado)
