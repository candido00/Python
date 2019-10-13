import tkinter #importando o tkinter

janela = tkinter.Tk() #instanciando o objeto da classe TK
janela.geometry("400x300")#definindo o tamanho da janela
janela.title("Cálculo do IMC") #alterando o texto da barra de titulos da janela

titulo = tkinter.Label(janela,text = "Cálculo IMC")#inserindo o título da página
titulo.pack()
#---------------------- Frame do Peso ----------------------------
framePeso = tkinter.Frame(janela)#criando o frame para os dados do peso
framePeso.pack()#inserindo o frame na página
labelPeso = tkinter.Label(framePeso,text="Peso: ")#criando um label para o peso
#e colocando ele no framePeso ao inves da janela, dessa forma colocamos o Frame
#como "pai" do elemento"""
labelPeso.pack(side="left")#Inserindo o label na tela, e, definindo o alinhamento
entPeso = tkinter.Entry(framePeso)#criando a entrada para o valor do peso e colocando no frame
entPeso.pack(side="right")#inserindo a entrada na página, e, definindo o alinhamento no frame

#----------------------- Frame da altura --------------------------
frameAltura = tkinter.Frame(janela)
frameAltura.pack()

labelAltura = tkinter.Label(frameAltura, text = "Altura: ")
labelAltura.pack(side="left")

entAltura = tkinter.Entry(frameAltura)
entAltura.pack(side="right")

#----------------------- Função calculo IMC --------------------------
def calcular():
    imc = float(entPeso.get())/float(entAltura.get())**2 #calcula o IMC
    resultado.config(text=str("%.2f"%imc))#exibe o resultado no label resultado
    entPeso.delete(0,"end")#zera o valor do campo Peso
    entAltura.delete(0,"end")#zera o valor do campo Altura
    pass

#--------------------------- Botão ----------------------------------
frameBt = tkinter.Frame(janela)#cria o frame do botão
frameBt.pack()#insere o frame do botão na página

bt = tkinter.Button(frameBt,text="Calcular",command=calcular)#cria o botão que chama a função
bt.pack() #insere o botão na janela

#-------------------------- Label de Resultado ---------------------
resultado = tkinter.Label(janela, text="")#cria a label para exibir o resultado
resultado.pack()#insere a label na janela


