num = int(input("digite um número"))
total = 1
for x in range(num,1,-1):
    total = x*total
    print("x = ",x,"total = ",total)
print (total)
