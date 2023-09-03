import tkinter as tk
from view import pageExcel, pageInserir, pageRemover, pageLogin
from PIL import Image, ImageTk


def main():
    janela = tk.Tk()
    janela.geometry("600x400")
    janela.title("Almoxarifado")

    # janela.iconbitmap("C:/Users/Marco/Desktop/Estagio/Almoxarifado/imgs/1434728.ico")

    # estilo uniforme da fonte
    fonte_padrao = ("Arial", 14)

    # adicione espaço em branco entre os botões
    espaco_entre_botoes = 20

    # escolha cores de contraste para tornar os botões mais fáceis de identificar
    cor_botao_1 = "#66CC66"
    cor_botao_2 = "#CC6666"
    cor_botao_3 = "#66CCCC"
    cor_botao_4 = "#808080"

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

    # imagem = Image.open("C:/Users/Marco/Desktop/Estagio/Almoxarifado/imgs/perfil.ico")

    # Redimensionar a imagem se necessário
    # imagem = imagem.resize((25, 25), Image.LANCZOS)

    # Converter a imagem para o formato Tkinter
    # imagem_tk = ImageTk.PhotoImage(imagem)

    # Criar o widget Label para exibir a imagem
    #label_imagem = tk.Label(janela, image=imagem_tk)
    #label_imagem.place(x=460, y=0)

    button_4 = tk.Button(janela,  font=fonte_padrao, bg=cor_botao_4, width=25, height=25, compound="center",
                         command=pageLogin.open_window_login)
    button_4.place(x=500, y=0)

    janela.mainloop()

if __name__ == "__main__":
    main()
