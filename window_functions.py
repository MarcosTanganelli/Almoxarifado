import tkinter as tk

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
