import tkinter as tk
from tkinter import*

def acao_entrada(event):
    texto1.config(text=entrada.get())
def acao_botao1():
    texto1.config(text='')

window = tk.Tk()
window.geometry('400x200')
window.title('Nova janela')
window.resizable(1,1)
 
texto1 = Label(window,text='Este é meu primeiro texto')
texto1.place(x=120,y=80)
botao1 = Button(window,text='Apagar!',command=acao_botao1)
botao1.place(x=160, y= 110)
 
entrada =Entry(window)
entrada.bind('<Return>',acao_entrada)
entrada.place(x=140, y=30) 
window.mainloop()