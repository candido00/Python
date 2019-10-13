import tkinter
from tkinter import *
import pymysql


def EntradaDiaria():
    janela = tkinter.Tk()
    janela.geometry("300x300")

    titulo = tkinter.Label(janela, text="ENTRADA DIARIA")
    titulo.grid(row=0, column=3,columnspan=5)

    frameentrada = tkinter.LabelFrame(janela, text="ENTRADA")
    frameentrada.grid(row=1,column=0,columnspan=5,sticky="w")
    
    #================================CAMPO DO NOME==============================
    nomelabel = tkinter.Label(frameentrada, text="NOME:")
    nomelabel.grid(row=2,column=0,columnspan=5,sticky="w")
    nomeentry = tkinter.Entry(frameentrada)
    nomeentry.grid(row=2,column=5,columnspan=5,sticky="w")
    #================================VALOR======================================

    valorlabel = tkinter.Label(frameentrada, text="VALOR(R$):")
    valorlabel.grid(row=3,column=0,columnspan=5,sticky="w")
    valorentry = tkinter.Entry(frameentrada)
    valorentry.grid(row=3,column=5,columnspan=5,sticky="w")
    #=================================DIA=======================================

    dialabel = tkinter.Label(frameentrada, text="DIA:")
    dialabel.grid(row=4,column=0,columnspan=5,sticky="w")
    diaentry = tkinter.Entry(frameentrada)
    diaentry.grid(row=4,column=5,columnspan=5,sticky="w")
    #=================================MES=======================================

    meslabel = tkinter.Label(frameentrada, text="MÊS:")
    meslabel.grid(row=5,column=0,columnspan=5,sticky="w")
    mesentry = tkinter.Entry(frameentrada)
    mesentry.grid(row=5,column=5,columnspan=5,sticky="w")
    #=================================ANO=======================================

    anolabel = tkinter.Label(frameentrada, text="ANO:")
    anolabel.grid(row=6,column=0,columnspan=5,sticky="w")
    anoentry = tkinter.Entry(frameentrada)
    anoentry.grid(row=6,column=5,columnspan=5,sticky="w")
    
    
    def inserir():
            conexao = pymysql.connect(host='localhost',port=3306,user='root',passwd='',db='financeiro')
            cursor = conexao.cursor()
            nome=nomeentry.get()
            valor=valorentry.get()
            dia=diaentry.get()
            mes=mesentry.get()
            ano=anoentry.get()

            consulta="INSERT INTO `entrada` VALUES('"+nome+"','"+valor+"','"+dia+"','"+mes+"','"+ano+"')"
            print(consulta)
            cursor.execute(consulta)
            conexao.commit()
            
            cursor.close()
            conexao.close()
            pass
    pass

                


    botaook=tkinter.Button(janela,text="Confirmar",command=inserir,width="26")
    botaook.grid(row=7,column=1,columnspan=5)

       
pass
    


def SaidaDiaria():
    janela = tkinter.Tk() 
    janela.geometry("300x300")

    titulo = tkinter.Label(janela, text="SAIDA DIARIA")
    titulo.grid(row=0, column=3,columnspan=5)

    framesaida = tkinter.LabelFrame(janela, text="SAIDA")
    framesaida.grid(row=1,column=0,columnspan=5,sticky="w")
    #================================CAMPO DO NOME==============================
    
    nome2label = tkinter.Label(framesaida, text="NOME:")
    nome2label.grid(row=2,column=0,columnspan=5,sticky="w")
    nome2entry = tkinter.Entry(framesaida)
    nome2entry.grid(row=2,column=5,columnspan=5,sticky="w")
    #================================VALOR======================================

    valor2label = tkinter.Label(framesaida, text="VALOR(R$):")
    valor2label.grid(row=3,column=0,columnspan=5,sticky="w")
    valor2entry = tkinter.Entry(framesaida)
    valor2entry.grid(row=3,column=5,columnspan=5,sticky="w")
    #=================================DIA=======================================

    dia2label = tkinter.Label(framesaida, text="DIA:")
    dia2label.grid(row=4,column=0,columnspan=5,sticky="w")
    dia2entry = tkinter.Entry(framesaida)
    dia2entry.grid(row=4,column=5,columnspan=5,sticky="w")
    #=================================MES=======================================

    mes2label = tkinter.Label(framesaida, text="MÊS:")
    mes2label.grid(row=5,column=0,columnspan=5,sticky="w")
    mes2entry = tkinter.Entry(framesaida)
    mes2entry.grid(row=5,column=5,columnspan=5,sticky="w")
    #=================================ANO=======================================

    ano2label = tkinter.Label(framesaida, text="ANO:")
    ano2label.grid(row=6,column=0,columnspan=5,sticky="w")
    ano2entry = tkinter.Entry(framesaida)
    ano2entry.grid(row=6,column=5,columnspan=5,sticky="w")
    
    def inserir2():
        
        conexao = pymysql.connect(host='localhost',port=3306,user='root',passwd='',db='financeiro')
        cursor = conexao.cursor()
        nome=nome2entry.get()
        valor=valor2entry.get()
        dia=dia2entry.get()
        mes=mes2entry.get()
        ano=ano2entry.get()

        consulta="INSERT INTO `saida` VALUES('"+nome+"','"+valor+"','"+dia+"','"+mes+"','"+ano+"')"
        print(consulta)
        cursor.execute(consulta)
        conexao.commit()
        cursor.close()
        conexao.close()
        pass
        
    pass


    botaook2=tkinter.Button(janela,text="Confirmar",command=inserir2,width="26")
    botaook2.grid(row=7,column=1,columnspan=5)

        
pass

