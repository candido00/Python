term1 = 0
term2 = 1
count = 3
num = int(input("INFORME UM NUMERO PARA A SEQUENCIA: "))
termos = []
termos.append(0)
termos.append(1)
while(count <=  num):
    term3 = term1 + term2
    termos.append(term3)
    term1 = term2
    term2 = term3
    count += 1
print(termos)
