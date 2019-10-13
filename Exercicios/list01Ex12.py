clientes=[]
cod=1

while cod!=0:
    dados=[]
    cod = int(input("informe o código do cliente, ou 0 para encerrar"))
    if cod!=0:
        dados.append(cod)
        dados.append(float(input("digite a altura")))
        dados.append(float(input("informe o peso")))
        clientes.append(dados)
maior=0
menor=clientes[0][1]
codMaior=0
codMenor=0
pGordo=0
pMagro=clientes[0][2]
codGordo=0
codMagro=0
sAltura=0
sPeso=0

for x in range(0,len(clientes)):
    if clientes[x][1]>maior:
        maior=clientes[x][1]
        codMaior=clientes[x][0]
    if clientes[x][1]<menor:
        menor=clientes[x][1]
        codMenor=clientes[x][0]
    if clientes[x][2]>pGordo:
        pGordo=clientes[x][2]
        codGordo=clientes[x][0]
    if clientes[x][2]<pMagro:
        pMagro=clientes[x][2]
        codMagro=clientes[x][0]
    sAltura += clientes[x][1]
    sPeso += clientes[x][2]
    
print("maior = ", codMaior, "com ",maior,"m de Altura")
print("menor = ", codMenor, "com ",menor,"m de Altura")
print("mais gordo = ", codGordo," pesando ",pGordo,"kg")
print("mais magro = ", codMagro," pesando ",pMagro,"kg")
print("Altura Média = ", sAltura/len(clientes))
print("Peso Médio = ", sPeso/len(clientes))
