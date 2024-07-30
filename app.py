from flask import Flask, render_template

app = Flask(__name__)
TITULO = "Livros"
@app.route("/inicio")
def ola():
    livro = "senhor dos aneis", 
    lista_de_livros=["senhor doa Anéis", "Don Casmuro","codigo limpo"]
    return render_template("livros.html", titulo = TITULO, lista_de_livros=lista_de_livros)

app.run(debug=True)
"""from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return"curriculo"

@app.route('/livro')
def curriculo():
    return render_template('curriculo.html')

app.run(debug=True)"""