import tkinter as tk
from tkinter import messagebox

from database_functions import connect_database, close_connection, fetch_data


def open_window_1():
    window = tk.Toplevel()
    window.title("Inserir")
    window.geometry("500x400")
    window.resizable(False, False)
    window.grab_set()

    # Create a container frame to organize the input fields
    input_frame = tk.Frame(window, padx=20, pady=10)
    input_frame.pack(fill=tk.BOTH, expand=True)

    # Define the input fields with labels
    label_codigo = tk.Label(input_frame, text="Código do material:")
    label_codigo.grid(row=0, column=0, padx=5, pady=5, sticky=tk.W)
    entry_codigo = tk.Entry(input_frame)
    entry_codigo.grid(row=0, column=1, padx=5, pady=5)

    label_material = tk.Label(input_frame, text="Material:")
    label_material.grid(row=1, column=0, padx=5, pady=5, sticky=tk.W)
    entry_material = tk.Entry(input_frame)
    entry_material.grid(row=1, column=1, padx=5, pady=5)

    label_local = tk.Label(input_frame, text="Local:")
    label_local.grid(row=2, column=0, padx=5, pady=5, sticky=tk.W)
    entry_local = tk.Entry(input_frame)
    entry_local.grid(row=2, column=1, padx=5, pady=5)

    label_unidade = tk.Label(input_frame, text="Unidade:")
    label_unidade.grid(row=3, column=0, padx=5, pady=5, sticky=tk.W)
    entry_unidade = tk.Entry(input_frame)
    entry_unidade.grid(row=3, column=1, padx=5, pady=5)

    label_saldo = tk.Label(input_frame, text="Saldo:")
    label_saldo.grid(row=4, column=0, padx=5, pady=5, sticky=tk.W)
    entry_saldo = tk.Entry(input_frame)
    entry_saldo.grid(row=4, column=1, padx=5, pady=5)

    # Create a button frame to organize the buttons
    button_frame = tk.Frame(window, padx=20, pady=10)
    button_frame.pack(fill=tk.BOTH, expand=True)

    # Create the submit and close buttons
    button_submit = tk.Button(button_frame, text="Inserir", bg="#007FFF", fg="white",
                              command=lambda: (submit_item(entry_codigo.get().strip(), entry_material.get(), entry_local.get(),
                                                           entry_unidade.get(), entry_saldo.get()),
                                               entry_codigo.delete(0, tk.END), entry_material.delete(0, tk.END),
                                               entry_local.delete(0, tk.END), entry_unidade.delete(0, tk.END),
                                               entry_saldo.delete(0, tk.END)))
    button_submit.pack(padx=5, pady=5)

    button_close = tk.Button(button_frame, text="Fechar", bg="#DC143C", fg="white", command=window.destroy)
    button_close.pack(side=tk.RIGHT, padx=5, pady=5)

    window.mainloop()


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
