# Unibratec
# Prova de Lógica
# Alunos: Adriel Pergentino | Lucicleydson Cândido


# Funcao que devolve o resultado da operacao escolhida
def converte (opcao, valor, Rel):

    reultado = 0
    # m/s para Km/h
    if opcao == 1:
        resultado = valor * 3.6
        print(":::::",resultado, " Km/h")
        Rel.append([valor, " m/s =",resultado, "Km/h"])
        
    # Km/h para m/s
    elif opcao == 2:
        resultado = valor/3.6
        print(":::::",resultado, " m/s\n")
        Rel.append([valor, " Km/h =",resultado, "m/s"])
        
    # cm para polegadas
    elif opcao == 3:
        resultado = valor / 2.54
        print(":::::",resultado, " polegadas\n")
        Rel.append([valor, " cm =",resultado, "polegadas"])
        
    # polegada para cm 
    elif opcao == 4:
        resultado = valor * 2.54
        print(":::::",resultado, " cm\n")
        Rel.append([valor, " polegadas =",resultado, "cm"])

    # ºF para ºC
    elif opcao == 5:
        resultado = ( valor * 33  - 32)/1.8
        print(":::::",resultado, " ºC\n")    
        Rel.append([valor, " ºF =",resultado, "ºC"])

    # ºC para ºF
    elif opcao == 6:
        resultado = (valor * 1.8 + 32)/33
        print(":::::",resultado, " ºF\n")
        Rel.append([valor, " ºC =",resultado, "ºF"])
        
    return Rel

# Interação com o usuário
print(" \n**************************************************")
print("\t\tCONVERSÃO DE UNIDADES")
print("**************************************************")



# Declaracao de variáveis
opcao = -1
valor = 0
parcial = [0,0,0]
relatorio = []
tamanhoVetor = 0
i = 0
usuario = str(input("\n Nome de usuário: "))

# Laço utilizado para controlar a saida do programa
while True :

    # Laço utilizado para impedir que o usuário digite uma opção inválida
    while opcao < 0 or opcao > 6:
        print (" \t0 : Sair do programa")
        print (" \t1 : m/s  para Km/h")
        print (" \t2 : Km/h para m/s")
        print (" \t3 : cm   para pol")
        print (" \t4 : pol  para cm ")
        print (" \t5 : ºF   para ºC" )
        print (" \t6 : ºC   para ºF")
        opcao = int(input(" Escolha uma opcao: "))

    if opcao == 0:
        break

    else:
        valor = float(input(" Digite o valor a ser convertido: "))
        #relatorio.append([opcao, valor, converte(opcao,valor)])
        relatorio = converte(opcao,valor,relatorio)
        opcao = -1

# Gerando o Relatório        
print(" *************** RELATORIO DO USUARIO: ",usuario, " *************** ")

while i < len(relatorio):
    print(i+1," - ",relatorio[i][0],relatorio[i][1],relatorio[i][2],relatorio[i][3])
    i += 1

print(" ***************************************************************** ")
