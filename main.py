import tkinter as tk
from window_functions import  open_window_2
import pageInserir
from database_functions import connect_database, close_connection, fetch_data

def main():
    # Crie a janela principal
    janela = tk.Tk()

    janela.geometry("600x400")

    # Adicione um título à janela
    janela.title("Almoxarifado")

    button_1 = tk.Button(janela, text="Inserir Item", width=10, height=1, command=pageInserir.open_window_1)
    button_1.place(x=50, y=20)

    button_2 = tk.Button(janela, text="Remover Item", width=10, height=1, command=open_window_2)
    button_2.place(x=128, y=20)
    # Inicie o loop principal da interface
    janela.mainloop()

if __name__ == "__main__":
    main()
