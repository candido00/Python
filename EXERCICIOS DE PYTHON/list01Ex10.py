while True:
    valor=10000
    vProdutos=[]
    soma = 0

    while valor!=0:
        valor = float(input("digite o valor do Item, ou 0 para encerrar"))
        if valor!=0:
            vProdutos.append(valor)

    print("\n--------Total da Compra--------\n")
    for x in range(0,len(vProdutos)):
        print("produto",x+1, " R$",vProdutos[x])
        soma+=vProdutos[x]
    print("O valor total da compra foi R$",soma)

    valor = float(input("Informe o valor pago pelo cliente"))
    print(" o troco é igual a R$",valor-soma)
