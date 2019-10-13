import tkinter as tk
from tkinter import *

def OpenJanela():
    janela = tk.Tk()
    janela.geometry("400x400")

    titulo=tk.Label(janela, text="Adicionar Produtos\n")
    titulo.grid(row=0,column=0,columnspan=5)

    frame=tk.Frame(janela)
    frame.grid(row=1, column=0, columnspan=1)

    Entry = tk.Entry(janela)
    Entry.grid(row=1,column=0,columnspan=2)

    

    



    
    
