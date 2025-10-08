# Crie uma lista com 3 dicionários, cada um representando uma pessoa (contendo nome, idade, cidade). Use um laço para imprimir o nome de cada pessoa.



# ------------------------------------------ ESCREVA SEU CÓDIGO ABAIXO -----------------------------------------------------------

pessoas = [
    {'nome': 'Ana', 'idade': 25, 'cidade': 'Barueri'},
    {'nome': 'Bruno', 'idade': 30, 'cidade': 'Osasco'},
    {'nome': 'Carla', 'idade': 22, 'cidade': 'Santana de Parnaiba'}
]


for pessoa in pessoas:
    print(pessoa['nome'])