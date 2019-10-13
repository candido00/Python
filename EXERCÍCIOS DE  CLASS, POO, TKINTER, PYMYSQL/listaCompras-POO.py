import tkinter

janela = tkinter.Tk() #cria um objeto do tipo Tk
janela.geometry("400x600") #define o tamanho da janela no esquema X Y

titulo = tkinter.Label(janela, text="Lista de Compras") #cria um label em Janela
titulo.pack()#adiciona o título à janela

frameInserir = tkinter.Frame(janela)
frameInserir.pack()

nomeItem = tkinter.Label(frameInserir, text="Novo Item:")
nomeItem.pack(side="left")

itemEntry = tkinter.Entry(frameInserir)#cria o campo de entrada de texto
itemEntry.pack(side="left")#insere o campo de texto na tela


listaItens = []
def add():
    listaItens.append(itemEntry.get())
    listagem.insert("insert",(str(len(listaItens))+"-"+itemEntry.get()+"\n"))
    itemEntry.delete(0,"end")
    pass


bt = tkinter.Button(frameInserir,text="Add",command=add)#cria o botao
bt.pack(side="right")#adiciona o botão ao Frame

frameItens = tkinter.LabelFrame(janela, text="Itens:")
frameItens.pack()

listagem = tkinter.Text(frameItens)
listagem.pack()
