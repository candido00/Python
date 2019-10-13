vHora = float(input("informe o valor da sua hora"))
qtdHoras = int(input("informe a quantidade de horas trabalhadas por sua pessoa"))
salario = vHora*qtdHoras
print(salario)
ir = salario*0.11
print(ir)
inss = salario*0.08
print(inss)
sindicato = salario*0.05
print(sindicato)
sLiquido = salario-ir-inss-sindicato
print(sLiquido)
