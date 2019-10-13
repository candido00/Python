import tkinter as tk
from tkinter import *
import pymysql


def OpenCadastrar():
    janela = tk.Tk()
    janela.geometry("250x300")

    titulo=tk.Label(janela, text="Cadastro de Produto")
    titulo.grid(row=0,column=3,columnspan=5)

    frameProduto = tk.LabelFrame(janela,text="Produto")
    frameProduto.grid(column=0,row=1,sticky="w",columnspan=4)

    #===================CAMPO DO CODIGO============================
    idLabel = tk.Label(frameProduto,text="Código")
    idLabel.grid(row=2,column=0,columnspan=2,sticky="w")
    idEntry = tk.Entry(frameProduto)
    idEntry.grid(column=3,row=2,columnspan=2,sticky="w")
    
    #====================NOME====================================
    nomeLabel = tk.Label(frameProduto,text="Nome")
    nomeLabel.grid(row=3,column=0,columnspan=2,sticky="w")
    nomeEntry = tk.Entry(frameProduto)
    nomeEntry.grid(column=3,row=3,columnspan=2,sticky="w")
    
    #==================QUANTIDADE============================
    qtdLabel = tk.Label(frameProduto, text="Quantidade")
    qtdLabel.grid(row=4,column=0,columnspan=2,sticky="w")
    qtdEntry = tk.Entry(frameProduto)
    qtdEntry.grid(row=4,column=3,columnspan=2,sticky="w")
    
    #=====================DESCRIÇÃO==========================
    descLabel = tk.Label(frameProduto, text="Descrição")
    descLabel.grid(row=5,column=0,columnspan=2,sticky="w")
    descEntry = tk.Entry(frameProduto)
    descEntry.grid(row=5,column=3,columnspan=2,sticky="w")
    
    #=======================FORNECEDOR========================
    forLabel = tk.Label(frameProduto, text="Fornecedor")
    forLabel.grid(row=6,column=0,columnspan=2,sticky="w")

    conexao = pymysql.connect(host='localhost',port=3306,user='root',passwd='',db='controle')
    cursor  = conexao.cursor()
    query = "SELECT id,nome FROM fornecedor"
    cursor.execute(query)

    funcao = tk.StringVar()
    opcoesFuncao = []
    dicFuncao = {}
    #preencher o array com os valores do banco
    for i in cursor:
        opcoesFuncao.append(i[1])
        dicFuncao[i[1]]=i[0]

    funcao.set(".")
    funcaoOption = tk.OptionMenu(frameProduto,funcao,*opcoesFuncao)
    funcaoOption.grid(row=6,column=3,columnspan=3)

    
    def inserir():
        if(funcao.get()!="."):
            conexao = pymysql.connect(host='localhost',port=3306,user='root',passwd='',db='controle')
            cursor = conexao.cursor()
            cod = idEntry.get()
            nome = nomeEntry.get()
            qtd = qtdEntry.get()
            idFornecedor = dicFuncao[funcao.get()]
            desc = descEntry.get()
            
            query = "INSERT INTO `produto` VALUES ('"+cod+"','"+nome+"',"+qtd+",'"+desc+"',"+str(idFornecedor)+")"
            print(query)
            cursor.execute(query)
            conexao.commit()
            pass
            
        pass



    btOk = tk.Button(janela,text="CONFIRMAR",command=inserir, width="16")
    btOk.grid(row=7,column=1,columnspan=2)

    cursor.close()
    conexao.close()

pass

def OpenExcluir():
    janela = tk.Tk()
    janela.geometry("250x300")

    titulo=tk.Label(janela, text="Excluir Produto")
    titulo.grid(row=0,column=2,columnspan=5)

    frameExcluir = tk.LabelFrame(janela,text="Produto")
    frameExcluir.grid(column=0,row=1,sticky="w",columnspan=4)

    #===================CAMPO DO CODIGO============================
    idLabel = tk.Label(frameExcluir,text="Código do Produto")
    idLabel.grid(row=2,column=0,columnspan=2,sticky="w")
    idEntry = tk.Entry(frameExcluir)
    idEntry.grid(column=3,row=2,columnspan=2)
    #------------------ Area de listagens ----------------
    frameLista = tk.LabelFrame(janela,text="Consulta")
    frameLista.grid(column=0, row=4,sticky="w",columnspan=4)

    lista = tk.Listbox(frameLista, width="40")
    lista.grid(column=0, row=0,sticky="w", columnspan=4)

    conexao = pymysql.connect(host='localhost',port=3306,user='root',passwd='',db='controle')
    cursor  = conexao.cursor()
    
    
    def Consultar():
        conexao = pymysql.connect(host='localhost',port=3306,user='root',passwd='',db='controle')
        cursor  = conexao.cursor()
        lista.delete(0,"end")
        codigo = idEntry.get()
        
        if (codigo != ""):
            consulta = "SELECT codigo,nome FROM produto WHERE codigo = "+codigo
            print(consulta)
            cursor.execute(consulta)
            for i in cursor: 
                texto = str(i[0])+" - "+i[1]
                lista.insert(i[0],texto)
        
        pass
    pass
    
    def Excluir():
       conexao = pymysql.connect(host='localhost',port=3306,user='root',passwd='',db='controle')
       cursor  = conexao.cursor()
       lista.delete(0,"end")
       delete = idEntry.get()
       consulta = "DELETE FROM produto WHERE produto.codigo = "+delete
       print(consulta)
       cursor.execute(consulta)
       conexao.commit()
           
       pass
    pass
       
      

    btC = tk.Button(janela,text="Consultar Item",command=Consultar,width="29")
    btC.grid(row=3,column=1,columnspan=2)
             
    btEx = tk.Button(janela,text="Excluir",command=Excluir,width="29")
    btEx.grid(row=5,column=1,columnspan=2)

    cursor.close()
    conexao.close()


    
