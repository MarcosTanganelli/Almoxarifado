from tkinter import messagebox

import mysql.connector
import openpyxl
from openpyxl.worksheet.table import TableStyleInfo

import config
from sqlalchemy import create_engine
import pandas as pd


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


def tabela_excel():
    conexao = connect_database()
    cursor = conexao.cursor()
    cursor.execute("SELECT * FROM estoque")
    resultados = cursor.fetchall()
    conexao.close()
    df = pd.DataFrame(resultados, columns=cursor.column_names)
    # Exportar o DataFrame para um arquivo Excel
    df.to_excel('firtsteste.xlsx', index=False)
