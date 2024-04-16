from random import randint
matriz = []
linha = []
for x in range(5):
    for y in range(5):
        linha.append(randint(1,100))
    matriz.append(linha)
    linha = []
print(matriz)
soma = 0
for x in range(0,5,2):
    for y in range(5):
        soma = soma+matriz[x][y]


media = soma/5
print(f'{media=}')


