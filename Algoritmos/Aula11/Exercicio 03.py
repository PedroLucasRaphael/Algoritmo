idade_por_sobrenome = {}

for _ in range(3):
    sobrenome = input("digite o sobrenome")
    idade = int(input("digite a idade"))
    idade_por_sobrenome[sobrenome] = idade

sobrenome_mais_velho = max(idade_por_sobrenome, key=idade_por_sobrenome.get)

print(f"\n0 sobrenome da pessoa mais velha é: {sobrenome_mais_velho}")