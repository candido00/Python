def escNum(n):
    for x in range(1,n+1):
        saida = ""
        for y in range(1,x+1):
            saida+=str(y)
        print(saida)

qtd = int(input("informe o número"))
escNum(qtd)
