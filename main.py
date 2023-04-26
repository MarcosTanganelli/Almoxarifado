import tkinter as tk
import database_functions
import pageRemover
import pageInserir


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

    # adicione botões com ícones ou texto
    button_1 = tk.Button(janela, text="Inserir Item", font=fonte_padrao, bg=cor_botao_1, width=20, height=2,
                         command=pageInserir.open_window_1)
    button_1.place(x=170, y=50)

    button_2 = tk.Button(janela, text="Remover Item", font=fonte_padrao, bg=cor_botao_2, width=20, height=2,
                         command=pageRemover.open_window_2)
    button_2.place(x=170, y=100 + espaco_entre_botoes)

    button_3 = tk.Button(janela, text="Exportar para Excel", font=fonte_padrao, bg=cor_botao_3, width=20, height=2,
                         command=database_functions.tabela_excel)
    button_3.place(x=170, y=150 + 2 * espaco_entre_botoes)

    janela.mainloop()


if __name__ == "__main__":
    main()
