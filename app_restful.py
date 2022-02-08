from flask import Flask, request
from flask_restful import Resource, Api
import json
from habilidades import Habilidades

app = Flask(__name__)
api = Api(app)

desenvolvedores = [
    {'nome' : 'Vinicius',
    'habilidades': ['Python', 'Flash','Django']
    },
    {'nome' : 'Paulo',
    'habilidades': ['Python', 'Django', 'ReactJS']
    },
    {'nome' : 'Guilherme',
    'habilidades': ['PHP', 'JAVA', 'Laravel']
    }
]
#Classe para devolver um desenvolvedor por ID, tmb altera e deleta um desenvolvedor.
class Desenvolvedor(Resource):
    def get(self, id):
        try:
            response = desenvolvedores[id]
        except IndexError:   
            mensagem = 'Desenvolvedor de ID {} não existe'.format(id)
            response = {'status':'Erro', 'mensagem': mensagem}
        except Exception:
            mensagem = 'Error desconhecido. Procure o administrador da API'
            response = {'status':'Erro', 'mensagem': mensagem}    
        return response

    def put(self, id):
        dados = json.loads(request.data)
        desenvolvedores[id] = dados
        return dados

    def delete(self, id):
        desenvolvedores.pop(id)
        dados = json.loads(request.data)
        return {'status':'sucesso', 'mensagem':'Registro excluído!'} 

#classe para listar todos os desenvolvedores
class ListaDesenvolvedores(Resource):
    def get(self):
        return desenvolvedores

    def post(self):
        dados = json.loads(request.data)
        posicao = len(desenvolvedores)
        dados['id'] = posicao
        desenvolvedores.append(dados) #inserindo novos dados na lista json
        return desenvolvedores[posicao]

#criando e registrando as rotas em restful
api.add_resource(Desenvolvedor, '/dev/<int:id>/')      
api.add_resource(ListaDesenvolvedores, '/dev/')
api.add_resource(Habilidades, '/habilidades/')



if __name__ == '__main__':
    app.run(debug=True)