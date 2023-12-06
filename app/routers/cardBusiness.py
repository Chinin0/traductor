from flask import Blueprint, render_template, request, session




global_cardBusiness = Blueprint("cardBusiness",__name__)
#funciones decoradas, (para que puedan ser usadas en otro archivo)
@global_cardBusiness.route('/', methods = ['GET'])
def card():
    return render_template("cardBusiness.html")