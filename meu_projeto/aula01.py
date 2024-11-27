from flask import Flask

app_viviam = Flask (__name__)

@app_viviam.route('/')
def raiz():
    return 'Olá, turma!'

app_viviam.run()
