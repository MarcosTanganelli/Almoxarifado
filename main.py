import tkinter as tk
from view import pageExcel, pageInserir, pageRemover, pageTabela
from PIL import Image, ImageTk
from database_functions import connect_database



credencial = 0
def realizar_login(entry_username, entry_password, label_resultado, window):
        # Conectar ao banco de dados
        db = connect_database()

        # Obter o cursor para executar as consultas SQL
        cursor = db.cursor()

        # Obter as entradas do usuário
        username = entry_username.get()
        password = entry_password.get()

        # Consulta SQL para verificar se o usuário e a senha correspondem
        query = "SELECT * FROM usuarios WHERE username = %s AND password = %s"
        values = (username, password)
        cursor.execute(query, values)

        # Verificar se há um resultado válido
        if cursor.fetchone():
            # fazer credencial mudar 
            window.destroy()
            main()
        else:
            label_resultado['text'] = "Login falhou!"

        # Fechar a conexão com o banco de dados
        cursor.close()
        db.close()

def main():
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
    cor_botao_4 = "#808080"
    #if credencial == 1: fazer logica de acesso
    # adicione botões com ícones ou texto
    button_1 = tk.Button(janela, text="Inserir Item", font=fonte_padrao, bg=cor_botao_1, width=20, height=2,
                         command=pageInserir.open_window_1)
    button_1.place(x=170, y=50)

    button_2 = tk.Button(janela, text="Remover Item", font=fonte_padrao, bg=cor_botao_2, width=20, height=2,
                         command=pageRemover.open_window_2)
    button_2.place(x=170, y=100 + espaco_entre_botoes)

    button_3 = tk.Button(janela, text="Excel", font=fonte_padrao, bg=cor_botao_3, width=20, height=2,
                         command=pageExcel.open_window_3)
    button_3.place(x=170, y=150 + 2 * espaco_entre_botoes)

    button_3 = tk.Button(janela, text="Tabela", font=fonte_padrao, bg=cor_botao_3, width=20, height=2,
                         command=pageTabela.open_tabela)
    button_3.place(x=170, y=150 + 2 * espaco_entre_botoes)
    janela.mainloop()

def login():
    janela = tk.Tk()
    janela.title("Login")
    janela.geometry("200x200")
    janela.grab_set()
    # janela.iconbitmap("C:/Users/Marco/Desktop/Estagio/Almoxarifado/imgs/perfil.ico")

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

    button_login = tk.Button(janela, text="Acessar", command=lambda: realizar_login(entry_username, entry_password, label_resultado, janela))
    button_login.pack()
    janela.mainloop()


if __name__ == "__main__":
    login()
    


