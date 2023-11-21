import tkinter as tk
from tkinter import ttk
from database_functions import connect_database, close_connection, fetch_data

def criar_tabela(window, tipo_tabela):
    # Destruir a tabela existente, se houver
    for widget in window.winfo_children():
        if isinstance(widget, ttk.Treeview):
            widget.destroy()

    tabela = ttk.Treeview(window, height=1)
    
    if tipo_tabela == "Estoque":
        colunas = ('Codigo Material', 'Material', 'Local', 'Unidade', 'Saldo')
    elif tipo_tabela == "Saida":
        colunas = ('Chamado ID', 'Tecnico', 'Material', 'Area Atual', 'Data', 'Codigo')

    tabela['columns'] = colunas

    # Configuração das colunas
    for coluna in tabela['columns']:
        tabela.column(coluna, anchor=tk.CENTER, width=100)
        tabela.heading(coluna, text=coluna)

    # Adicione os dados à tabela
    conn = connect_database()

    if tipo_tabela == "Estoque":
        result = fetch_data(conn, "SELECT cod_mat, material, local, unidade, saldo FROM estoque")
    elif tipo_tabela == "Saida":
        result = fetch_data(conn, "SELECT chamado_id, tecnico, material, area_atuacao, data, codigo FROM saida")
    
    close_connection(conn)

    for row in result:
        tabela.insert("", "end", values=row)  # Insira cada linha na tabela

    # Coloque a tabela na janela
    tabela.pack(fill="both", expand=True)

def open_tabela():
    window = tk.Toplevel()
    window.title("Tabela")
    window.geometry("800x600")
    window.grab_set()
    label_tabela = tk.Label(window, text="Selecione a tabela:")
    label_tabela.pack()
    tipos_tabelas = ["Estoque", "Saida"]
    combo_tipo_tabela = ttk.Combobox(window, values=tipos_tabelas)
    combo_tipo_tabela.pack()

    def on_selecionar_tabela():
        tipo_selecionado = combo_tipo_tabela.get()
        criar_tabela(window, tipo_selecionado)

    botao_selecionar = tk.Button(window, text="Selecionar Tabela", command=on_selecionar_tabela)
    botao_selecionar.pack()

    window.mainloop()

