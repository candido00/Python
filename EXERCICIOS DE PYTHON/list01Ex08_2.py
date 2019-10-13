eleitores = int(input("informe o total de eleitores: \n"))
cand1=0
cand2=0
cand3=0

for x in range(0, eleitores):
    voto = int(input("informe o número do candidato (1, 2, ou 3)"))
    if voto == 1:
        cand1+=1
    elif voto == 2:
        cand2+=1
    elif voto == 3:
        cand3+=1
    else:
        print("voto não computado")
vencedor = ""
maior=0
if cand1>cand2:
    maior = cand1
    vencedor = "candidato 01"
elif cand2>cand3:
    maior = cand3
    vencedor = "candidato 02"
else:
    maior = cand2
    vencedor = "candidato 02"
if cand1>cand3:
    maior = cand1
    vencedor = "candidato 01"
else:
    maior = cand3
    vencedor = "candidato 03"
    
print("o vencedor foi ",vencedor)
print("com o total de ",maior," votos")
