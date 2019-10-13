import tkinter as tk
import pymysql
from tkinter import *
from modules import Janela

janela = tk.Tk()
janela.geometry("600x600")

titulo=tk.Label(janela, text="Controle de Estoque\n")
titulo.grid( row=0,column=0,columnspan=5)

#-------------------------------------------------------------------------------

frame=tk.Frame(janela)
frame.grid(row=1, column=0, columnspan=1)

#-------------------------------------------------------------------------------

botao=tk.Button(frame , text="Adicionar",width="16", command=Janela.OpenJanela)
botao.grid(row=0,column=0)

botao2=tk.Button(frame , text="Atualizar",width="16")
botao2.grid(row=0,column=1)

botao3=tk.Button(frame , text="Pesquisar",width="16")
botao3.grid(row=0,column=2)

botao4=tk.Button(frame , text="Excluir",width="16")
botao4.grid(row=0,column=3)

#-------------------------------------------------------------------------------

texto=tk.Text(janela)
texto.grid(row=2,column=0,columnspan=25)

#-------------------------------------------------------------------------------
 



