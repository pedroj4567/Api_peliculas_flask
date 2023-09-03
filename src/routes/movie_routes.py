from flask import Blueprint, jsonify, request
import uuid
# entities 
from models.entities.movie import Movie

from models.movie_model import MovieModel
main = Blueprint("movie_blueprint", __name__)

# decorador para la ruta principal
# ruta listar o get
@main.route("/")
def get_movies ():
    try:
        # obtenemos las peliculas desde el modelo 
        movies = MovieModel.get_movies()
        return jsonify(movies)
        
    except Exception as ex : 
        return jsonify({"message" : str(ex)}), 500
    
@main.route('/<id>')
def get_movie (id) :
    try:
        # obtenemos las peliculas desde el modelo 
        movie = MovieModel.get_movie(id)
        if movie != None:
            return jsonify(movie)
        else: 
            return jsonify({}), 404
        

    except Exception as ex : 
        return jsonify({"message" : str(ex)}), 500
    
@main.route('/add', methods=["POST"])
def add_movie () :
    try:
        
        id = uuid.uuid4()
        title = request.json["title"]
        duration = int(request.json["duration"])
        released = request.json["released"]
        
        movie = Movie(str(id), title,duration,released)
        
        affectedRow = MovieModel.add_movie(movie)
        
        if affectedRow == 1 :
            return jsonify(movie.id)
        else:
            return jsonify({"message" : "Error in insert"}), 500
            
       
    except Exception as ex : 
        return jsonify({"message" : str(ex)}), 500

@main.route('/delete/<id>', methods=["DELETE"])
def delete_movie (id) :
    try:
        movie = Movie(id)
        
        affectedRow = MovieModel.delete_movie(movie)
        
        if affectedRow == 1 :
            return jsonify({"message" : "Movie deleted successfully" , "error" : False}), 200
        else:
            return jsonify({"message" : "Movie not found"}), 404
            
       
    except Exception as ex : 
        return jsonify({"message" : str(ex)}), 500
    

@main.route("/update/<id>", methods=["PUT"])
def update_movie(id):
    try:
        # datos nuevos enviados desde el cliente 
        title = request.json["title"]
        duration = int(request.json["duration"])
        released = request.json["released"]

        # creamos un nuevo objeto desde la entidad 
        movie = Movie(id, title, duration, released )
        
        affected_row = MovieModel.update_movie(movie)
        
        if affected_row == 1:
            return jsonify(movie.id)
        else : 
            return jsonify({"message" : "Fail on update row"}), 404
        
    except Exception as ex:
        return jsonify({"message" : str(ex)}), 500