vhora = float(input("digite o valor da hora trabalhada:"))
total_horas = int(input("total de horas trabalhadas: "))
sal_bruto = vhora * total_horas

if sal_bruto <= 900:
    IR = 0
    aliquota = 0
elif sal_bruto <= 1500:
    IR = sal_bruto * 0.05
    aliquota = 5
elif sal_bruto <= 2500:
    IR = sal_bruto * 0.1
    aliquota = 10
else:
    IR = sal_bruto *  0.2
    aliquota = 20

INSS = sal_bruto * 0.1
FGTS = sal_bruto * 0.11
imposto_sindical = sal_bruto * 0.03

total_desconto = IR + INSS

sal_liquido = sal_bruto - total_desconto

print("salario bruto: (",vhora, "*", total_horas, "): r$", sal_bruto)
print("(-) IR (",aliquota, "%)                      :R$", IR )
print("(-) INSS (10%)                               :R$", INSS)
print("FGTS (11%)                                   :R$", FGTS)
print("Total de Descontos                           :R$", total_desconto)
print("Salário Liquido                              :R$", sal_liquido)
