from flask import Blueprint, render_template, request, session




global_card = Blueprint("card",__name__)
#funciones decoradas, (para que puedan ser usadas en otro archivo)
@global_card.route('/', methods = ['GET'])
def card():
    return render_template("card.html")