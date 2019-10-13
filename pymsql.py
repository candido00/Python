import pymysql

conexao = pymysql.connect(host="localhost",port=3306,user="root",passwd="",db="testepy")
cursor = conexao.cursor()

nome = input("Digite o nome do usuário: ")
cursor.execute("SELECT * FROM usuário WHERE nome LIKE '%s'"%nome)
print(cursor.description)

print("\n")

for linha in cursor:
    print(linha)

cursor.close()
conexao.close()
