import tkinter as tk
from  tkinter import messagebox

root = tk.Tk()
root.title("Jogo Da Velha")
root.resizable(False , False)

player_atual = 'X'
botoes = []
mapa_do_jogo = ["","","","","","","","",""]


def Resetar_Jogo():
    global  player_atual , mapa_do_jogo
    mapa_do_jogo = ["","","","","","","","",""]
    player_atual = "X"
    for botao in botoes:
        botao.config(text = "", state=tk.NORMAL)

def Mostrar_vencedor(vencedor):
    messagebox.showinfo('O vencedor do jogo e o : ' , vencedor)
    Resetar_Jogo()

def validar_vencedor():
    condicoes_de_vitoria = [(0,1,2),(3,4,5), (6,7,8),
                            (0,3,6) , (1,4,7) , (2,5,8) ,
                            (0,4,8) , (2,4,6)]
    for condicao in condicoes_de_vitoria:
        if mapa_do_jogo[condicao[0]] == mapa_do_jogo[condicao[1]] == mapa_do_jogo[condicao[2]] != "":
            Mostrar_vencedor(mapa_do_jogo[condicao[0]])
            return True
        if "" not in mapa_do_jogo:
            messagebox.showinfo('Fim de Jogo Empate', 'O jogo terminou em empate!')
            Resetar_Jogo()
            return  True
    return  False
def click(index):
    global player_atual
    if mapa_do_jogo[index] == "":
        mapa_do_jogo[index] = player_atual
        botoes[index].config(text = player_atual, state=tk.DISABLED)
        if not validar_vencedor():
            player_atual = "0" if player_atual == 'X' else 'X'

for i in range(9):
    botao = tk.Button(root, text="", font=('normal', 40), width=5, height=2,
                       command=lambda i=i: click(i))
    botao.grid(row=i//3, column=i%3)
    botoes.append(botao)


botao_resetar = tk.Button(root, text="Reiniciar", command=Resetar_Jogo)
botao_resetar.grid(row=3, column=0, columnspan=3)


root.mainloop()