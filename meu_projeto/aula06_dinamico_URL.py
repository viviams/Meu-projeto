#Criamos no decorador app_viviam com página dinâmica
from flask import Flask, render_template

app_viviam = Flask(__name__)
 

@app_viviam.route("/")  #rota para solicitação web
def homepage():     #função da rota
    return render_template ("homepage.html")

@app_viviam.route("/index")
def indice():
    return render_template ("index.html") 

@app_viviam.route("/contato")
def contato():
    return render_template("contato.html") 

@app_viviam.route("/usuario")
def dados_usuario():
    nome_usuario="viviam"
    dados_usu = {"profissao": "Professora EBTT", "disciplina":"Desenvolvimento Web III"}
    return render_template("usuario.html", nome = nome_usuario, dados = dados_usu)
                                           #parâmetro recebe argumento
                                           #colocar o site no ar
#########################################
"""
  Página dinâmica com argumentos via URL. Precisa de 3 elementos: 
  o dado dinâmico na URL entre < >, 
  os parâmetros na função e 
  a página montada dinamicamente.
"""
@app_viviam.route('/<id>')
def saudacao(id):
    return render_template('homepage_nome.html', nome=id)

@app_viviam.route("/usuario/<nome_usuario>;<nome_profissao>;<nome_disciplina>") 
#o que está entre < > é o dado dinâmico que vai diferenciar a página para cada usuário.
def usuario (nome_usuario, nome_profissao, nome_disciplina): #passa o valor da variável como argumento na função
    
    dados_usu = {"profissao": nome_profissao, "disciplina": nome_disciplina}
    #dados_usu é um dicionário com 2 chaves:valor

    return render_template ("usuario.html", nome=nome_usuario, dados = dados_usu)  
        #o parâmetro 'nome' recebe como argumento o valor armazenado na variável 'nome_usuario'
        #o parâmetro 'dados' recebe como argumento o dicionário dados_usu


#colocar o site no ar
if __name__ == "__main__": 
     app_viviam.run(port = 8000) 