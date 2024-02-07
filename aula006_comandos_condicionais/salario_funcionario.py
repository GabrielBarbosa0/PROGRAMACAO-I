# Uma empresa concederá um aumento de salário aos seus funcionários, variável de acordo com o cargo, conforme a tabela abaixo. Faça um programa que leia o salário e o código do cargo de um funcionário e calcule o seu novo salário. Se o cargo do funcionário não estiver na tabela, ele deverá, então, receber 15% de aumento. Mostre o salário antigo, o novo salário e a diferença entre ambos.

codigo_cargo = int(input("Digite o codigo do seu cargo: "))

salario = int(input("Digite seu salario atual: "))

if codigo_cargo == 310: print((salario * 0.05) + salario)
elif codigo_cargo == 456: print((salario * 0.07) + salario)
elif codigo_cargo == 885: print((salario * 0.10) + salario)
else: print((salario * 0.15) + salario)