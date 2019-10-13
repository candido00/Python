import tkinter
import pymysql

janela = tkinter.Tk()
janela.geometry("250x300")

titulo = tkinter.Label(janela,text="Inserir Funcionário")
titulo.grid(row=0, column=0, columnspan=4)

#----------- Linha do nome---------------
nomeLabel = tkinter.Label(janela,text="Nome:")
nomeLabel.grid(column=0, row=1, sticky="w", columnspan=2)

nomeEntry = tkinter.Entry(janela)
nomeEntry.grid(column=2, row=1, columnspan=2)

#----------- Linha do email---------------
mailLabel = tkinter.Label(janela,text="email:")
mailLabel.grid(column=0, row=2, sticky="w", columnspan=2)

mailEntry = tkinter.Entry(janela)
mailEntry.grid(column=2, row=2, columnspan=2)

#----------- Linha do cpf---------------
cpfLabel = tkinter.Label(janela,text="CPF:")
cpfLabel.grid(column=0, row=3, sticky="w", columnspan=2)

cpfEntry = tkinter.Entry(janela)
cpfEntry.grid(column=2, row=3, columnspan=2)

#----------- Linha da função---------------
funcaoLabel = tkinter.Label(janela,text="Função:")
funcaoLabel.grid(column=0, row=4, sticky="w", columnspan=2)
#conexao do banco
conexao = pymysql.connect(host='localhost',port=3306,user='root',passwd='',db='empresa')
cursor = conexao.cursor()

#consulta das funções para preencher o select
query = "SELECT id,nome FROM funcao"
cursor.execute(query)

funcao = tkinter.StringVar()
opcoesFuncao = []
dicFuncao = {}
#preencher o array com os valores do banco
for i in cursor:
    opcoesFuncao.append(i[1])
    dicFuncao[i[1]]=i[0]

funcao.set("Escolha")
funcaoOption = tkinter.OptionMenu(janela,funcao,*opcoesFuncao)
funcaoOption.grid(column=2, row=4, columnspan=2)

#----------- Linha do departamento---------------
funcaoLabel = tkinter.Label(janela,text="Departamento:")
funcaoLabel.grid(column=0, row=5, sticky="w", columnspan=2)

depto = tkinter.StringVar()
#consulta das funções para preencher o select
query = "SELECT id,nome FROM departamento"
cursor.execute(query)

opcoesDepto = []
dicDepto = {}
for i in cursor:
    opcoesDepto.append(i[1])
    dicDepto[i[1]]=i[0]
    
depto.set("Escolha")
funcaoOption = tkinter.OptionMenu(janela,depto,*opcoesDepto)
funcaoOption.grid(column=2, row=5, columnspan=2)

#----------------função inserir------------------------
def inserir():
    if(funcao.get()!="Escolha")and (depto.get()!="Escolha"):
        conexao = pymysql.connect(host='localhost',port=3306,user='root',passwd='',db='empresa')
        cursor = conexao.cursor()
        cpf = cpfEntry.get()
        nome = nomeEntry.get()
        email = mailEntry.get()
        idFuncao = dicFuncao[funcao.get()]
        idDepto = dicDepto[depto.get()]
        query = "INSERT INTO `funcionario` VALUES (NULL,"+cpf+",'"+nome+"','"+email+"',"+str(idFuncao)+","+str(idDepto)+")"
        print(query)
        cursor.execute(query)
        conexao.commit()
        pass
        
    pass

#----------------função cancelar------------------------
def cancelar():
    
    pass

#------------------linha dos botões--------------------
btOk = tkinter.Button(janela,text="ok",command=inserir, width="16")
btOk.grid(row=6,column=0,columnspan=2)

btCancel = tkinter.Button(janela,text="cancelar",command=inserir, width="16")
btCancel.grid(row=6,column=2,columnspan=2)

#fechar a conexao com o BD
cursor.close()
conexao.close()

