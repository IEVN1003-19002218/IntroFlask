
from flask import Flask, render_template, request
import math
app = Flask(__name__)


@app.route("/")
def index():
    titulo = "Pagina de inicio"
    listado = ['Python', 'Flask', 'jinja2', 'HTML', 'CSS']
    return render_template("index.html", titulo=titulo, listado=listado)



@app.route("/distancia", methods=["GET", "POST"])
def distancia():
    x1 = 0
    y1 = 0
    x2 = 0
    y2 = 0
    resultado = 0

    if request.method == 'POST':
        x1 = float(request.form.get('x1'))
        y1 = float(request.form.get('y1'))
        x2 = float(request.form.get('x2'))
        y2 = float(request.form.get('y2'))

        resultado = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

    return render_template('distancia.html',
                           x1=x1,
                           y1=y1,
                           x2=x2,
                           y2=y2,
                           resultado=resultado)

 


@app.route("/operasbas", methods=["GET", "POST"])
def operasbas():
    num1 = 0
    num2 = 0
    resultado = 0
    operacion = ''

    if request.method == 'POST':
        num1 = request.form.get('num1')
        num2 = request.form.get('num2')
        operacion = request.form.get('operaciones')

        if operacion == 'sumar':
            resultado = float(num1) + float(num2)

        elif operacion == 'restar':
            resultado = float(num1) - float(num2)

        elif operacion == 'multiplicar':
            resultado = float(num1) * float(num2)

    return render_template('operasbas.html',
                           num1=num1,
                           num2=num2,
                           resultado=resultado,
                           operacion=operacion)





@app.route("/hola")
def hola():
    return "<h1> Hola PWA </h1>"


@app.route("/user/<string:nom>")
def user(nom):
    return "<h1>Hola User: {} </h1>".format(nom)

@app.route("/numero/<int:n>")
def numero(n):
    return "Numero: {}".format(n)

@app.route("/user/<int:id>/<string:username>")
def username (id, username):
    return "ID: {} nombre {}".format(id, username)

@app.route("/suma/<float:num1>/<float:num2>")
def func(num1, num2):
    return "La suma es: {}".format(num1 + num2)



if __name__ == "__main__":
    app.run(debug=True)
