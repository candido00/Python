import tkinter

janela = tkinter.Tk()
janela.geometry("400x400")
janela.title("calculo so imc")

titulo = tkinter.Label(janela,text="calculo imc")
titulo.pack()
#-----------------------------frame do peso------------------------------------
framepeso = tkinter.Frame(janela)
framepeso.pack()
labelpeso = tkinter.Label(framepeso,text="peso:")
labelpeso.pack(side="left")
entpeso = tkinter.Entry(framepeso)
entpeso.pack(side="right")
#------------------------------frame da altura----------------------------------
framealtura=tkinter.Frame(janela)
framealtura.pack()
labelaltura = tkinter.Label(framealtura, text = "altura")
label.altura.pack(side="left")
entaltura = tkinter.Entry(framealtura)
entaltura.pack(side="right")
#----------------------------funçao calculo imc---------------------------------
def CALCULAR():
    imc = float(entpeso.get())/float(entaltura.get())**2
    resultado.config(text= str("%.2f"%imc))
    entpeso.delete(0"end")
    entaltura.delete(0"end")
    pass
#-----------------------------------botao---------------------------------------
framebt = tkinter.Frame(janela)
framebt.pack()

bt = tkinter.Button(framebt,text="calcular",command=CALCULAR)

#-------------------------------Label de Resultado------------------------------                  

resultado= tkinter.Label(janela,text="")
resultado.pack()                  





