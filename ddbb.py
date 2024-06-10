# Datos de Conexion
import psycopg2

db_host = '127.0.0.1'
db_port = 5432
db_user = 'postgres'
db_pass = '1234'
dbname = 'dinobase'


def get_db_connection():
    db_connection = psycopg2.connect(
        dbname=dbname,
        user=db_user,
        host=db_host,
        password=db_pass,
        port=db_port,
        client_encoding='utf8'
    )
    return db_connection

def createSaurio(jsonsaurio):
    connection = None
    try:
        connection = get_db_connection()
        if not connection:
            return False
        cursor = connection.cursor()
        query = """INSERT INTO dinosaurios(nombresaurio,dinopoder,dinoedad,dinoalimentacion) values(%(nombreSaurio)s,%(poder)s,%(dinoAge)s,%(alimentacion)s)"""
        cursor.execute(query, jsonsaurio)
        connection.commit()

        if cursor.rowcount > 0:
            return True
    except Exception as e :
        print("error al insertar dinosaurio")
    finally:
        if connection is not None:
            connection.close()