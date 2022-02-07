from flask import Flask, jsonify, request
import json

app = Flask(__name__)

desenvolvedores = [
    {'nome' : 'Vinicius',
    'habilidades': ['Python', 'Flash','Django']},
    {'nome' : 'Paulo',
    'habilidades': ['Python', 'Django', 'ReactJS']}
]
#devolve um desenvolvedor pelo ID, também  altera e deleta registros
@app.route('/dev/<int:id>/', methods=['GET','PUT', 'DELETE'])
def desenvolvedor(id):
    if request.method == 'GET': #enviar uma solicitação e recebe um json pelo ID
        try:
            response = desenvolvedores[id]
        except IndexError:   
            mensagem = 'Desenvolvedor de ID {} não existe'.format(id)
            response = {'status':'Erro', 'mensagem': mensagem}
        except Exception:
            mensagem = 'Error desconhecido. Procure o administrador da API'
            response = {'status':'Erro', 'mensagem': mensagem}    
        return jsonify(response)
    elif request.method == 'PUT': #alteração de registro por ID
        dados = json.loads(request.data)
        desenvolvedores[id] = dados
        return jsonify(dados)
    elif request.method == 'DELETE': #exclusão de registro por ID
        desenvolvedores.pop(id)
        return jsonify({'status':'sucesso', 'mensagem':'Registro excluído!'})     

#lista todos os desenvolvedores e permitir registrar um novo desenvolvedor
@app.route('/dev/', methods=['POST', 'GET'])
def lista_desenvolvedores():
    if request.method == 'POST':
        dados = json.loads(request.data)
        posicao = len(desenvolvedores)
        dados['id'] = posicao
        desenvolvedores.append(dados) #inserindo novos dados na lista json
        return jsonify(desenvolvedores[posicao])
    elif request.method == 'GET':    #lista todos os desenvolvedores em um json
        return jsonify(desenvolvedores)


if __name__ == '__main__':
    app.run(debug=True)

