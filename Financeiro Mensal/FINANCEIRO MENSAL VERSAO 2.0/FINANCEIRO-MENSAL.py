import tkinter
from tkinter import *
from MODULOS import JANELA
import pymysql

janela = tkinter.Tk()
janela.geometry("570x500")

titulo = tkinter.Label(janela,text="FINANCEIRO MENSAL")
titulo.grid(row=0,column=5,columnspan=5)

frameentrada = tkinter.LabelFrame(janela,text="ENTRADA")
frameentrada.grid(row=1,column=0,columnspan=5)


framesaida = tkinter.LabelFrame(janela,text="SAIDA")
framesaida.grid(row=3,column=0)


#----------------------------LISTBOX--------------------------------------------

framesaldo = tkinter.LabelFrame(janela,text="SALDO TOTAL")
framesaldo.grid(row=5,column=0,columnspan=5)
resultado= tkinter.Listbox(framesaldo,width="40")
resultado.grid(row=6,column=0,columnspan=5)

#-----------------------------pesquisa-saldo------------------------------------

def saldo():
    conexao = pymysql.connect(host='localhost',port=3306,user='root',passwd='',db='financeiro')
    cursor = conexao.cursor()
    consulta="SELECT SUM(valor) FROM entrada"
    resultado.delete(0,"end")
    teste = cursor.execute(consulta)
    print(teste)
    texto=str (consulta)
    resultado.insert(0,teste)

    pass
pass
    
    
        



#---------------------------------LINHA-BOTOES----------------------------------
botaoentrada = tkinter.Button(frameentrada,text="Entrada Diaria",command=JANELA.EntradaDiaria,width="33")
botaoentrada.grid(row=2,column=0,columnspan=5)

botaosaida = tkinter.Button(framesaida,text="Saida Diaria",command=JANELA.SaidaDiaria,width="33")
botaosaida.grid(row=4,column=0,columnspan=5)

botaosaldo = tkinter.Button(framesaldo,text="Saldo",command=saldo,width="33")
botaosaldo.grid(row=5,column=0,columnspan=5)

janela.mainloop()
