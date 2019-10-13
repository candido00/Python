num = 1
den = 1
soma = 1
count = 1
print(num,den,end="--1")
print("")
while(num < 99 and den < 50):
    count += 1
    num += 2
    den += 1
    divi = (num + num )/(den + den)
    soma = soma + divi
    print(num,den,end="--")
    #print(divi)
    #print(count,end="--")
    print(soma)
