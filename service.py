import teste
from flask import Flask, request, jsonify

app = Flask(__name__)

account = []

@app.route('/', methods=['POST'])
def main():
    data = request.get_json(silent=True)
    
    context = data['queryResult']['outputContexts']
    print(context)
    
    for contexts in context:
        if 'introduo-no-followup' in contexts['name']:
            info = contexts['parameters']
            nome = info['nome']['name']
            idade = info['idade']
            email = info['email']
            senha = info['senha']
            account.append({"nome": nome, "idade": idade, "email": email, "senha": senha})
        
        if 'introduo-yes-followup' in contexts['name']:
            info = contexts['parameters']
            email = info['email']
            senha = info['senha']
            account.append({"email": email, "senha": senha})
    
    #print(data)

    print(account)
    
    #alterando o texto do bot
    ##tt = teste.teste(data['fulfillmentText'])
    ##print(tt)

    ##data['fulfillmentText'] = 'Sucesso ao trocar.'

    return jsonify(data)

# run Flask app
if __name__ == "__main__":
    app.debug = False
    app.run()

