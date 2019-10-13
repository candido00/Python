notas=[]
soma=0

for x in range(8):
    notas.append(float(input("digite a nota:")))
    
for i in range(len(notas)):
    soma=soma+notas[i]
    
media = (soma/len(notas))
print("a média do aluno foi = ",media)

if media>=7:
    print("aluno APROVADO")
else:
    print("aluno REPROVADO")
