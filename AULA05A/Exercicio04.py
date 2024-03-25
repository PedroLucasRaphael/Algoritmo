import math
print('calculo de equação de segundo grau')
print('Ax2 + Bx + C = 0')
A = float(input("digite o valor de A"))
B = float(input("digite o valor de B"))
C = float(input("digite o valor de C"))

if (A == 0):
    print('Os valores não formam ua equação de segundo grau')
else:
    delta = math.pow(B,2) - (4* A * C)
    if (delta < 0):
        print('A equação não possui valores reais')
    elif (delta == 0):
        print('A equação possui apenas uma raiz')