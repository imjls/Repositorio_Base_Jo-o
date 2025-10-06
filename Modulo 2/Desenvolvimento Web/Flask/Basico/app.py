from flask import Flask, render_template,request

app = Flask(__name__)

#principal
@app.route('/')
def ola():
    return "Olá Mundo!, João"

@app.route('/contato')
def contato():
    return render_template('contato.html')

### Criar um template Hobbies e colocar seus hobbies
#/hobbies
@app.route("/hobbies")
def hobbies():
    return render_template('hobbies.html')

@app.route("/esportes")
def esportes():
    return render_template('esportes.html')


@app.route("/jogos")
def jogos():
    jogos = ["Call of Duty", "Fifa 22", "Mk11"]
    return render_template('jogos.html', jogos = jogos)

if __name__ == '__main__':
    app.run(debug=True)