import tkinter as tk
from tkinter import*


window = tk.Tk()
window.geometry('350x350')
window.title('Exercicio 25/10')
window.resizable(0,0)


imagem9594 = PhotoImage(file='Screenshot_1.png') 
labelImagem = Label(window = tk.Tk(), image=imagem9594) #Ferramenta Label que irá apresentar a imagem
labelImagem.place(x = 0, y = 0, relwidth = 1.0, relheight = 1.0)# Tamanho relativo do Label à janela

cmd_user = tk.Button(window, image = imagem9594,border = 0)
cmd_user.place(x = 142, y = 4) #Localização do canto  superior esquerdo da ferramenta

window.mainloop()


