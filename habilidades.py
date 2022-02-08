from flask import Flask, request
from flask_restful import Resource
import json

lista_habilidades = ['Python', 'Java', 'Flask', 'PHP']
data = json.dumps(lista_habilidades) #converter a lista em json 

#metodos de listar, alterar e excluir registros
class Habilidades(Resource):
    def get(self, id):
        try:
            response = lista_habilidades[id]
        except IndexError:   
            mensagem = 'Desenvolvedor de ID {} não existe'.format(id)
            response = {'status':'Erro', 'mensagem': mensagem}
        except Exception:
            mensagem = 'Error desconhecido. Procure o administrador da API'
            response = {'status':'Erro', 'mensagem': mensagem}    
        return response

    def put(self, id):
        dados = json.loads(request.data)
        lista_habilidades[id] = dados

        return {'status':'sucesso', 'mensagem':'Registro alterado {}'.format(dados)}

    def delete(self, id):
        lista_habilidades.pop(id)
        dados = json.loads(request.data)
        return {'status':'sucesso', 'mensagem':'Registro excluído!'} 


#metodos listar todas as habilidades e inserir nova habilidade.
class ListaHabilidades(Resource):
    def get(self):
        return lista_habilidades

    def post(self, id):
        dados = json.loads(request.data)
        posicao = len(data)
        dados['id'] = posicao
        lista_habilidades.append(dados) #inserindo novos dados na lista json
        return lista_habilidades[posicao]    