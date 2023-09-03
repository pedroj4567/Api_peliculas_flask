"""
Este es el archivo de configuracion del servidor 
WSGI de flask
"""

from decouple import config

class Config : 
    # Con el metodo config puedo acceder a las variables de entorno
    SECRET_KEY = config("SECRET_KEY")

class DevelopmentConfig (Config) :
    DEBUG = True
    
config = {
    'development' : DevelopmentConfig
}