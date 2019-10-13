num1 = [1,2,3,4,5,6,7,8]
num2 = [3,2,4,7,9,5,1,6]
num3 = [[3,2,4,7,9,5,1,6],[3,2,4,7,9,5,1,6]]
nome = ["jademir ","de ","moura "]

#concatenando nomes em um array de strings
nomePrint =""
for x in nome:
    nomePrint+=x
print(nomePrint)

#somando os arrays
print(sum(num3[0])+sum(num3[1])) #soma de matrizes
print("Arrays------------------")
print(num1)
print(num2)
print("------- soma dos itens dos array ------")
print(sum(num1)+sum(num2))

soma=0
print("------ somatório dos itens detalhados------")
print("------ Array 1------")
for x in range(0,len(num1)):
    print(soma,"+",num1[x]," = ",soma+num1[x])
    soma+=num1[x]
print("------ Array 2------")
for x in range(0,len(num2)):
    print(soma,"+",num2[x]," = ",soma+num2[x])
    soma+=num2[x]

