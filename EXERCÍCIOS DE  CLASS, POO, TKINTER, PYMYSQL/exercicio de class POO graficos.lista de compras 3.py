import tkinter

janela= tkinter.Tk()
janela.geometry("450x450")
janela.title("Lista de Compras")

titulo=tkinter.Label(janela,text="Lista de Compras")
titulo.pack()

frameinserir=tkinter.Frame(janela)
frameinserir.pack()

labelinserir=tkinter.Label(frameinserir, text="Inserir:")
labelinserir.pack(side="left")

entinserir=tkinter.Entry(frameinserir)
entinserir.pack(side="left")

botao=tkinter.Button(frameinserir,text="Adcionar")
botao.pack(side="right")


frameinserir2=tkinter.Text(janela)
titulo=tkinter.Label(janela,text="Itens")
titulo.pack()
frameinserir2.pack()



