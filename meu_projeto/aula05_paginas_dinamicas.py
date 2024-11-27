"""
@author: viviam
"""
#página usuario.html dinâmica
from flask import Flask, render_template

app_viviam = Flask(__name__ , template_folder='templates')
#cria o objeto da aplicação

@app_viviam.route("/")  #rota para solicitação web
def homepage():          #função
    return render_template ("homepage.html")

@app_viviam.route("/contato")
def contato():
    return render_template("contato.html") 

@app_viviam.route("/index")
def indice():
    return render_template ("index.html") 

@app_viviam.route("/usuario")
def dados_usuario():
    nome_usuario="viviam"
    dados_usu = {"profissao": "Professora EBTT", "disciplina":"Desenvolvimento Web III"}
    return render_template("usuario.html", nome = nome_usuario, dados = dados_usu)
                                           #parâmetro recebe argumento
                                           #colocar o site no ar
if __name__ == "__main__": 
     app_viviam.run(port = 8000) 
                                