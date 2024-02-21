
from flask import Flask, request, render_template, Response, g, redirect
from flask_wtf.csrf import CSRFProtect
import forms


app=Flask(__name__)
app.secret_key='esta es la clave secreta'

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'),404

@app.before_request
def before_request():
    g.nombre='Daniel'
    # g.nombre='Daniel'
    print('before_request')
    
@app.after_request
def after_request(response):
    print('ultimo')
    if 'Daniel' not in g.nombre and request.endpoint not in ['index']:
        return redirect('index.html')
    return response

@app.route("/")
def index():
    escuela="UTL"
    alumnos=["Mario","Pedro","Luis","Dario"]
    return render_template("index.html",escuela=escuela,alumnos=alumnos)

@app.route("/alumnos",methods=["GET","POST"])
def alum():
    
    print("Dentro de alumnos")
    print("Hola {}".format(g.nombre))
    nom=""
    apaterno=""
    amaterno=""
    alum_form = forms.UsersForm(request.form)
    if request.method == 'POST' and alum_form.validate():
        nom=alum_form.nombre.data
        apaterno=alum_form.apaterno.data
        amaterno=alum_form.amaterno.data
        
        mensaje="Bienvenido {}".format(nom)
        flash(mensaje)
        
        # print("Nombre: {}".format(nom))
        # print("Apellido Paterno: {}".format(apaterno))
        # print("Apellido Materno: {}".format(amaterno))
        
    return render_template("alumnos.html",form=alum_form, nom=nom, apa=apaterno, ama=amaterno)

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

@app.route("/resultado",methods=["GET","POST"])
def mult():
    if request.method == "POST":
        num1=request.form.get("n1")
        num2=request.form.get("n2")
        return "<h1> La multiplicacion es {}</h1>".format(str(int(num1)*int(num2)))

@app.route("/formulario1")
def formulario():
    return render_template("formulario1.html")

@app.route("/formulario2")
def formulario2():
    return render_template("formulario2.html")

if __name__=="__main__":
    app.run(debug=True)