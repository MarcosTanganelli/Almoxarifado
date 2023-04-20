import tkinter as tk
import mysql.connector

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

janela.geometry("500x300")

# Adicione um título à janela
janela.title("Minha Interface")

# Crie um botão
botao = tk.Button(janela, text="Clique aqui!")

# Adicione o botão à janela
botao.pack()

# Inicie o loop principal da interface
janela.mainloop()
