from database.db import get_conecction
from .entities.movie import Movie

class MovieModel ():
    
    # Para instaciar la clase sin necesidad de instaciar en otro lado se usa el classMethod
    @classmethod
    def get_movies(self):
        try:
            connection = get_conecction()
            movies = [] 
            
            # Se apertura una transaccion hacia la bd
            with connection.cursor() as cursor :
                cursor.execute("SELECT id, title, duration, released from movies ORDER BY title ASC")
                results = cursor.fetchall()
                
                for row in results:
                    movie = Movie(row[0],row[1],row[2],row[3])
                    movies.append(movie.to_JSON())
                    
            # una vez hecha la operacion, se cierra el cursor
            connection.close()
            return movies
        
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def get_movie(self, id):
        try:
            connection = get_conecction()
            # Se apertura una transaccion hacia la bd
            with connection.cursor() as cursor :
                cursor.execute("SELECT id, title, duration, released from movies WHERE id = %s", (id,))
                row = cursor.fetchone()
                movie = None
                
                if row != None:
                    movie = Movie(row[0],row[1],row[2],row[3])
                    movie = movie.to_JSON()
                
            # una vez hecha la operacion, se cierra el cursor
            connection.close()
            return movie
        
        except Exception as ex:
            raise Exception(ex)



    @classmethod
    def add_movie(self, movie):
        try:
            connection = get_conecction()
            # Se apertura una transaccion hacia la bd
            with connection.cursor() as cursor :
                cursor.execute("""INSERT INTO movies ( id, title, duration, released)
                               VALUES (%s , %s , %s, %s)""", (movie.id, movie.title, movie.duration, movie.released))
                # verificamos cuantas filas son afectadas 
                # return 1 si existe una nueva row
                affected_row = cursor.rowcount 
                # confirmamos este cambio 
                connection.commit()
                
            connection.close()
            return affected_row
        
        except Exception as ex:
            raise Exception(ex)
        
    @classmethod
    def delete_movie(self, movie):
        try:
            connection = get_conecction()
            # Se apertura una transaccion hacia la bd
            with connection.cursor() as cursor :
                cursor.execute("""DELETE FROM movies WHERE id = %s""", (movie.id,))
                # verificamos cuantas filas son afectadas 
                # return 1 si existe una nueva row
                affected_row = cursor.rowcount 
                # confirmamos este cambio 
                connection.commit()
                
            connection.close()
            return affected_row
        
        except Exception as ex:
            raise Exception(ex)
        
    @classmethod
    def update_movie(self, movie):
        try:
            connection = get_conecction()
            # Se apertura una transaccion hacia la bd
            with connection.cursor() as cursor :
                cursor.execute("""UPDATE movies SET title = %s, duration = %s, released = %s
                                    WHERE id = %s""", (movie.title,movie.duration,movie.released,movie.id))
                # verificamos cuantas filas son afectadas 
                # return 1 si existe una nueva row
                affected_row = cursor.rowcount 
                # confirmamos este cambio 
                connection.commit()
                
            connection.close()
            return affected_row
        
        except Exception as ex:
            raise Exception(ex)