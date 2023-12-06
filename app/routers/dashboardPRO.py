from flask import Blueprint, render_template, request, session




global_dashboardPRO = Blueprint("dashboardPRO",__name__)
#funciones decoradas, (para que puedan ser usadas en otro archivo)
@global_dashboardPRO.route('/', methods = ['GET'])
def dashboardPRO():
    return render_template("dashboardPRO.html")