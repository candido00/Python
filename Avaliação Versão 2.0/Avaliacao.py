import tkinter as tk
from tkinter import *
from modules import Janela
import pymysql


janela = tk.Tk()
janela.geometry("400x400")

titulo = tk.Label(janela,text="Controle de Estoque")
titulo.grid(row=0, column=0,columnspan=4)

frameSelect = tk.LabelFrame(janela,text="Escolha uma Função")
frameSelect.grid(column=0,row=1,sticky="w",columnspan=4)

#================PESQUISA====================
framePesquisar = tk.LabelFrame(janela,text="Pesquisa de Produtos")
framePesquisar.grid(column=0,row=2,columnspan=4)
                #NOME
nomeLabel = tk.Label(framePesquisar,text="Nome")
nomeLabel.grid(column=0, row=2, sticky="w", columnspan=2)
nomeEntry = tk.Entry(framePesquisar)
nomeEntry.grid(column=1, row=2, columnspan=2)
                #CODIGO
codLabel = tk.Label(framePesquisar,text="Código")
codLabel.grid(column=0, row=3, sticky="w", columnspan=2)
codEntry = tk.Entry(framePesquisar)
codEntry.grid(column=1, row=3, columnspan=2)

#=================FRAME LISTA===============

frameResultado = tk.LabelFrame(janela,text="Resultado da Pesquisa")
frameResultado.grid(row=4,column=0,columnspan=4)
resultado = tk.Listbox(frameResultado,width="40")
resultado.grid(row=5,column=0)


def pesquisar():
    #conexao do banco
    conexao = pymysql.connect(host='localhost',port=3306,user='root',passwd='',db='controle')
    cursor = conexao.cursor()
    
    codigo = codEntry.get()
    nom = nomeEntry.get()
    if (codigo != ""):
        consulta = "SELECT codigo,nome,quantidade FROM produto WHERE codigo = "+codigo
        resultado.delete(0,"end")
        print(consulta)
        cursor.execute(consulta)
        for i in cursor:
            texto = str(i[0])+" - "+i[1]+" - "+str(i[2])
            resultado.insert(1,texto)
    elif (nom !="" or nom == None):
        conexao = pymysql.connect(host='localhost',port=3306,user='root',passwd='',db='controle')
        cursor = conexao.cursor()

        consulta = "SELECT codigo,nome,quantidade FROM produto WHERE nome = '"+nom+"'"
        resultado.delete(0,"end")
        print(consulta)
        cursor.execute(consulta)
        for i in cursor:
            texto = str(i[0])+" - "+i[1]+" - "+str(i[2])
            resultado.insert(1,texto)
     
    else:
        consulta = "SELECT codigo,nome,quantidade FROM produto"
        resultado.delete(0,"end")
        print(consulta)
        cursor.execute(consulta)
        for i in cursor:
            texto = str(i[0])+" - "+i[1]+" - "+str(i[2])
            resultado.insert(1,texto)
    
    
       
    pass












#========================Botoes=========================================
btED = tk.Button(frameSelect, text="Cadastrar",width="10",command=Janela.OpenCadastrar)
btED.grid(row=1,column=0,columnspan=2)

btEX = tk.Button(frameSelect,text="Excluir",width="10",command=Janela.OpenExcluir)
btEX.grid(row=1,column=2,columnspan=2) 

btIN = tk.Button(frameSelect,text="Editar",command=Janela.OpenEditar,width="10")
btIN.grid(row=1,column=4,columnspan=2) 

btPQ = tk.Button(framePesquisar,text="Pesquisar",command=pesquisar,width="25")
btPQ.grid(row=6,column=2,columnspan=1)

janela.mainloop()
