import mysql.connector
from mysql.connector import errorcode
"""try:
	db_connection = mysql.connector.connect(
	    host='localhost', user='root', password='', database='bot-saude')
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

# db_connection = mysql.connector.connect(host='localhost', user='root', password='', database='bot-saude')
# cursor = db_connection.cursor()

#CREATE
#def Cadastro(nome, senha, idade, email):
db_connection = mysql.connector.connect(host='localhost', user='root', password='', database='bot-saude')
cursor = db_connection.cursor()

id = ''
nome = 'Cleber Gomes da Silva'
senha = 'senha3'
idade = 25
email = 'cleber@gmail.com'

sql = f'INSERT INTO Paciente (id_do_paciente, nome_paciente, senha_paciente, idade, email) VALUES ({id}, "{nome}", "{senha}", {idade}, "{email}")'

cursor.execute(sql)
cursor.commit()


#READ

email = 'fabio@gmail.com'

sql = f'SELECT * FROM Paciente WHERE email="{email}"'
cursor.execute(sql)
resultado = cursor.fetchall()




#DELETE
data = '2022-07-15'

sql = f'DELETE FROM Consultas WHERE data = "{data}"'

cursor.close()
db_connection.close()




#Cadastro('antonio', 'senha2', '20', 'antonio@gmail.com')
