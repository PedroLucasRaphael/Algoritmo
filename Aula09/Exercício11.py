from random import randint
matriz = []
linha = []
for x in range(4):
    for y in range(4):
        linha.append(randint(1,100))
    matriz.append(linha)
    linha = []
print(matriz)
soma = 0
for i in range(4):
    soma = soma+matriz[i][i]

print(f'{soma=}')
