# # Programa que calcule e imprima o salário a ser transferido para um funcionário.
# # Deve receber o valor bruto do salário e o adicional dos benefícios
# # O cálculo deve ser da seguinte maneira:
# # (valor bruto do salário - percentual de imposto mediante ao salário + adicional dos benefícios)
# # Pecentual de imposto segue as alíquotas:
# # De R$ 0,00 a R$ 1100,00 = 5,00%
# # De R$ 1100,00 a R$ 2500,00 = 10,00%
# # Maior que R$ 2500 = 15%
# # Entradas: Valor bruto do salário e adicional de benefícios
# # Saída é o salário calculado

salario_bruto = float(input("Informe o salário bruto do salário do empregado: "))

beneficios = float(input("Informe o valor total dos benefícios do empregado: "))

imposto = 0

if 0 < salario_bruto <= 1100:
    imposto = 0.05
elif 1100 < salario_bruto <= 2500:
    imposto = 0.10
else:
    imposto = 0.15

salario_liquido = salario_bruto - (imposto*salario_bruto) + beneficios

print(f"""
===============Folha de Pagamento================
*********** Salário bruto ->     R$ {salario_bruto:.2f}
******** Imposto = {imposto*100:5.2f}% ->   - R$ {imposto*salario_bruto:.2f}
Valor total de benefícios ->     R$ {beneficios:.2f}
-------------------------------------------------

********* Salário líquido ->     R$ {salario_liquido:.2f}

=================================================
""")

# # Exercício 01
saldo_atual = float(input("Informe o seu salto atual: R$ "))
valor_deposito = float(input("Qual o valor do depósito? R$ "))
valor_retirada = float(input("Qual o valor do saque? R$ "))

# #TODO: Calcular o saldo atualizado de acordo com a descrição deste desafio.
saldo_final = saldo_atual + valor_deposito - valor_retirada 

# #TODO: Imprimir o a saída de conforme a tabela de exemplos (uma casa decimal).
print(f"Saldo atualizado na conta: RS {saldo_final}")

# Exercício 2

ativos = []

# # Entrada da quantidade de ativos
quantidadeAtivos = int(input("Informe a quantidade de ativos: "))

# # Entrada dos códigos dos ativos
for ativo in range(quantidadeAtivos):
  codigoAtivo = input(f"Entre com a descrição do ativo de código {ativo + 1}: ")
  ativos.append(codigoAtivo)

# # TODO: Ordenar os ativos em ordem alfabética.
ativos_ordenados = ativos.sort()

# # TODO: Imprimir a lista de ativos ordenada, conforme a tabela de exemplos.
for ativo in ativos:
   print(ativo)

# # Exercício 3
# # Entrada de dados
saldo_total = int(input())
valor_saque = int(input())

# # TODO: Criar as condições necessárias para impressão da saída, vide tabela de exemplos.

if saldo_total >= valor_saque:
  saldo = saldo_total - valor_saque
  print(f"Saque realizado com sucesso. Novo saldo: {saldo}")
else:
  print("Saldo insuficiente. Saque nao realizado!")

# Exercício 4
valor_inicial = float(input())
taxa_juros = float(input())
periodo = int(input())

valor_final = valor_inicial

# # TODO: Iterar, baseado no período em anos, para calculo do valorFinal com os juros.
for ano in range(periodo):
    valor_final += valor_final*taxa_juros

print(f"Valor final do investimento: R$ {valor_final:.2f}")

# Exercício 5
valor = float(input())

if valor > 0:
#   # TODO: Imprimir a mensagem de sucesso, formatando o saldo atual (vide Exemplos).
  print("Deposito realizado com sucesso!")
  print(f"Saldo atual: R$ {valor:.2f}")
elif valor == 0:
#   # TODO: Imprimir a mensagem de valor inválido.
  print("Encerrando o programa...")
else:
#   # TODO: Imprimir a mensagem de encerrar o programa.
  print("Valor invalido! Digite um valor maior que zero.")