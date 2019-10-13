paisA=80000
paisB=200000
cont=0
while paisA<paisB:
    paisA += paisA*0.03
    print("agora o valor de A é =",paisA)
    paisB += paisB*0.015
    print("agora o valor de B é =",paisB)
    cont+=1
print("são necessários ",cont," anos para A alcançar B")
