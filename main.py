from flask import Flask, request, render_template

app=Flask(__name__)

@app.route("/")
def index():
    escuela="UTL"
    alumnos=["Mario","Pedro","Luis","Dario"]
    return render_template("index.html",escuela=escuela,alumnos=alumnos)

@app.route("/alumnos")
def alum():
    return render_template("alumnos.html")

@app.route("/maestros")
def maest():
    return render_template("maestros.html")

@app.route("/hola")
def hola():
    return "<p> <h1> Hola desde hola<br>mundo</h1> </p>"

@app.route("/user/<string:name>")
def user(name):
    return "<h1>Hola "+name+"</h1>"

@app.route("/numero/<int:n>")
def numero(n):
    return "El numero es: {}".format(n)

@app.route("/user/<int:id>/<string:name>")
def user2(idu,name):
    return "ID: {} Nombre: {}".format(idu,name)

@app.route("/suma/<float:n1>/<float:n2>")
def suma(n1,n2):
    return "El valor de {} + {} es: {}".format(n1,n2,n1+n2)

@app.route("/default")
@app.route("/default/<string:ab>")
def default(ab="URL"):
    return "El valor es: {}".format(ab)



if __name__=="__main__":
    app.run(debug=True)