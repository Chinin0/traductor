from flask import Blueprint, render_template, request, session




global_dashboard = Blueprint("dashboard",__name__)
#----------------------DASHBOARD------------------------------
#funciones decoradas, (para que puedan ser usadas en otro archivo)
@global_dashboard.route('/', methods = ['GET'])
def dashboard():
    return render_template("dashboard.html")
