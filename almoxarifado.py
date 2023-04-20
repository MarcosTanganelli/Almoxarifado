import tkinter as tk
import mysql.connector
def open_window_1():
    window = tk.Toplevel()
    window.title("Inserir")
    window.geometry("200x100")

    label = tk.Label(window, text="Local de inserir")
    label.pack()

    button_close = tk.Button(window, text="Fechar", command=window.destroy)
    button_close.pack()

def open_window_2():
    window = tk.Toplevel()
    window.title("Remover")
    window.geometry("200x100")

    label = tk.Label(window, text="Local de Remover")
    label.pack()

    button_close = tk.Button(window, text="Fechar", command=window.destroy)
    button_close.pack()

conexao = mysql.connector.connect(
    host="localhost",
    user="root",
    password="gviwfw89",
    database="almoxarifado"
)
cursor = conexao.cursor()
cursor.execute('SELECT * FROM estoque')
resultados = cursor.fetchall()
print(resultados)
conexao.close()

# Crie a janela principal
janela = tk.Tk()

janela.geometry("600x400")

# Adicione um título à janela
janela.title("Almoxarifado")

button_1 = tk.Button(janela, text="Inserir Item", width=10, height=1, command=open_window_1)

button_1.place(x=50, y=20)

button_2 = tk.Button(janela, text="Remover Item", width=10, height=1, command=open_window_2)

button_2.place(x=128, y=20)
# Inicie o loop principal da interface
janela.mainloop()
