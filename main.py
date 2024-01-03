from flask import Flask, render_template, make_response, jsonify, request
from bd import Produtos

app = Flask(__name__)
app.json.sort_keys = False

@app.route('/')
def home():
    return render_template('index.html')


@app.route('/produtos', methods=['GET'])
def get_produtos():
    return make_response(
        jsonify(
            mensagem='Lista de Produtos',
            dados=Produtos
        )
    )


@app.route('/produtos', methods=['POST'])
def create_produto():
    produto = request.json
    Produtos.append(produto)
    return make_response(
        jsonify(
            mensagem='Produto cadastrado com sucesso',
            produto=produto) 
    )

app.run()