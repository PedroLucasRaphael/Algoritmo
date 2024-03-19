lado1 = int(input("digite o tamanho do primeiro lado"))
lado2 = int(input("digite o tamanho do segundo lado"))
lado3 = int(input("digite o tamanho do terceiro lado"))

if (lado1+lado2<lado3) or (lado2+lado3<lado1) or (lado1+lado3<lado2):
    print("não é um triangulo >:(")
if (lado1==lado2==lado3):
    print("é um triangulo equilátero")
if (lado1==lado2!=lado3) or (lado2==lado3!=lado1) or (lado3==lado1!=lado2):
    print("é um triangulo isósceles")
if (lado1!=lado2!=lado3):
    print("é um triangulo escaleno")
