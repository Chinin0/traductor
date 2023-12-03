class Config:
    SERVER_NAME = "localhost:5000"
    DEBUG = True
    DB_HOST = "localhost" 


    SECRET_KEY = 'B!1w8NAt1T^%kvhUI*S^'      #clave secreta para la proteccion del login


    TEMPLATE_FOLDER = "views/templates"      # defino las rutas para los archivos de vista 
    STATIC_FOLDER ="views/static"