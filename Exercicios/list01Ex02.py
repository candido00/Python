usuario=input("informe o usuário: \n")
senha=usuario
while senha==usuario:
    senha = input("informe uma senha diferente do usuário")
    if senha==usuario:
        print("A senha digitada não é válida")
