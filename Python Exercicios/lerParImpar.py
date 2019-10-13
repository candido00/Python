num = int
numeros = []
count1 = 0
count2 = 0
while(num != -1):
    num = int(input("INFORME UM NUMERO OU( -1 ) PARA ENCERRAR: "))
    numeros.append(num)
for x in(numeros):
    if(x % 2 == 0 and x != 0):
        count1 += 1
    elif(x % 2 !=0 and x != -1):
        count2 += 1
print("PARES: ",count1)
print("IMPARES: ",count2)
        
