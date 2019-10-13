fact = 1
num = int(input("DIGITE UM NUMERO PARA FATORAR: "))
while(num > 0):
    print(num,"X " if num > 1 else "= ",end="")
    fact *= num
    num -= 1
print(fact)
