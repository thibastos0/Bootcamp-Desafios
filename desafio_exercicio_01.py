# Programa que calcule e imprima o salário a ser transferido para um funcionário.
# Deve receber o valor bruto do salário e o adicional dos benefícios
# O cálculo deve ser da seguinte maneira:
# (valor bruto do salário - percentual de imposto mediante ao salário + adicional dos benefícios)
# Pecentual de imposto segue as alíquotas:
# De R$ 0,00 a R$ 1100,00 = 5,00%
# De R$ 1100,00 a R$ 2500,00 = 10,00%
# Maior que R$ 2500 = 15%
# Entradas: Valor bruto do salário e adicional de benefícios
# Saída é o salário calculado

salario_bruto = float(input("Informe o salário bruto do salário do empregado: "))

beneficios = float(input("Informe o valor total dos benefícios do empregado: "))

imposto = 0

if 0 < salario_bruto <= 1100:
    imposto = 0.05
elif 1100 < salario_bruto <= 2500:
    imposto = 0.15
else:
    imposto = 0.15

salario_liquido = salario_bruto - (imposto*salario_bruto) + beneficios

print(f"""
===============Folha de Pagamento================
*********** Salário bruto ->     R$ {salario_bruto:.2f}
******** Imposto = {imposto*100:.2f}% ->   - R$ {imposto*salario_bruto:.2f}
Valor total de benefícios ->     R$ {beneficios:.2f}
-------------------------------------------------

********* Salário líquido ->     R$ {salario_liquido:.2f}

=================================================
""")
