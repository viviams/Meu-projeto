"""
@author: viviam
"""
from flask import Flask  #importa a biblioteca. flask diferente de Flask

app_viviam = Flask (__name__) #cria objeto da aplicação. 
                               # Tem 2 underlines antes e depois de name

@app_viviam.route('/')
@app_viviam.route('/ola') # rota para solicitação web
                           # @ significa decorador
def raiz():                # função a ser executa quando chamar rota acima ('/ola')
    return 'Olá, turma!'

def saudacoes (nome):
    return f'Olá, {nome}!'

if __name__ == "__main__" : # Dois underlines no name e no main
    # diferenciar quando é executado aqui, como um script princial
    # ou é invocado por fora, quando importado por um módulo
    app_viviam.run(port = 8000)  #executa aplicação
