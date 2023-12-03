# Sistema web para traduccion de videoconferencias. 
Proyecto para la materia Software1, con el ing. Martinez.
Utilizando Python, Flask y PosgresSQL.

<hr/>

1.- Instalar virtualenv:
Desde la terminal de tu VC o desde el cmd, (esto solo se realiza la primera vez) ejecutar lo siguiente:
### `pip install virtualenv`

2.- Crear un entorno virtual:
Descargar el proyecto, ingresa a la ruta del proyecto desde el cmd, (esto solo se realiza la primera vez) ejecutar lo siguiente:
opcion1:
### `virtualenv env`
opcion2:
### `python -m virtualenv env`

3.- Activar el entorno virtual, desde la terminal de tu VC o desde el cmd, ejecutar:
opcion1:
### `.\env\Scripts\activate`
opcion2:
### `.\env\Scripts\activate.bat`
opcion para desactivar:
### `.\env\Scripts\deactivate.bat`

4.- Para instalar los paquetes necesarios, esto solo se realiza la primera vez que abres el proyecto desde otro equipo:
### `pip install -r requirements.txt`

5.- Si ya estas en Visual Code no es necesario este paso, sino es así, desde el mismo cmd, ejecutar:
### `code .`

<hr/>


# Primeros pasos para crear tu proyecto MVC con Flask
1.- Crear una carpeta para tu proyecto; examen2
2.- Instalar y activar el entorno virtual.
3.- Instalar desde la terminal
pip install Flask
pip install Flask-WTF

3.- Crear los archivos: config.py, run.py 
4.- Crear la carpeta para la aplicacion; app
5.- crear el archivo dentro de app: __init__.py
6.- crear las carpetas dentro de app: controllers, models, routers, views.
7.- crear las carpetas dentro views: static, templates.
8.- Crear la carpeta y archivo dentro de templates; base, home.html
9.- Crear el archivo dentro de base; base.html
10.- Desarrollar tu plantilla en el archivo base.html para el proyecto y utiliza la carpeta static para los archivos que se necesiten.
11.-  Desarrolla tu pagina de inicio en el archivo home.html, no olvide de poner como referencia al inico del codigo la plantilla base: {% extends "base.html" %}
12.- Crear los archivos dentro de routers; routers.py , __init__.py
13.- Desarrollar el archivo routers.py
14.- Desarrollar el archivo __init__.py para centralizar las rutas

15.- Desarrollar el archivo config.py
16.- Desarrollar el archivo __init__.py
17.- Desarrollar el archivo run.py




