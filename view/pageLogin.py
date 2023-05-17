import tkinter as tk
from database_functions import connect_database


def open_window_login():
    window = tk.Toplevel()
    window.title("Login")
    window.geometry("200x200")
    window.grab_set()
    window.iconbitmap("C:/Users/Marco/Desktop/Estagio/Almoxarifado/imgs/perfil.ico")

    # Labels
    label_username = tk.Label(window, text="Usuário:")
    label_username.pack()
    entry_username = tk.Entry(window)
    entry_username.pack()

    label_password = tk.Label(window, text="Senha:")
    label_password.pack()
    entry_password = tk.Entry(window, show="*")
    entry_password.pack()

    label_resultado = tk.Label(window, text="")
    label_resultado.pack()

    button_login = tk.Button(window, text="Acessar", command=lambda: realizar_login(entry_username, entry_password, label_resultado, window))
    button_login.pack()


def realizar_login(entry_username, entry_password, label_resultado, window):
    # Conectar ao banco de dados
    db = connect_database()

    # Obter o cursor para executar as consultas SQL
    cursor = db.cursor()

    # Obter as entradas do usuário
    username = entry_username.get()
    password = entry_password.get()

    # Consulta SQL para verificar se o usuário e a senha correspondem
    query = "SELECT * FROM usuarios WHERE username = %s AND password = %s"
    values = (username, password)
    cursor.execute(query, values)

    # Verificar se há um resultado válido
    if cursor.fetchone():
        label_resultado['text'] = "Login bem-sucedido!"
        window.destroy()
    else:
        label_resultado['text'] = "Login falhou!"

    # Fechar a conexão com o banco de dados
    cursor.close()
    db.close()
