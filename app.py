from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)
app.secret_key = "CHAVE_SECRETA_ALEATORIA"

@app.route("/")

def index():
    """
    Rota inicial: zera a pontuação e redireciona para a primeira pergunta.
    """
    session["score"] = 0
    return render_template("index.html")


@app.route("/resultado")
def resultado():
    """
    Exibe a pontuação final.
    """
    pontuacao_final = session.get("score", 0)
    return render_template("resultado.html", pontuacao=pontuacao_final)


if __name__ == "__main__":
    app.run(debug=True)