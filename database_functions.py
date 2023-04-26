from tkinter import messagebox

import mysql.connector
import openpyxl
from openpyxl.worksheet.table import TableStyleInfo
from tkinter import filedialog
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


def tabela_excel(txt):
    try:
        conexao = connect_database()
        cursor = conexao.cursor()
        cursor.execute(txt)
        resultados = cursor.fetchall()
        conexao.close()
        df = pd.DataFrame(resultados, columns=cursor.column_names)
        # Exportar o DataFrame para um arquivo Excel
        destino = filedialog.asksaveasfilename(defaultextension='.xlsx')
        df.to_excel(destino, index=False)
        messagebox.showinfo("Sucesso", f"Arquivo  salvo com sucesso!")
    except Exception as e:
        messagebox.showerror("Erro", f"Não foi possível gerar o arquivo: {str(e)}")


def inserir_banco_excel():
    try:
        conexao = connect_database()
        cursor = conexao.cursor()

        filetypes = [("Arquivos Excel", "*.xlsx")]
        file_path = filedialog.askopenfilename(filetypes=filetypes)
        if file_path is None:
            messagebox.showerror("Erro", "Nenhum arquivo selecionado.")
            return

        dados_excel = pd.read_excel(file_path)
        # Loop através dos dados e inserir no banco de dados MySQL
        for index, row in dados_excel.iterrows():
            query = "INSERT IGNORE INTO estoque (cod_mat, material, local, unidade, saldo) VALUES (%s, %s, %s, %s, %s)"
            valores = (row['cod_mat'], row['material'], row['local'], row['unidade'], row['saldo'])
            cursor.execute(query, valores)
        # Confirmar as mudanças no banco de dados MySQL
        conexao.commit()
        # Fechar a conexão com o banco de dados MySQL
        cursor.close()
        conexao.close()
        messagebox.showinfo("Sucesso", f"Banco de dados alterado com sucesso")
    except Exception as e:
        messagebox.showerror("Erro", f"Não foi possível gerar o arquivo: {str(e)}")


