#Criação da função
def media(a,b):
    return (a+b)/2

#iniciando o array vazio, para guardar os alunos"""
alunos = []

#laço que solicita os dados dos alunos
while True:
    #iniciando o array pra guardar CADA ALUNO CRIADO!!!
    aluno=[]
    #insere o nome do aluno na próxima posição vazia (como o array está vazio, fica sempre na [0])
    aluno.append(input("Digite o nome do aluno, ou 0 para encerrar"))
    #verifica se foi digitado 0 para encerrar o laço
    if aluno[0] == "0":
        break #encerra o laço
    #adiciona as notas dos alunos no array aluno
    aluno.append(float(input("Digite a primeira nota")))
    aluno.append(float(input("Digite a segunda nota")))
    #insere o aluno digitado ao array principal "alunos"
    alunos.append(aluno)

#laço para escrever todos os alunos com suas médias, chamando a função media()
for i in range(0,len(alunos)):
    print("A média do aluno ",alunos[i][0]," foi = ",media(alunos[i][1],alunos[i][2]))
