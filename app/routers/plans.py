from flask import Blueprint, render_template, request, session




global_plans = Blueprint("plans",__name__)
#funciones decoradas, (para que puedan ser usadas en otro archivo)
@global_plans.route('/', methods = ['GET'])
def plans():
    return render_template("plans.html")