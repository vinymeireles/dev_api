from flask import Flask, jsonify, request
import json

app = Flask(__name__)

tarefas = [
{
    'id': 0,
    'responsavel': 'Vinicius',
    'tarefa': 'Desenvolver método GET',
    'status': 'Concluido'
},
{
    'id': 1,
    'responsavel': 'Otávio',
    'tarefa': 'Desenvolver método PUT',
    'status': 'pendente'
},
{
    'id': 2,
    'responsavel': 'Paulo',
    'tarefa': 'Desenvolver método GET, PUT, POST, DELETE',
    'status': 'pendente'
},
]
#metodos GET, PUT e DELETE: listar, Alterar e excluir.
@app.route('/tarefa/<int:id>/', methods=['GET', 'PUT', 'DELETE'])
def tarefas_dev(id):
    if request.method == 'GET':
        try:
            response = tarefas[id]
        except IndexError:   
            mensagem = 'Responsável de ID {} não existe'.format(id)
            response = {'status':'Erro', 'mensagem': mensagem}
        except Exception:
            mensagem = 'Error desconhecido. Procure o administrador da API'
            response = {'status':'Erro', 'mensagem': mensagem}    
        return jsonify(response)
    elif request.method == 'PUT': #alteração de registro por ID
        dados = json.loads(request.data)
        tarefas[id] = dados
        return jsonify(dados)
    elif request.method == 'DELETE': #exclusão de registro por ID
        tarefas.pop(id)
        return jsonify({'status':'sucesso', 'mensagem':'Registro excluído!'})     

#metodos POST, GET: Inserir e Listar todos os registros
@app.route('/tarefa/', methods=['POST', 'GET'])
#adicionar tarefas
def listar_tarefas():
    if request.method == 'POST':
        dados = json.loads(request.data)
        tarefas.append(dados) 
        mensagem = 'Registro inserido com sucesso'
        return jsonify({'status': mensagem})
    #listar todas as tarefas    
    elif request.method == 'GET':    
        return jsonify(tarefas)

if __name__ == '__main__':
    app.run(debug=True)