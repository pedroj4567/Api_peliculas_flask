# Aqui se refleja los datos de la tabla como si fuera un modelo 
# Asi creamos un esquema de modulo de datos a usar 
from utils.Dataformat import Dataformat

class Movie () :
    def __init__(self, id, title = None, duration=None , released = None) -> None:
        self.id = id
        self.title = title
        self.duration = duration
        self.released = released
        
    # Creamos un metodo para que retorne nuestro modelo como un json 
    def to_JSON (self) :
        return {
            "id" : self.id,
            "title" : self.title,
            "duration" : self.duration,
            "released" : Dataformat.convert_date(self.released)
        } 