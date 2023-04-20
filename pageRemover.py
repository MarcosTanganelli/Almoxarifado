import tkinter as tk
from tkinter import ttk
import pandas as pd
from pandastable import Table, TableModel
from tkinter import messagebox

from database_functions import connect_database, close_connection, fetch_data

def update_combobox_values(entry_search, combo):
    global selected_option
    # Obtenha o texto digitado na Entry
    search_text = entry_search.get()
    # Conecte-se ao banco de dados
    conn = connect_database()
    # Busque uma lista de códigos de materiais que correspondam ao texto digitado na tabela "estoque"
    result = fetch_data(conn, f"SELECT cod_mat FROM estoque WHERE cod_mat LIKE '%{search_text}%'")
    # Feche a conexão com o banco de dados
    close_connection(conn)
    # Atualize os valores da combobox com base nos resultados da pesquisa
    combo['values'] = result

def open_window_2():
    window = tk.Toplevel()
    window.title("Remover")
    window.geometry("600x400")

    label = tk.Label(window, text="Local de Remover")
    label.pack(padx=10, pady=10)

    # Adicione um widget Entry e um botão "Buscar"
    entry_search = tk.Entry(window)
    entry_search.pack(padx=10, pady=10)
    button_search = tk.Button(window, text="Buscar", command=lambda: update_combobox_values(entry_search, combo))
    button_search.pack(padx=10, pady=10)

    # Crie uma combobox para exibir os resultados da pesquisa
    combo = ttk.Combobox(window, state="readonly")
    combo.pack(padx=10, pady=10)

    # Conecte-se ao banco de dados
    conn = connect_database()

    # Busque uma lista de códigos de materiais na tabela "estoque"
    result = fetch_data(conn, "SELECT cod_mat FROM estoque")
    # Feche a conexão com o banco de dados
    close_connection(conn)

    # Adicione os códigos de materiais à propriedade "values" da Combobox
    combo['values'] = result
    #combo.get() -> da o item selecionado

    button_close = tk.Button(window, text="Fechar", command=window.destroy)
    button_close.pack(padx=10, pady=10)


