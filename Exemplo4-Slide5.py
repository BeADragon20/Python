import tkinter as tk
from tkinter import ttk #Acesso as ferramentas

window = tk.Tk()

window.iconbitmap('python.ico')
window.title('Nova Janela')
window.resizable(1,1)

texto1 = ttk.Label(window,
                   text='Este é meu primeiro texto...')
texto1.place(x=120,y=80) #Montagem de posicionamento


def acao_botao1():
    texto1.config(text='O comando foi acionado')
botao1 = ttk.Button(window, text='Clique aqui',
                    command=acao_botao1)
botao1.place(x=160,y=100)


window.geometry('400x200')
window.mainloop()