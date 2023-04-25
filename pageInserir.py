import tkinter as tk
from tkinter import messagebox

from database_functions import connect_database, close_connection, fetch_data


def open_window_1():
    window = tk.Toplevel()
    window.title("Inserir")
    window.geometry("500x500")
    window.grab_set()

    label_codigo = tk.Label(window, text="Código do material:")
    label_codigo.pack()
    entry_codigo = tk.Entry(window)
    entry_codigo.pack()

    label_material = tk.Label(window, text="Material:")
    label_material.pack()
    entry_material = tk.Entry(window)
    entry_material.pack()

    label_local = tk.Label(window, text="Local:")
    label_local.pack()
    entry_local = tk.Entry(window)
    entry_local.pack()

    label_unidade = tk.Label(window, text="Unidade:")
    label_unidade.pack()
    entry_unidade = tk.Entry(window)
    entry_unidade.pack()

    label_saldo = tk.Label(window, text="Saldo:")
    label_saldo.pack()
    entry_saldo = tk.Entry(window)
    entry_saldo.pack()

    # Crie o botão de submissão
    button_submit = tk.Button(window, text="Inserir",
                              command=lambda: (submit_item(
                                  entry_codigo.get(), entry_material.get(), entry_local.get(),
                                  entry_unidade.get(), entry_saldo.get()
                              ),
                                               entry_codigo.delete(0, tk.END), entry_material.delete(0, tk.END),
                                               entry_local.delete(0, tk.END), entry_unidade.delete(0, tk.END),
                                               entry_saldo.delete(0, tk.END)))
    button_submit.pack()

    # Crie o botão de fechar
    button_close = tk.Button(window, text="Fechar", command=window.destroy)
    button_close.pack()


def submit_item(codigo, material, local, unidade, saldo):
    try:
        conexao = connect_database()
        cursor = conexao.cursor()
        sql = "INSERT INTO estoque (cod_mat, material, local, unidade, saldo) VALUES (%s, %s, %s, %s, %s)"
        values = (codigo, material, local, unidade, saldo)
        cursor.execute(sql, values)
        conexao.commit()
        close_connection(conexao)
        messagebox.showinfo("Inserção bem sucedida", "Item inserido com sucesso!")
    except Exception as e:
        messagebox.showerror("Erro ao inserir", f"Não foi possível inserir o item. Erro: {e}")
