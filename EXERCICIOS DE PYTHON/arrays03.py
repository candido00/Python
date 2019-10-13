compra=[]
parar = ""
soma=0

while parar!="s":
    item= []
    item.append(input("informe o nome do produto: \n"))
    item.append(float(input("informe o preço do produto: \n")))
    item.append(int(input("informe a quantidade do produto: \n")))
    compra.append(item)
    parar = input("digite S para finalizar")

for x in range(len(compra)):
    print ("total do item",compra[x][0]," = R$",compra[x][1]*compra[x][2])
    soma +=(compra[x][1]*compra[x][2])
print("o Valor total da compra foi: R$",soma)
