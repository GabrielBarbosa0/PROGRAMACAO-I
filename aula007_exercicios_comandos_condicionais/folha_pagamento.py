# Faça um programa para o cálculo de uma folha de pagamento, sabendo que os descontos 
# são do Imposto de Renda, que depende do salário bruto (conforme alíquotas abaixo) e 3% 
# para o Sindicato e que o FGTS corresponde a 11% do Salário Bruto, mas não é descontado (é 
# a empresa que deposita). O Salário Líquido corresponde ao Salário Bruto menos os 
# descontos. O programa deverá pedir ao usuário o valor da sua hora e a quantidade de horas 
# trabalhadas no mês.

valor_hora = float(input("Digite o valor da sua hora: "))
quantidade_horas = float(input("Digite a quantidade de horas trabalhadas: "))
salario_bruto = valor_hora * quantidade_horas

ir = 0

if salario_bruto <= 900: ir = 0
elif salario_bruto > 900 and salario_bruto <= 1500: ir = salario_bruto * 0.05
elif salario_bruto > 1500 and salario_bruto <= 2500: ir = salario_bruto * 0.10
else: ir = salario_bruto * 0.20

inss = salario_bruto * 0.10
sindicato = salario_bruto * 0.03
fgts = salario_bruto * 0.11
total_descontos = ir + inss + sindicato
salario_liquido = salario_bruto - total_descontos

print("Salário bruto: ", "R$ ", salario_bruto)
print("IR: ", "R$ ", ir)
print("INSS (10%): ", "R$ ", inss)
print("Sindicato (3%): ", "R$ ", sindicato)
print("FGTS (11%): ", "R$ ", fgts)
print("Total de descontos: ", "R$ ", total_descontos)
print("Salário líquido: ", "R$ ", salario_liquido)
