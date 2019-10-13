#Declaração das funções das 4 operações matemáticas
def soma(a,b):
    return a+b
def sub(a,b):
    return a-b
def mult(a,b):
    return a*b
def div(a,b):
    return a/b

operador = ""
num = int
valorAtual = float(input("informe um número \n"))
#solicitar ao usuário o cálculo
while True:
    #verifica qual o operador informado para executar a função correspondente
    if operador == "+":
        valorAtual = soma(valorAtual,num)
    elif operador == "-":
        valorAtual = sub(valorAtual,num)
    elif operador == "*":
        valorAtual = mult(valorAtual,num)
    elif operador == "/":
        valorAtual = div(valorAtual,num)
    print(valorAtual) #printa o valor a cada laço

    operador = input("informe o operador, digite = para encerrar")
    #verifica se o operador informado é "=" para encerrar o programa
    if operador == "=":
        break #quebra a execução do laço
    num = float(input("informe um número\n"))



