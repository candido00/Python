import tkinter

janela = tkinter.Tk()
janela.geometry("400x500")

titulo= tkinter.Label(janela, text= "calculadora do prejuizo")
titulo.pack()

frameinserir= tkinter.Frame(janela)
frameinserir.pack()

taxaLabel= tkinter.Label(frameinserir,text="  Taxa  de  Juros:")
taxaLabel.pack(side="left")

InserirEntry1= tkinter.Entry(frameinserir)
InserirEntry1.pack(side="right")

#-------------------------------------------------------------------------------

frameinserir= tkinter.Frame(janela)
frameinserir.pack()

textLabel= tkinter.Label(frameinserir,text="Valor Solicitado:")
textLabel.pack(side="left")

InserirEntry2= tkinter.Entry(frameinserir)
InserirEntry2.pack(side="right")

#-------------------------------------------------------------------------------

frameinserir= tkinter.Frame(janela)
frameinserir.pack()

textLabel= tkinter.Label(frameinserir,text="       Nº Parcelas:")
textLabel.pack(side="left")

InserirEntry3= tkinter.Entry(frameinserir)
InserirEntry3.pack(side="right")
#------------------------------------------------------------------------------

def TAXAJUROS():
    float(InserirEntry.get()/100)
    pass

def VALORSOLICITADO():
    float(InserirEntry2.get())
    pass

def NPARCELAS():
    float(InserirEntry3.get())
    pass

def CALCULAR():
    taxa=float(InserirEntry1.get())/100*float(InserirEntry2.get())
    valortotal= float(InserirEntry2.get())+taxa
    parcelas= float(valortotal/(float(InserirEntry3.get())))
    texto=("Resultado: \n Valor total: ",valortotal,"\n Parcela de: ",parcelas)
    text.insert("insert",texto)
    pass
    
#-------------------------------------------------------------------------------

frameinserir= tkinter.Frame(janela)
frameinserir.pack()

botao= tkinter.Button(frameinserir,text="Calcular",command=CALCULAR)
botao.pack(side="right")


text= tkinter.Text(janela)
text.pack()


