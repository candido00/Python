import tkinter
import pymysql

janela = tkinter.Tk()
janela.geometry("250x350")

titulo = tkinter.Label(janela,text="Tela de Listagens")
titulo.grid(row=0, column=0, columnspan=4)
#----------- Area do Select---------------
frameSelect = tkinter.LabelFrame(janela, text="LISTAGEM")
frameSelect.grid(column=0, row=1, sticky="w", columnspan=4)
selectLabel = tkinter.Label(frameSelect,text="Escolha uma listagem")
selectLabel.grid(column=0, row=0, sticky="w", columnspan=2)

select = tkinter.StringVar()
opcoesSelect = ["cursos", "turmas","disciplinas"]

select.set("Escolha")
selectOption = tkinter.OptionMenu(frameSelect,select,*opcoesSelect)
selectOption.grid(column=2, row=0, columnspan=2)
#----------- Area de pesquisa do aluno---------------
framePesquisa = tkinter.LabelFrame(janela,text="PESQUISAR ALUNO:")
framePesquisa.grid(column=0, row=2, sticky="w", columnspan=4)

matriculaLabel = tkinter.Label(framePesquisa,text="Matrícula do aluno:", )
matriculaLabel.grid(column=0, row=0, sticky="w", columnspan=2)

matriculaEntry = tkinter.Entry(framePesquisa)
matriculaEntry.grid(column=2, row=0, columnspan=2)

#------------------ Area de listagens ----------------
frameLista = tkinter.LabelFrame(janela,text="Listagens: ")
frameLista.grid(column=0, row=3,sticky="w",columnspan=4)

lista = tkinter.Listbox(frameLista, width="40")
lista.grid(column=0, row=0,sticky="w", columnspan=4)

#----------------função Listar------------------------
def listar():
    if(select.get()!="Escolha")and(select.get()!="Escolha"):
        #conexao do banco
        conexao = pymysql.connect(host='localhost',port=3306,user='root',passwd='',db='curso')
        cursor = conexao.cursor()
        lista.delete(0,"end")
        if(select.get()=="cursos"):
            consulta = "SELECT cod_curso,nome FROM `curso`"
            
        elif(select.get()=="turmas"):
            consulta = "SELECT cod_turma,nome FROM `turma`"
           
        elif(select.get()=="disciplinas"):
            consulta = "SELECT cod_disc,nome FROM `disciplina`"

        print(consulta)
        cursor.execute(consulta)
        for i in cursor:
            print(i)
            texto = str(i[0])+" - "+i[1]
            lista.insert(i[0],texto)
        pass
        
    pass

#----------------função Pesquisar------------------------
def pesquisar():
    #conexao do banco
    conexao = pymysql.connect(host='localhost',port=3306,user='root',passwd='',db='curso')
    cursor = conexao.cursor()
    lista.delete(0,"end")
    matricula = matriculaEntry.get()
    if (matricula != ""):
        consulta = "SELECT mat,nome FROM aluno WHERE mat = "+matricula
        print(consulta)
        cursor.execute(consulta)
        for i in cursor:
            texto = str(i[0])+" - "+i[1]
            lista.insert(i[0],texto)
    else:
        consulta = "SELECT mat,nome FROM aluno"
        print(consulta)
        cursor.execute(consulta)
        for i in cursor:
            texto = str(i[0])+" - "+i[1]
            lista.insert(i[0],texto)
    pass

#----------------função cancelar------------------------
def cancelar():
    
    pass

#------------------linha dos botões--------------------
btOk = tkinter.Button(frameSelect,text="ok",command=listar, width="16")
btOk.grid(row=2,column=2,columnspan=2)

btPesquisa = tkinter.Button(framePesquisa,text="Pesquisar",command=pesquisar, width="16")
btPesquisa.grid(row=1,column=2,columnspan=2)



