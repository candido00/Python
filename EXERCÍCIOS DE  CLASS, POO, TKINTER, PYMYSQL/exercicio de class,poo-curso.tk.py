import tkinter
import pymysql

#conexao do banco
conexao = pymysql.connect(host='localhost',port=3306,user='root',passwd='',db='empresa')
cursor = conexao.cursor()

janela = tkinter.Tk()
janela.geometry("400x400")

titulo = tkinter.Label(janela,text="Curso")
titulo.grid(column=0,row=0, columnspan=5)

listaLabel = tkinter.Label(janela,text="Escolha uma Listagem")
listaLabel.grid(column=0, row=1, sticky="w", columnspan=5)

lista = tkinter.StringVar()
opcoesSelect=["cursos","turmas","disciplinas"]
lista.set(" Escolha ")
listaoption=tkinter.OptionMenu(janela,lista,*opcoesSelect)
listaoption.grid(column=0, row=2, columnspan=5)

btOk = tkinter.Button(janela,text="ok", width="3")
btOk.grid(column=1,row=3,columnspan=8)

titulo = tkinter.Label(janela,text="Pesquise um Aluno")
titulo.grid(column=0,row=4, columnspan=5)

matentry=tkinter.Entry(janela)
matentry.grid(column=0,row=5,columnspan=5)

btOk = tkinter.Button(janela,text="ok", width="3")
btOk.grid(column=3,row=6,columnspan=5)

titulo = tkinter.Label(janela,text="Listagem")
titulo.grid(column=0,row=7, columnspan=2)

lista=tkinter.Listbox(janela,width="40")
lista.grid(column=0,row=8,sticky="w", columnspan=20)
