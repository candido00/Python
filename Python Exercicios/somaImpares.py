num1 = int(input("digite um numero: "))
num2 = int(input("digite um numero: "))
soma = 0
if ( num1 % 2 == 0 ):
    num1 += 1
while (num1 <= num2 ):
    #print(" +" if num1 > 1 else "=" ,num1,end="")
    print(num1,end="+")
    soma += num1
    num1 += 2
print(" =",soma)
    
