import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

import database_functions
from database_functions import connect_database, fetch_data, tabela_excel
from datetime import datetime
from tkcalendar import DateEntry
from datetime import datetime, timedelta


def open_window_3():
    window = tk.Toplevel()
    window.title("Excel")
    window.geometry("800x600")
    window.grab_set()

    config_frame = tk.Frame(window, padx=10, pady=10)
    config_frame.pack(side="left", anchor="nw")

    title_label = tk.Label(config_frame, text="Configurações para gerar excel de saída:")
    title_label.grid(row=0, column=0, columnspan=2, sticky="w")

    date_label = tk.Label(config_frame, text="Início:")
    date_label.grid(row=1, column=0, sticky="w")

    date_entry = DateEntry(config_frame, date_pattern='dd/mm/yyyy', show_week_numbers=False)
    date_entry.grid(row=1, column=1, sticky="w")

    date_label1 = tk.Label(config_frame, text="Saída:")
    date_label1.grid(row=2, column=0, sticky="w")

    date_entry1 = DateEntry(config_frame, date_pattern='dd/mm/yyyy', show_week_numbers=False)
    date_entry1.grid(row=2, column=1, sticky="w")

    current_date = datetime.now().date()
    one_month_ago = current_date - timedelta(days=30)
    date_entry1.set_date(one_month_ago)

    submit_button = tk.Button(config_frame, text="Gerar", bg="#66CCCC", fg="white",
                              command=lambda: tabela_excel(f"SELECT * FROM saida WHERE data BETWEEN '{datetime.strptime(date_entry1.get(), '%d/%m/%Y').strftime('%Y-%m-%d')}' AND '{datetime.strptime(date_entry.get(), '%d/%m/%Y').strftime('%Y-%m-%d')}'"))
    submit_button.grid(row=3, column=0, columnspan=2, pady=10)

    title_label1 = tk.Label(config_frame, text="Configurações para gerar excel com todos elementos:")
    title_label1.grid(row=4, column=0, columnspan=2, sticky="w")

    ger_label = tk.Label(config_frame, text="Estoque:")
    ger_label.grid(row=5, column=0, sticky="w")

    generate_button = tk.Button(config_frame, text="Gerar",
                              command=lambda: tabela_excel(
                                  f"SELECT * FROM estoque "))
    generate_button.grid(row=5, column=0, columnspan=2, pady=10)

    ################

    ger_label1 = tk.Label(config_frame, text="Saida:")
    ger_label1.grid(row=5, column=2, sticky="w")

    generate_button1 = tk.Button(config_frame, text="Gerar",
                                command=lambda: tabela_excel(
                                    f"SELECT * FROM saida "))
    generate_button1.grid(row=5, column=3, columnspan=2, pady=10)

    ###################################

    enviar_label = tk.Label(config_frame, text="Enviar excel:")
    enviar_label.grid(row=6, column=0, sticky="w")

    enviar_button = tk.Button(config_frame, text="Gerar",
                                 command=lambda: database_functions.inserir_banco_excel())
    enviar_button.grid(row=6, column=0, columnspan=2, pady=10)