class PRODUTOS:
    def __init__(self,numeroID,nome,descricao,valorvenda,quantidade):
        self.numeroid=numeroID
        self.nomep=nome
        self.descri=descricao
        self.valorv=valorvenda
        self.quantidad=quantidade
        
    def REDUZIR(self,quantidade):
        self.quantidade-=quantidad

    def ADICIONAR(self):
        self.quantidade+=quantidad
        
        pass
TOTAL=[]
while True:
    nomep=input("digite o nome do produto ou 0 para encerrar:\n")
    if nomep=="0":
        break
    else:
        numeroid=int(input("digite o numero indentificador:\n"))
        descri=input("decreva o produto:\n")
        valorv=float(input("digite o valor do produto:\n"))
        quantidad=int(input("digite a quantidade do produto:\n"))
        TOTAL.append(PRODUTOS(numeroid,nomep,descri,valorv,quantidad))
print(TOTAL[0].nomep)
        
    
    
    
    

