import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from database_functions import connect_database, close_connection, fetch_data

linha_id = 0

def update_combobox_values(entry_search, combo):
    global selected_option
    # Obtenha o texto digitado na Entry
    search_text = entry_search.get()
    # Conecte-se ao banco de dados
    conn = connect_database()
    # Busque uma lista de códigos de materiais que correspondam ao texto digitado na tabela "estoque"
    result = fetch_data(conn, f"SELECT cod_mat FROM estoque WHERE cod_mat LIKE '%{search_text}%'")
    # Feche a conexão com o banco de dados
    close_connection(conn)
    # Atualize os valores da combobox com base nos resultados da pesquisa
    combo['values'] = result


def open_window_2():
    window = tk.Toplevel()
    window.title("Remover")
    window.geometry("600x400")

    label = tk.Label(window, text="Buscar:")
    label.pack(padx=10, pady=10)

    # Adicione um widget Entry e um botão "Buscar"
    entry_search = tk.Entry(window)
    entry_search.pack(padx=10, pady=10)
    button_search = tk.Button(window, text="Buscar", command=lambda: update_combobox_values(entry_search, combo))
    button_search.pack(padx=10, pady=10)

    # Crie uma combobox para exibir os resultados da pesquisa
    combo = ttk.Combobox(window, state="readonly")
    combo.pack(padx=10, pady=10)

    # Conecte-se ao banco de dados
    conn = connect_database()

    # Busque uma lista de códigos de materiais na tabela "estoque"
    result = fetch_data(conn, "SELECT cod_mat FROM estoque")
    # Feche a conexão com o banco de dados
    close_connection(conn)

    # Adicione os códigos de materiais à propriedade "values" da Combobox
    combo['values'] = result
    # combo.get() -> da o item selecionado
    tabela = ttk.Treeview(window, height=1)
    tabela['columns'] = ('Codigo Material', 'Material', 'Local', 'Unidade', 'Saldo')
    tabela.column('#0', width=0, stretch=tk.NO)
    tabela.column('Codigo Material', anchor=tk.CENTER, width=100)
    tabela.column('Material', anchor=tk.CENTER, width=100)
    tabela.column('Local', anchor=tk.CENTER, width=100)
    tabela.column('Unidade', anchor=tk.CENTER, width=100)
    tabela.column('Saldo', anchor=tk.CENTER, width=100)

    tabela.heading('#0', text='')
    tabela.heading('Codigo Material', text='Codigo Material')
    tabela.heading('Material', text='Material')
    tabela.heading('Local', text='Local')
    tabela.heading('Unidade', text='Unidade')
    tabela.heading('Saldo', text='Saldo')

    def exibir_tabela(event):
        global linha_id
        if linha_id != 0:
            tabela.delete(linha_id - 1)
        valor_selecionado = combo.get()
        conn = connect_database()
        result = fetch_data(conn, f"SELECT * FROM estoque WHERE cod_mat = '{valor_selecionado}' ")
        close_connection(conn)
        tabela.insert(parent='', index='end', text='', iid = linha_id, values=(result[0][0], result[0][1], result[0][2], result[0][3], result[0][4]))
        tabela.pack()
        if linha_id == 0:
            label_quantidade = tk.Label(window, text="Quantidade:")
            label_quantidade.pack()
            entry_quantidade = tk.Entry(window, validate="key", vcmd=(window.register(validate_int), "%P"))
            entry_quantidade.pack()
            button_submit = tk.Button(window, text="Remover",
                                      command=lambda: submit_item(entry_quantidade.get(), valor_selecionado))
            button_submit.pack()
        linha_id += 1

    # Adicione o evento à combobox
    combo.bind('<<ComboboxSelected>>', exibir_tabela)
    def validate_int(input):
        if input.isdigit():
            return True
        else:
            return False

  #  button_close = tk.Button(window, text="Fechar", command=window.destroy)

    def close_window():
        global linha_id
        linha_id = 0
        window.destroy()

    button_close = tk.Button(window, text="Fechar", command=close_window)

    button_close.pack(side=tk.BOTTOM, pady=10)

def submit_item(quantidade, valor_selecionado):
    try:
        conexao = connect_database()
        cursor = conexao.cursor()
        sql = f"UPDATE estoque SET saldo = saldo - {quantidade} WHERE cod_mat = {valor_selecionado}"
        cursor.execute(sql)
        conexao.commit()
        close_connection(conexao)
        messagebox.showinfo("Remoção bem sucedida", "Item removido com sucesso!")
    except Exception as e:
        messagebox.showerror("Erro ao Remover", f"Não foi possível remover o item. Erro: {e}")
