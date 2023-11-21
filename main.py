import tkinter as tk
from view import pageExcel, pageInserir, pageRemover, pageTabela
from PIL import Image, ImageTk
from database_functions import connect_database


def main(credencial):
    janela = tk.Tk()
    janela.geometry("600x400")
    janela.title("Almoxarifado")

    # estilo uniforme da fonte
    fonte_padrao = ("Arial", 14)

    # adicione espaço em branco entre os botões
    espaco_entre_botoes = 20

    # escolha cores de contraste para tornar os botões mais fáceis de identificar
    cor_botao_1 = "#66CC66"
    cor_botao_2 = "#CC6666"
    cor_botao_3 = "#66CCCC"
    cor_botao_4 = '#FFA500'
    cor_cinza   = '#CCCCCC'
    #if credencial == 1: fazer logica de acesso
    # adicione botões com ícones ou texto
    if credencial == 1:
        button_1 = tk.Button(janela, text="Inserir Item", font=fonte_padrao, bg=cor_botao_1, width=20, height=2,
                             command=pageInserir.open_window_1)
        button_1.place(x=170, y=50)

        button_2 = tk.Button(janela, text="Remover Item", font=fonte_padrao, bg=cor_botao_2, width=20, height=2,
                             command=pageRemover.open_window_2)
        button_2.place(x=170, y=100 + espaco_entre_botoes)

        button_3 = tk.Button(janela, text="Excel", font=fonte_padrao, bg=cor_botao_3, width=20, height=2,
                             command=pageExcel.open_window_3)
        button_3.place(x=170, y=150 + 2 * espaco_entre_botoes)

        button_4 = tk.Button(janela, text="Tabela", font=fonte_padrao, bg=cor_botao_4, width=20, height=2,
                             command=pageTabela.open_tabela)
        button_4.place(x=170, y=220 + 2 * espaco_entre_botoes)
    else:
        button_1 = tk.Button(janela, text="Inserir Item", font=fonte_padrao, bg=cor_cinza, width=20, height=2)
        button_1.place(x=170, y=50)

        button_2 = tk.Button(janela, text="Remover Item", font=fonte_padrao, bg=cor_cinza, width=20, height=2)
        button_2.place(x=170, y=100 + espaco_entre_botoes)

        button_3 = tk.Button(janela, text="Excel", font=fonte_padrao, bg=cor_cinza, width=20, height=2)
        button_3.place(x=170, y=150 + 2 * espaco_entre_botoes)

        button_4 = tk.Button(janela, text="Tabela", font=fonte_padrao, bg=cor_botao_4, width=20, height=2,
                             command=pageTabela.open_tabela)
        button_4.place(x=170, y=220 + 2 * espaco_entre_botoes)

    janela.mainloop()

def login():
    global credencial
    janela = tk.Tk()
    janela.title("Login")
    janela.geometry("200x200")
    janela.grab_set()

    # Labels
    label_username = tk.Label(janela, text="Usuário:")
    label_username.pack()
    entry_username = tk.Entry(janela)
    entry_username.pack()

    label_password = tk.Label(janela, text="Senha:")
    label_password.pack()
    entry_password = tk.Entry(janela, show="*")
    entry_password.pack()

    label_resultado = tk.Label(janela, text="")
    label_resultado.pack()
    
    def realizar_login_padrao():
        global credencial 
        credencial = 0
        janela.destroy()

    def realizar_login():
        global credencial

        # Conectar ao banco de dados
        db = connect_database()

        # Obter o cursor para executar as consultas SQL
        cursor = db.cursor()

        # Obter as entradas do usuário
        username = entry_username.get()
        password = entry_password.get()

        # Consulta SQL para verificar se o usuário e a senha correspondem
        query = "SELECT username, password, credencial FROM usuarios WHERE username = %s AND password = %s"
        values = (username, password)
        cursor.execute(query, values)
        result = cursor.fetchone()

        # Verificar se há um resultado válido
        if result:
            _, _, credencial = result
            # fazer credencial mudar querry_n = "select credenecial from usuarios where username = %s AND password = %s"
            janela.destroy()
        else:
            label_resultado['text'] = "Login falhou!"

        # Fechar a conexão com o banco de dados
        cursor.close()
        db.close()

    button_login = tk.Button(janela, text="Acessar", command=realizar_login)
    button_login.pack()

    button_login_padrao = tk.Button(janela, text="Entrar como visitante", command=realizar_login_padrao)
    button_login_padrao.pack()

    janela.mainloop()
    return credencial

if __name__ == "__main__":
    credencial = login()
    main(credencial)
    


