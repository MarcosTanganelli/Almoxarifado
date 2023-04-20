import tkinter as tk
import pageRemover
import pageInserir


def main():
    # Crie a janela principal
    janela = tk.Tk()

    janela.geometry("600x400")

    # Adicione um título à janela
    janela.title("Almoxarifado")

    button_1 = tk.Button(janela, text="Inserir Item", width=10, height=1, command=pageInserir.open_window_1)
    button_1.place(x=50, y=20)

    button_2 = tk.Button(janela, text="Remover Item", width=10, height=1, command=pageRemover.open_window_2)
    button_2.place(x=128, y=20)
    # Inicie o loop principal da interface
    janela.mainloop()

if __name__ == "__main__":
    main()
