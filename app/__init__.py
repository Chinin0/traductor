######################################################################################
#                          AQUI SE CREAR EL PROYECTO EXAMEN                        #
######################################################################################

from flask import Flask
from config import Config              # traemos las configuraciones del archivo => config.py
from flask_wtf.csrf import CSRFProtect # para la proteccion del login, importante crear la SECRET_KEY


# importamos las rutas con sus variablas de entorno
from .routers import global_dashboard, global_home, global_login

csrf = CSRFProtect()    # creamos una instancia para la proteccion para login   => csrf


#######################################################################################
# Creando el proyecto, con las rutas de las carpetas las cuales estan en => config.py #
#######################################################################################
proyecto = Flask(__name__, static_folder = Config.STATIC_FOLDER, template_folder = Config.TEMPLATE_FOLDER)
proyecto.config.from_object(Config)
csrf.init_app(proyecto)



#####################################################################################
#                                 RUTAS                                             #
#     Aqui se llama a las rutas imprimiendo su template, osea la VISTA en la WEB    #
#####################################################################################
proyecto.register_blueprint(global_home, url_prefix = "/")
proyecto.register_blueprint(global_login, url_prefix = "/login")
proyecto.register_blueprint(global_dashboard, url_prefix = "/dashboard")
