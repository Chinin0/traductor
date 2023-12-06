from flask import Blueprint, render_template, request, session




global_home = Blueprint("views",__name__)
#----------------------HOME------------------------------
#funciones decoradas, (para que puedan ser usadas en otro archivo)
@global_home.route('/', methods = ['GET'])
def home():
    return render_template("home.html")


#esto es una prueba