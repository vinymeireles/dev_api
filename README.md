# dev_api

Curso: Desenvolvimento Avançado Python com Flask e REST API
Digital Innovation One
No.	Descrição
1	Introdução ao Rest Api com Flask
2	Instalando Flask, criando ambiente virtual e introdução a Postman
3	Utilizando métodos, biblioteca Request e JSON
4	Desenvolvendo uma Rest Api completa
5	Desenvolvendo uma REST API com a extensão Flask-RESTful
6	Manipulando banco de dados com SQLAlchemy
7	Rest Api com persistência em banco de dados
1. O que é uma API
É um conjunto de rotinas para acesso a um aplicativo / software / plataforma baseado na web.
Acrônimo de Application Programming Interface, Interface de Programações de Aplicativos.
APIS são importantes quando se tem a intenção de realizar integrações com outros serviços.
Com as APIS a comunicação de software fica transparente ao usuário.
APIS podem ser locais, baseado em Web e baseados em programas.
2. O que é REST
É um modelo a ser utilizado para projetar arquiteturas de software baseados em comunicação via rede.
Acrônimo de Representation State Transfer - Transferência de Estado Representacional.
Foi definido por Roy Fielding em sua tese de doutorado (PhD) na UC Irvine em 2000.
REST projeta a ideia de que todo recurso deveria responder aos mesmo métodos.
3. O que é REST API
É uma API desenvolvida utilizando os principios da arquitetura REST.
Uma REST API é utilizada na comunicação / integração entre o software através de serviços Web.
Uma REST API é consumida através de requisições HTTP.
REST APIs são geralmente representados em formatos por JSON e XML. Também são usados em páginas HTML, PDF e arquivo de imagens.
Ao implementar uma REST API, cada metódo deve ser responsável por um tipo de ação. Exemplo: Consulta, Alteração, Imclusão e Exclusão.
4. Métodos do protocolo HTTP
GET: método que solicita algum recurso ou objeto do servidor via URI.
POST: método usado para envio de arquivos / dados ou formulário HTML para o servidor.
PUT: aceitar criar ou modificar um objeto do servidor.
DELETE: informa por meio da URI um objeto a ser deletado.
5. XML e JSON
É uma linguagem de marcação.
Utilizada para compartilhamento de informações através de requisições HTTP.
XML - Extensible Markup Language
Arquivo XML
<xmlcep>
  <cep>22041-001</cep>
  <logradouro>Avenida Atlântica</logradouro>
  <complemento>de 2174 a 2634 - lado par</complemento>
  <bairro>Copacabana</bairro>
  <localidade>Rio de Janeiro</localidade>
  <uf>RJ</uf>
  <unidade/>
  <ibge>3304557</ibge>
  <gia/>
</xmlcep>
JSON - JavaScript Object Notation
é um formato de troca de dados entre sistemas independente da linnguagem utilizada derivada do JavaScript.
Muitas linguagens possuem suporte nativo a JSON.
Arquivo JSON
{
  "cep":"22041-001",
  "logradouro":"Avenida Atlântica",
  "complemento":"de 2174 a 2634 - lado par",
  "bairro":"Copacabana",
  "localidade":"Rio de Janeiro",
  "uf":"RJ","unidade":"",
  "ibge":"3304557",
  "gia":"",
}
6. URL, URN e URI
URL: Uniform Resource Locator - Localizador de Recursos Universal.
Host que será acessado. Exemplo: globallabs.academy
URN: Uniform Resource Name - Nome do Recurso Universal.
_É o recurso que será identificado. Exemplo: /category/blog/
URI: Uniform Resource Identifier - Identificador de Recursos Universal
É o identificado do recurso, podendo ser uma imagem, um arquivo ou uma página. Exemplo: https://globallabs.academy/category/blog/
URI une Protocolo(https://), URL(globallabs.academy) e URN(/category/blog)
7. Framework Flask
É um microframework para Python utilizado para desenvolvimento de aplicações Web.
É chamado de microframework porque mantém um núcleo simples, mas é estendível.
Flask não possui camada de abstração para banco de dados, validação de formulários entre outros, mas é possivél estender com outras bibliotecas.
Por ser leve e simples de se usar, Flask é um dos frameworks Python mais utilizados para desenvolvimento de APIS.
Exemplo do código
from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
  return "Olá mundo!"
  
if __name__ == "__main__":
  app.run()
