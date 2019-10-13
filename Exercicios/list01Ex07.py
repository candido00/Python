soma = 0
vnum = []
x=int(input("Digite um número diferente de 0: \n"))

while x !=0:
    vnum.append(x)
    x = int(input("Digite um número diferente de 0: \n"))

maior = vnum[0]
menor = vnum[0]

for i in range(0,len(vnum)):
    if vnum[i]>maior:
        maior = vnum[i]

    if vnum[i]<menor:
        menor = vnum[i]
    soma += vnum[i]
print("o vetor é =", vnum)
print("o maior valor é =", maior)
print("o menor valor é =", menor)
print("o valor da soma é =", soma)
vpalavras = ["laksjdlçfkjasçldkjfçlasd","kjslafk","kasjldfjlsdkfj"]
print(max(vpalavras))
print(min(vpalavras))
