l1 = float(input("insira oo primeiro lado:"))
l2 = float(input("insira o segundo lado:"))
l3 = float(input("insira o terceiro lado:"))

if (l1<l2+l3) or (l2<l1+l3) or (l3<l2+l1):
    print("não é um triangulo :(")
    if (l1==l2) and (l2==l3):
        print("é um triangulo equilatero")
    elif (l1==l2) or (l2==l3) or (l3==l1):
        print("é um triangulo isosceles")
    else:
        print("é um triangulo escaleno")
