def valorPagamento(vPrest,dAtraso):
    if dAtraso!=0:
        return (vPrest+(vPrest*0.03)+(vPrest*0.001*dAtraso))
    else:
        return (vPrest)

prest = 1
valores = []
while prest !=0:
    prest = int(input("informe o valor da prestação"))
    dias = 0
    if prest !=0:
        dias = int(input("informe a quantidade de dias atrasados"))
        valores.append(valorPagamento(prest,dias))
        print(valorPagamento(prest,dias))
    else:
        print("obrigado por utilizar nosso sistema!")
print("------------ Relatório do dia -------------")
totalDia = 0
for i in range(0,len(valores)):
    totalDia += valores[i]
print("foram feitos ",len(valores)," pagamentos com valor total = ",totalDia)
