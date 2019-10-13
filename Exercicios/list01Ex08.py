eleitores = int(input("informe o total de eleitores: \n"))
candidatos = [["candidato 01",0],["candidato 02",0],["candidato 03",0]]

for x in range(0, eleitores):
    voto = int(input("informe o número do candidato (1, 2, ou 3)"))
    if voto == 1:
        candidatos[0][1]+=1
    elif voto == 2:
        candidatos[1][1]+=1
    elif voto == 3:
        candidatos[2][1]+=1
    else:
        print("voto não computado")
vencedor = ""
maior=0
for i in range(len(candidatos)):
    if candidatos[i][1]>maior:
        maior = candidatos[i][1]
        vencedor = candidatos[i][0]
print("o vencedor foi ",vencedor)
print("com o total de ",maior," votos")
