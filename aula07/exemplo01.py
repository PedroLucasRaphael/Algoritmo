soma=0
for i in range(1,6):
    idade= int(input(f'entre com a idade {i}: '))
    soma= soma+idade
media= soma/5
print(f'A media das idades é {round(media)} anos.')
