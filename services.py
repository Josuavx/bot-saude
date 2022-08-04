import json
import connection
import main
from google_auth_oauthlib.flow import Flow
from flask import Flask, request, jsonify, render_template


class values:
    token = ""
    email = ""
    id = ""
    url = ""

app = Flask(__name__)

appflow = Flow.from_client_secrets_file(
    'client_secret.json',
    scopes=['openid', 'https://www.googleapis.com/auth/dialogflow',
            'https://www.googleapis.com/auth/cloud-platform'],
    redirect_uri= 'https://dr-freud.herokuapp.com/login')  # Aqui tá redirecionando apos o login com google pra pasta padrao



@app.route('/')
def home():
     
    re = request.args.get('intention')
    if re == 'url':
        auth_uri = appflow.authorization_url()

        return {'res': auth_uri[0]}
    
    return render_template('/LandingPage/index.html')

@app.route('/login')
def login():

    code = request.args.get('code')

    appflow.fetch_token(code=code)
    credentials = appflow.credentials
    values.token = credentials.token

    return render_template('login.html')

#Recebe requisições do front (manipula, responde)
@app.route('/chatbot', methods= ['GET'])
def chat():
    if request.is_json:
        text = request.args.get('input_text')
        credencial = values.token

        retorno = main.Conversa(credencial, text)
        
        tip = type(retorno)
        if tip == list:
            if retorno[0] == 'cadastro':
                nome = retorno[1]
                senha = retorno[2]
                idade = retorno[3]
                email = retorno[4]

                retorno = connection.cadastro(nome, senha, idade, email)
            
            elif (retorno[0] == 'marcar'):
                id = retorno[1]
                retorno = connection.marcarConsulta(id, values.id)

            elif (retorno[0] == 'login'):
                email = retorno[1]
                senha = retorno[2]
            
                retorno = connection.validarLogin(email, senha)
                tip = type(retorno)
                if tip == tuple:
                    res = retorno[1]
                    values.email = res[0]
                    values.id = res[1]
        
                retorno = retorno[0]

        else:
            if retorno == 'consulta-marcar':
                retorno = connection.consultasDisponiveis()
            
            elif retorno == 'visualizar-consultas':
                retorno = connection.consultasMarcadas(values.id)
            
            elif (retorno == 'cancelar'):
                retorno = connection.cancelarConsulta(values.id)
        

        if retorno != None:
            return {'res': retorno}
        else: return 'falhou?'
        
    return render_template('/chatbot/index.html')



if __name__ == "__main__":
    app.debug = True
    app.run()
