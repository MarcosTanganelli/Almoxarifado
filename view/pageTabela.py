import tkinter as tk
from tkinter import ttk
from database_functions import connect_database, close_connection, fetch_data

def open_tabela():
    window = tk.Toplevel()
    window.title("Tabela")
    window.geometry("800x600")
    window.grab_set()

    tree = ttk.Treeview(window, columns=("CODIGO", "MATERIAL", "LOCAL", "UNIDADE", "SALDO"), height=1)  # Substitua pelos nomes reais das colunas

    # Defina os cabeçalhos das colunas
    tree.heading("#1", text="CODIGO")
    tree.heading("#2", text="MATERIAL")
    tree.heading("#3", text="LOCAL")
    tree.heading("#4", text="UNIDADE")
    tree.heading("#5", text="SALDO")


    # Adicione os dados à tabela
    conn = connect_database()
    result = fetch_data(conn, "SELECT cod_mat, material, local, unidade, saldo FROM estoque")
    close_connection(conn)

    for row in result:
        tree.insert("", "end", values=row)  # Insira cada linha na tabela

    # Coloque a tabela na janela
    tree.pack(fill="both", expand=True)
