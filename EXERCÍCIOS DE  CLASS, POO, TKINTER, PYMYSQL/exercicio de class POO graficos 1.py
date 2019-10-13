import tkinter
def TROCAR():
    titulo.config(text=textoinput.get())
    textoinput.delete(0,len(textoinput.get()))
    pass
janela = tkinter.Tk()
janela.geometry("400x300")

titulo = tkinter.Label(janela, text= "hello word")
titulo.pack()

textoinput = tkinter.Entry(janela)
textoinput.pack()

botao = tkinter.Button(janela,text="trocar texto",command= TROCAR)
botao.pack()

janela.mainloop()

