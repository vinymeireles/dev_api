from flask import Flask
app = Flask(__name__)

#criando a rota e o depurador da aplicação
@app.route('/<int:numero>', methods=['GET','POST'])

def ola(numero):
    return 'Hello, Aprendendo sobre Flask. {}'.format(numero)

if __name__ == '__main__':
    app.run(debug=True)

