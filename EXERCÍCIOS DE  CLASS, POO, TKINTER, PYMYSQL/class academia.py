import datetime

class Alunos:
    def __init__(self,nom,dataN,mail,dataI,alt,pes):
        self.nome=nom
        self.nasc=dataN
        self.email=mail
        self.insc=dataI
        self.altura=alt
        self.peso=pes

    def GETIDADE(self):
        IDADE=datetime.date.today()-self.nasc
        return int(IDADE.days/365.25)

    def CAL_IMC(self):
        return(self.peso/self.altura**2)
    
    def TEMPO_INSCRICAO(self):
        T_INSCRICAO=(datetime.date.today()-self.insc)
        return int(T_INSCRICAO.days/30)
    
    
        
           
    pass

DADOS_ALUNOS=[]
while True:
    nome=input("Informe seu nome, ou '0' pra sair: \n")
    if(nome=="0"):
        break
    else:
        email=input("Informe seu Email: \n")
        altura=float(input("Informe sua altura: \n"))
        peso=float(input("Informe seu peso: \n"))
        nasAno=int(input("Informe o ano em que voce nasceu: \n"))
        nasMes=int(input("Informe o mes em que você nasceu: \n"))
        nasDia=int(input("Informe o dia em que você nasceu: \n"))
        inscAno=int(input("Informe o ano de sua inscrição: \n"))
        inscMes=int(input("Informe o mes de sua inscrição: \n"))
        inscDia=int(input("Informe o dia de sua inscrição: \n"))
        dataNascimento=datetime.date(nasAno,nasMes,nasDia)
        dataInscricao=datetime.date(inscAno,inscMes,inscDia)
        DADOS_ALUNOS.append(Alunos(nome,dataNascimento,email,dataInscricao,altura,peso))


maisvelho = (DADOS_ALUNOS[0].GETIDADE())
maisnovo = (DADOS_ALUNOS[0].GETIDADE())
maisgordo =(DADOS_ALUNOS[0].CAL_IMC())
maismagro = (DADOS_ALUNOS[0].CAL_IMC())
maisantigo = (DADOS_ALUNOS[0].TEMPO_INSCRICAO())
maismoderno = (DADOS_ALUNOS[0].TEMPO_INSCRICAO())



for i in (DADOS_ALUNOS):
    print("nome:",i.nome,"idade:",i.GETIDADE(),"imc:",i.CAL_IMC(),"tempo inscriçao:",i.TEMPO_INSCRICAO(),"meses")
    print("\n")
    if i.GETIDADE()>maisvelho:
        maisvelho=i.GETIDADE()
        
    if i.GETIDADE()<maisnovo:
        maisnovo=i.GETIDADE()
        
    if i.CAL_IMC() > maisgordo:
        maisgordo= i.CAL_IMC()

    if i.CAL_IMC() < maismagro:
        maismagro= i.CAL_IMC()

    if i.TEMPO_INSCRICAO() > maisantigo:
        maisantigo = i.TEMPO_INSCRICAO()

    if i.TEMPO_INSCRICAO() < maismoderno:
        maismoderno = i.TEMPO_INSCRICAO()
print("o mais velho tem:",maisvelho,"o mais novo tem:",maisnovo,"o mais gordo tem:",maisgordo,"IMC","o mais magro tem:",maismagro,"IMC","o mais antigo tem:",maisantigo,"meses","o mais moderno tem:",maismoderno,"meses")


    


    
          
          
    
        

