from flask import Blueprint, render_template, request, session

# importamos los controladores de Usuario

# importamos los Modelos de usuario

#----------------------LOGIN------------------------------
#funciones decoradas, (para que puedan ser usadas en otro archivo)
global_login = Blueprint("login",__name__)

@global_login.route('/', methods = ['GET'])
def login():
    return render_template("login.html")