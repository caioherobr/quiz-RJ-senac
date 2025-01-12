from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)
app.secret_key = "CHAVE_SECRETA_ALEATORIA"

@app.route("/")

def index():
    """
    Rota inicial: zera a pontuação e redireciona para a pergunta1 pergunta.
    """
    session["score"] = 0
    return render_template("index.html")

@app.route("/pergunta1", methods=["GET", "POST"])
def pergunta1():
    """
    Página da pergunta1 pergunta.
    Se for GET, renderiza o template. 
    Se for POST, verifica a resposta e atualiza a pontuação.
    """
    if request.method == "POST":
        resposta = request.form.get("resposta")
       
        if resposta == "":  
            # Se for a opção correta
            session["score"] += 1
        
        # Independente de acertar ou errar, segue para a pergunta2
        return redirect(url_for("pergunta2"))
    
    return render_template("pergunta1.html")

@app.route("/pergunta2", methods=["GET", "POST"])
def pergunta2():
    """
    Página da pergunta2 pergunta.
    """
    if request.method == "POST":
        resposta = request.form.get("resposta")
        # Verifique qual opção é correta
        if resposta == "":
            session["score"] += 1
        return redirect(url_for("pergunta3"))
    
    return render_template("pergunta2.html")

@app.route("/pergunta3", methods=["GET", "POST"])
def pergunta3():
    """
    Página da pergunta3 pergunta.
    """
    if request.method == "POST":
        resposta = request.form.get("resposta")
        # Verifique qual opção é correta
        if resposta == "":
            session["score"] += 1
        return redirect(url_for("pergunta4"))
    
    return render_template("pergunta3.html")

@app.route("/pergunta4", methods=["GET", "POST"])
def pergunta4():
    """
    Página da pergunta4 pergunta.
    """
    if request.method == "POST":
        resposta = request.form.get("resposta")
        # Verifique qual opção é correta
        if resposta == "":
            session["score"] += 1
        return redirect(url_for("resultado"))
    
    return render_template("pergunta4.html")

@app.route("/resultado")
def resultado():
    """
    Exibe a pontuação final.
    """
    pontuacao_final = session.get("score", 0)
    if pontuacao_final >=4:
        mensagem = "Parabéns"
    else:
        mensagem = "Tente outra vez"
    return render_template("resultado.html", pontuacao=mensagem)

if __name__ == "__main__":
    app.run(debug=True)