from flask import Flask, render_template
from formulas_cartola import base_de_dados

app_flask = Flask(__name__)

@app_flask.route("/")
def homepage():
    return render_template("homepage.html")

@app_flask.route('/tabela')
def tabela():
        return render_template("tabela.html", dados=base_de_dados)

if __name__ == "__main__":
    app_flask.run(debug=True)
    
