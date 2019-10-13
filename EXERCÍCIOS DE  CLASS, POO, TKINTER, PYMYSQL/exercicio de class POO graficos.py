import tkinter
janela = tkinter.Tk() #CRIA UM OBJETO DO TIPO TK
janela.geometry("400x300") #DEFINE O TAMANHO DA JANELA NO ESQUEMA X Y

titulo = tkinter.Label(janela, text = "HELLO WORD") #CRIA UM LABEL EM JANELA
titulo.pack() #ADCIONA UM TITULO A JANELA

textoinput = tkinter.Entry(janela) #CRIA O CAMPO DE ENTRADA DE TEXTO
textoinput.pack() #INSERE O CAMPO DE TEXTO NA TELA

bt = tkinter.Button(janela,text="ok",command=teste)#CRIA UM BOTAO NA INTERFACE
bt.pack()

janela.mainloop() #EXECUTA O LOOP PRINCIPAL

