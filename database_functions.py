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

def fetch_data(conexao, mysql_txt = None):
    cursor = conexao.cursor()
    if mysql is None:
        cursor.execute('SELECT * FROM estoque')
    else:
        cursor.execute(mysql_txt)
    resultados = cursor.fetchall()
    return resultados
