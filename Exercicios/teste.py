nome=input("digite o seu nome:\n")

nota1=float(input("digite a primeira nota:\n"))

nota2=float(input("digite a primeira nota:\n"))

media=float(nota1+nota2)/2
if(media==10):
    print("Aprovado com sucesso")
elif(media>=7 and media<10):
        print("Aprovado")
else:
            print("Reprovado")

print("o nome é:",nome,"a primeira nota é:",nota1,"a segunda nota é:",nota2,
      "a media do aluno(a) foi:",media)


