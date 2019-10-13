import pymysql

conexao = pymysql.connect(host='localhost',port=3306,user='root',passwd='',db='empresa')
cursor = conexao.cursor()

nome = input("Digite o nome do funcionario: ")

cursor.execute("SELECT `nome` FROM funcionario WHERE departamento=2 ")
print(cursor.description)

print()

for linha in cursor:
    print(linha)


cursor.close()
conexao.close()
