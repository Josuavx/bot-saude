from Paciente import Paciente
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

"""def preencherPaciente(resultado):
	
	print(resultado)
	id, nome, senha, idade, email = resultado


	#pc_info = Paciente(id, nome, email)

	ret.setId(id)
	pc_info.setNome(nome)
	pc_info.setEmail(email)
"""

def cadastro(nome, senha, idade, email):
	id = 'DEFAULT'
	
	sql = f'INSERT INTO Paciente (id_do_paciente, nome_paciente, senha_paciente, idade, email) VALUES ({id}, "{nome}", "{senha}", {idade}, "{email}")'

	cursor.execute(sql)

ret = Paciente(None, None, None)
#Cadastro('Pedro Silvino Aguiar', 'senha2', '29', 'pedro@gmail.com')


def consultasDisponiveis():
	#funciona

	sql = 'SELECT * FROM consultasDisponiveis'
	cursor.execute(sql)
	resultado = cursor.fetchall()
	

	return resultado


#re = consultasDisponiveis()

#print('re: ', re)



def marcarConsulta(ID_disponivel, id_medico, data, horario, lugar_medico):

	ID = 'DEFAULT'

	id_paciente = 1 #ret.getId()

	sql = f'INSERT INTO Consultas (ID, id_paciente, id_medico, data_consult, horario, lugar_medico) VALUES ({ID}, {id_paciente}, {id_medico}, "{data}", "{horario}", "{lugar_medico}")'
	cursor.execute(sql)
	sql = f'DELETE FROM consultasDisponiveis WHERE ID = {ID_disponivel}'
	cursor.execute(sql)

	return 'Consulta marcada com sucesso!'

#p = marcarConsulta(1, 1, '2022-07-15', '15:45:00', 'rua1')
#print(p)
	


#READ
def validarLogin(email, senha):

	sql = f'SELECT * FROM Paciente WHERE (email="{email}") AND (senha_paciente="{senha}")'
	cursor.execute(sql)
	resultado = cursor.fetchall()
	
	#ret = Paciente(None, None, None)

	##retorno = ret.setNome('13')

	#preencherPaciente(resultado[0])

	res = resultado[0]
	id, nome, senha, idade, email = res

	ret.setId(id)
	ret.setNome(nome)
	ret.setEmail(email)

	retorno1 = ret.getId()
	retorno2 = ret.getNome()
	retorno3 = ret.getEmail()

	#print('retorno:'+retorno1+"retorno 2: "+retorno2+"retorno3: ", retorno3)
	print(retorno1)
	print(retorno2)
	print(retorno3)

	return resultado

#res = validarLogin('fabio@gmail.com', 'senha1')

#if res != None:
#	print('Logado com sucesso!')



def consultasMarcadas():
	sql = f'SELECT * FROM Consultas WHERE id_paciente = {id}'

	cursor.execute(sql)
	resultado = cursor.fetchall()

	return resultado


#res = consultasMarcadas()
#print('res: ', res)

#DELETE

def cancelarConsulta(data, id):

	sql = f'DELETE FROM Consultas WHERE (data_consult = "{data}") AND id_paciente = {id}' #adicionar um and, pegar o id do paciente e comparar
	cursor.execute(sql)
	print('deletado')

id = ret.getId()

##cancelarConsulta('2022-07-15', id)

cursor.close()
db_connection.close()

#Cadastro('antonio', 'senha2', '20', 'antonio@gmail.com')