valor = float(input('digite o valor do produto aqui:'))

if (valor <= 1000.00):
    print('com desconto', (valor * 0.1))
elif (valor <= 5000.00) and (valor >= 1001.00):
    print('com desconto', (valor * 0.2))
elif (valor > 5000.00):
    print('com desconto', (valor * 0.3))
