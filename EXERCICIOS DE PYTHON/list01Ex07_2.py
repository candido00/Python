soma = 0
vnum = []
x=int(input("Digite um número diferente de 0: \n"))

while x !=0:
    vnum.append(x)
    soma += x
    x = int(input("Digite um número diferente de 0: \n"))

maior = max(vnum)
menor = min(vnum)

print("o vetor é =", vnum)
print("o maior valor é =", maior)
print("o menor valor é =", menor)
print("o valor da soma é =", soma)
