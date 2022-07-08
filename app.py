import json

from flask import Flask, jsonify, request

app = Flask(__name__)

developers = [
    {'nome': 'Luciano',
     'habilidades': ['Python', 'Django', 'Flask']

     },
    {'nome': 'Juraci Jubileu',
     'habilidades': ['Javascript', 'Ruby', 'Ruby on Rails']}

]


@app.route('/dev/<int:id>/', methods=['GET', 'PUT', 'DELETE'])
def developers(id):
    if request.method == 'GET':
        try:
            response = developers[id]
        except IndexError:
            mensagem = 'Desenvolvedor de ID {} não existe'.format(id)
            response = {'status': 'erro', 'mensagem': mensagem}
        except Exception:
            mensagem = 'Erro desconhecido, procure o admin..'
            response = {'status': 'erro', 'mensagem': mensagem}
            return jsonify(response)
    elif request.method == 'PUT':
        dados = json.loads(request.data)
        developers[id] = dados
        return jsonify(dados)
    elif request.method == 'DELETE':
        developers.pop(id)
        return jsonify({'status': 'sucess', 'mensagem': 'registro removido'})


# def lista_developers():

if __name__ == '__main__':
    app.run(debug=True)
