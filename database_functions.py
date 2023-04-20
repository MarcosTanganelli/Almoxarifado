import mysql.connector
import config

def connect_database():
    conexao = mysql.connector.connect(
        host=config.DB_HOST,
        user=config.DB_USER,
        password=config.DB_PASSWORD,
        database=config.DB_NAME
    )
    return conexao

def close_connection(conexao):
    conexao.close()

def fetch_data(conexao):
    cursor = conexao.cursor()
    cursor.execute('SELECT * FROM estoque')
    resultados = cursor.fetchall()
    return resultados
