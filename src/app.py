from flask import Flask

from flask_cors import CORS

from config import config

from routes import movie_routes

from database import db

app = Flask(__name__)

# Cors configuration 
# CORS(app, resources={"*" : {"origins" : "http://localhost:5173"}})
# Funcion para las paginas no encontradas 

def page_not_found(error):
    return "<h1>Not Found Page</h1>", 404

if __name__ == "__main__":
    app.config.from_object(config['development'])
    # registramos el blueprints 
    # Como parametro recibe la ruta principal que esta el archivo de rutas y despues un url_prefix para darle un prefijo a
    # la ruta
    app.register_blueprint(movie_routes.main , url_prefix = "/api/v1/movies" )
    # para manejar los errores, se registran los manejadores como lo es la funcion page_not_found
    # Esta pasa como parametro el codigo de estatus y el manejador de error 
    app.register_error_handler(404, page_not_found)
    app.run()