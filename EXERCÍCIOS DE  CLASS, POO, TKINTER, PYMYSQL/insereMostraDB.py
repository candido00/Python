"""import pymysql

conexao = pymysql.connect(host='localhost',port=3306,user='root',passwd='',db='empresa')
cursor = conexao.cursor()

while True:
    nome = input("informe o nome ou 0 para encerrar:\n")
    if nome=="0":
        break
    cpf = (input("informe o CPF: \n"))
    email = input("informe o email: \n")
    idFuncao = (input("informe o id da função:\n"))
    idDepto = (input("informe o id do departamento:\n"))
    sql = "INSERT INTO funcionario VALUES (NULL,'"+nome+"','"+email+"','"+cpf+"',"+idFuncao+","+idDepto+")"
    cursor.execute(sql)
    conexao.commit()
    print("Funcionário inserido com sucesso!\n")

#Exibir os funcionários da tabela
cursor.execute("SELECT * FROM funcionario") #executando o código SQL na conexão atual

for linha in cursor:
    print(linha)

cursor.close()
conexao.close()"""

#-------------------------------------------------------------------------------

import tkinter

janela = tkinter.Tk()
janela.geometry("400x400")
janela.title("Inserir Dados")

titulo = tkinter.Label(janela,text="Inserir Dados")
titulo.grid(column=0,row=0,columnspan=4)
#-------------------------------------------------------------------------------
nomelabel=tkinter.Label(janela,text="nome")
nomelabel.grid(row=1,column=0,columnspan=2, sticky="w")
nomeentry=tkinter.Entry(janela)
nomeentry.grid(row=1,column=2,columnspan=2)

emaillabel=tkinter.Label(janela,text="email")
emaillabel.grid(row=2,column=0,columnspan=2, sticky="w")
emailentry=tkinter.Entry(janela)
emailentry.grid(row=2,column=2,columnspan=2)

cpflabel=tkinter.Label(janela,text="cpf")
cpflabel.grid(row=3,column=0,columnspan=2, sticky="w")
cpfentry=tkinter.Entry(janela)
cpfentry.grid(row=3,column=2,columnspan=2)
#--------------------------botao------------------------------------------------


#--------------------------linha de funçao--------------------------------------
funcaoLabel= tkinter.Label(janela,text="Funçao:")
funcaoLabel.grid(column=0, row=4, sticky="w",columnspan=2)

funcao=tkinter.StringVar()
opcoesFuncao=(1,2,3)
funcao.set("Escolha")
funcaoOption=tkinter.OptionMenu(janela,funcao,*opcoesFuncao)
funcaoOption.grid(column=2, row=4, columnspan=2)
#---------------------------linha de departamento-------------------------------
funcaoLabel= tkinter.Label(janela,text="Departamento:")
funcaoLabel.grid(column=0, row=5, sticky="w",columnspan=2)

depto=tkinter.StringVar()
opcoesdepto=(1,2,3)
depto.set("Escolha")
funcaoOption=tkinter.OptionMenu(janela,depto,*opcoesdepto)
funcaoOption.grid(column=2, row=5, columnspan=2)


janela.mainloop()
