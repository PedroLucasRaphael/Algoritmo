frase= input('digite uma frase: ')
quantidade= 0
for letra in frase:
    if letra in 'AEIOUaeiouáéíóúãê':
        quantidade= quantidade + 1
print(f'A quantidade de vogais nesta frase é {quantidade}')

