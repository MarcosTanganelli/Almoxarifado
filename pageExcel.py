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
    window.geometry("900x800")
    window.configure(bg="#F4F4F4")

    config_frame = tk.Frame(window, bg="#F4F4F4", padx=20, pady=20)
    config_frame.pack(side="left", anchor="nw")

    title_label = tk.Label(config_frame, text="Configurações para gerar excel de saída:", font=("Arial", 14), bg="#F4F4F4", fg="#333")
    title_label.grid(row=0, column=0, columnspan=2, sticky="w", pady=10)

    date_label = tk.Label(config_frame, text="Início:", font=("Arial", 12), bg="#F4F4F4", fg="#333")
    date_label.grid(row=1, column=0, sticky="w", pady=5)

    date_entry = DateEntry(config_frame, date_pattern='dd/mm/yyyy', show_week_numbers=False, font=("Arial", 12))
    date_entry.grid(row=1, column=1, sticky="w", pady=5)

    date_label1 = tk.Label(config_frame, text="Saída:", font=("Arial", 12), bg="#F4F4F4", fg="#333")
    date_label1.grid(row=2, column=0, sticky="w", pady=5)

    date_entry1 = DateEntry(config_frame, date_pattern='dd/mm/yyyy', show_week_numbers=False, font=("Arial", 12))
    date_entry1.grid(row=2, column=1, sticky="w", pady=5)

    current_date = datetime.now().date()
    one_month_ago = current_date - timedelta(days=30)
    date_entry1.set_date(one_month_ago)

    submit_button = tk.Button(config_frame, text="Gerar", bg="#66CCCC", fg="white", font=("Arial", 12),
                              command=lambda: tabela_excel(f"SELECT * FROM saida WHERE data BETWEEN '{datetime.strptime(date_entry1.get(), '%d/%m/%Y').strftime('%Y-%m-%d')}' AND '{datetime.strptime(date_entry.get(), '%d/%m/%Y').strftime('%Y-%m-%d')}'"))
    submit_button.grid(row=3, column=0, columnspan=2, pady=20)

    title_label1 = tk.Label(config_frame, text="Configurações para gerar excel com todos elementos:", font=("Arial", 14), bg="#F4F4F4", fg="#333")
    title_label1.grid(row=4, column=0, columnspan=2, sticky="w", pady=10)

    ger_label = tk.Label(config_frame, text="Estoque:", font=("Arial", 12), bg="#F4F4F4", fg="#333")
    ger_label.grid(row=5, column=0, sticky="w", pady=5)

    generate_button = tk.Button(config_frame, text="Gerar", font=("Arial", 12),
                              command=lambda: tabela_excel(f"SELECT * FROM estoque "))
    generate_button.grid(row=5, column=1, pady=10)

    ger_label1 = tk.Label(config_frame, text="Saida:", font=("Arial", 12), bg="#F4F4F4", fg="#333")
    ger_label1.grid(row=5, column=2, sticky="w", pady=5)

    generate_button1 = tk.Button(config_frame, text="Gerar", font=("Arial", 12),
                                 command=lambda: tabela_excel(f"SELECT * FROM saida "))
    generate_button1.grid(row=5, column=3, pady=10)

    title_label2 = tk.Label(config_frame, text="Configurações para enviar excel:")
    title_label2.grid(row=6, column=0, columnspan=2, sticky="w")

    enviar_label = tk.Label(config_frame, text="Enviar excel de estoque:")
    enviar_label.grid(row=7, column=0, sticky="w")
    enviar_button = tk.Button(config_frame, text="Enviar",
                               command=lambda: database_functions.atualizar_banco_excel())
    enviar_button.grid(row=7, column=1, pady=10)

    enviar_label1 = tk.Label(config_frame, text="Enviar excel de saída:")
    enviar_label1.grid(row=7, column=2, sticky="w")
    enviar_button1 = tk.Button(config_frame, text="Enviar",
                                command=lambda: database_functions.atualizar_banco_saida_excel())
    enviar_button1.grid(row=7, column=3, columnspan=2, pady=10)
