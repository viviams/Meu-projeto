#Criamos no decorador "app_Mariela" com 2 páginas HTML estáticas.
"""
@author: viviam
"""
#nova biblioteca importada chamada render_template
from flask import Flask, render_template

app_viviam = Flask(__name__ , template_folder='templates')
#cria o objeto da aplicação

@app_viviam.route("/")  #rota para solicitação web
def homepage():          #função
    return render_template ("homepage.html")

@app_viviam.route("/contato")
def contato():
    return render_template("contato.html") 

if __name__ == "__main__": 
     app_viviam.run(port = 8000) 
                                