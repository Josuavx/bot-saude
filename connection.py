import mysql.connector
from mysql.connector import errorcode
"""try:
	db_connection = mysql.connector.connect(host='localhost', user='root', password='', database='bot-saude')
	print("Conexão com banco de dados: Sucesso.")
except mysql.connector.Error as error:
	if error.errno == errorcode.ER_BAD_DB_ERROR:
		print("Database inexistente.")
	elif error.errno == errorcode.ER_ACCESS_DENIED_ERROR:
		print("Username ou Senha errada.")
	else:
		print('erro:', error)
else:
	db_connection.close()
"""

db_connection = mysql.connector.connect(host='localhost', user='root', password='', database='bot-saude')
cursor = db_connection.cursor()

sql = ("SELECT id, name, cpf FROM user")

cursor.execute(sql)

for (id, name, cpf) in cursor:
  print(id, name, cpf)
print("\n")


print(cursor)