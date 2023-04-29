from flask import Flask, render_template
import dash

app_flask = Flask(__name__)

@app_flask.route("/")
def homepage():
    return render_template("homepage.html")

@app_flask.route('/tabela')
def tabela():
        return render_template("data_frame.html")

if __name__ == "__main__":
    app_flask.run(debug=True)

