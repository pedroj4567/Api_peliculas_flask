import psycopg2
from psycopg2 import DatabaseError 
from decouple import config

def get_conecction () :
    try:
        return psycopg2.connect(
            host = config("DATABASE_HOST"),
            user = config("DATABASE_USER"),
            password = config("DATABASE_PASSWORD"),
            database = config("DATABASE_NAME"),
            
        )
    except DatabaseError as ex: 
        raise ex