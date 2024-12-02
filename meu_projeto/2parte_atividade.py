from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)
app.secret_key = 'sua-chave-secreta'  # Necessário para usar o flash

# Página Inicial (Tela de Login)
@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        senha = request.form['senha']
        # Aqui você pode adicionar validações de senha ou autenticação
        if senha == "senha_correta":  # Exemplo de verificação simples
            return redirect(url_for('home'))
        else:
            flash('Senha incorreta, tente novamente.')
    return render_template('login.html')

# Página de Cadastro
@app.route('/cadastro', methods=['GET', 'POST'])
def cadastro():
    if request.method == 'POST':
        nome = request.form['nome']
        cpf = request.form['cpf']
        email = request.form['email']
        telefone = request.form['telefone']
        endereco = request.form['endereco']
        senha = request.form['senha']
        confirmacao_senha = request.form['confirmacao_senha']

        if senha != confirmacao_senha:
            flash("As senhas não coincidem. Tente novamente.")
        else:
            # Aqui você pode salvar os dados em um banco ou arquivo, se necessário
            flash("Cadastro realizado com sucesso!")
            return redirect(url_for('login'))

    return render_template('cadastro.html')

# Página Home (após login bem-sucedido)
@app.route('/home')
def home():
    return "Bem-vindo ao sistema!"

if __name__ == '__main__':
    app.run(debug=True)
