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
    window.geometry("800x600")
    window.grab_set()

    label_codigo = tk.Label(window, text="Código de Material:", font=("Arial", 12), pady=10, padx=10)
    label_codigo.pack()

    # Criar o quadro para o campo de pesquisa e botão "Buscar"
    frame_search = tk.Frame(window)
    frame_search.pack(pady=5)
    entry_search = tk.Entry(frame_search, font=("Arial", 12), width=20)
    entry_search.pack(side=tk.LEFT)
    button_search = tk.Button(frame_search, text="Buscar", font=("Arial", 12),
                              command=lambda: update_combobox_values(entry_search, combo))
    button_search.pack(side=tk.LEFT, padx=5)

    # Criar a combobox para exibir os resultados da pesquisa
    combo = ttk.Combobox(window, state="readonly", font=("Arial", 12), width=30)
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
    tabela.column('Material', anchor=tk.CENTER, width=300)
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
        tabela.insert(parent='', index='end', text='', iid=linha_id,
                      values=(result[0][0], result[0][1], result[0][2], result[0][3], result[0][4]))
        tabela.pack()
        if linha_id == 0:
            label_saida = tk.Label(window, text="Configuração de Saída", font=("Arial", 14), pady=10, padx=10)
            label_saida.pack()

            # Criar o rótulo e campo para "Número Chamado"
            frame_nrochmdo = tk.Frame(window)
            frame_nrochmdo.pack(pady=5)
            label_nrochmdo = tk.Label(frame_nrochmdo, text="Número Chamado:", font=("Arial", 12), width=15)
            label_nrochmdo.pack(side=tk.LEFT)
            entry_nrochmdo = tk.Entry(frame_nrochmdo, font=("Arial", 12))
            entry_nrochmdo.pack(side=tk.LEFT)

            # Criar o rótulo e campo para "Área de Atuação"
            frame_aatcao = tk.Frame(window)
            frame_aatcao.pack(pady=5)
            label_aatcao = tk.Label(frame_aatcao, text="Área de Atuação:", font=("Arial", 12), width=15)
            label_aatcao.pack(side=tk.LEFT)
            entry_aatcao = tk.Entry(frame_aatcao, font=("Arial", 12))
            entry_aatcao.pack(side=tk.LEFT)

            # Criar o rótulo e campo para "Técnico"
            frame_tecnico = tk.Frame(window)
            frame_tecnico.pack(pady=5)
            label_tecnico = tk.Label(frame_tecnico, text="Técnico:", font=("Arial", 12), width=15)
            label_tecnico.pack(side=tk.LEFT)
            entry_tecnico = tk.Entry(frame_tecnico, font=("Arial", 12))
            entry_tecnico.pack(side=tk.LEFT)

            # Criar o rótulo e campo para "Descrição"
            frame_descricao = tk.Frame(window)
            frame_descricao.pack(pady=5)
            label_descricao = tk.Label(frame_descricao, text="Descrição:", font=("Arial", 12), width=15)
            label_descricao.pack(side=tk.LEFT)
            entry_descricao = tk.Entry(frame_descricao, font=("Arial", 12))
            entry_descricao.pack(side=tk.LEFT)

            frame_quantidade = tk.Frame(window)
            frame_quantidade.pack(pady=5)
            label_quantidade = tk.Label(frame_quantidade, text="Quantidade:", font=("Arial", 12), width=15)
            label_quantidade.pack(side=tk.LEFT)
            entry_quantidade = tk.Entry(frame_quantidade, font=("Arial", 12))
            entry_quantidade.pack(side=tk.LEFT)
            button_submit = tk.Button(window, text="Remover", bg="#CC6666", font=("Arial", 14),
                                      command=lambda: (button_submit_callback(entry_nrochmdo.get(), entry_aatcao.get(),
                                                                             entry_tecnico.get(), entry_descricao.get(),
                                                                             combo.get(), entry_quantidade.get()),
                                                    entry_nrochmdo.delete(0, tk.END), entry_aatcao.delete(0, tk.END),
                                                    entry_tecnico.delete(0, tk.END), entry_descricao.delete(0, tk.END),
                                                    entry_quantidade.delete(0, tk.END)))

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
        sql = f"UPDATE estoque SET saldo = saldo - {quantidade} WHERE cod_mat = '{valor_selecionado}'"
        cursor.execute(sql)
        conexao.commit()
        close_connection(conexao)
        messagebox.showinfo("Remoção bem sucedida", "Item removido com sucesso!")
    except Exception as e:
        messagebox.showerror("Erro ao Remover", f"Não foi possível remover o item. Erro: {e}")


def submit_saida(nro_chamado, aatcao, tecnico, descricao, valor_selecionado):
    try:
        conexao = connect_database()
        cursor = conexao.cursor()

        sql = f"INSERT INTO saida (chamado_id, tecnico, material, area_atuacao, data, codigo) VALUES ({nro_chamado}, '{tecnico}', '{descricao}', '{aatcao}', NOW(), '{valor_selecionado}')"
        cursor.execute(sql)
        conexao.commit()
        close_connection(conexao)
    except Exception as e:
        messagebox.showerror("Erro ao Remover", f"Não foi possível remover o item. Erro: {e}")

def button_submit_callback(entry_nrochmdo, entry_aatcao, entry_tecnico, entry_descricao,valor_selecionado, entry_quantidade):
    try:
        submit_saida(entry_nrochmdo, entry_aatcao, entry_tecnico, entry_descricao, valor_selecionado)
        submit_item(entry_quantidade, valor_selecionado)
    except Exception as e:
        messagebox.showerror("Erro", f"Ocorreu um erro: {e}")