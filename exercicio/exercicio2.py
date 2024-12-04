import tkinter as tk
from tkinter import ttk, messagebox



janela = tk.Tk() #Cria uma nova janela da interface
janela.geometry('425x550') #Personaliza o tamanho da interface
janela.resizable(0,0)
janela.config(background=None) #Remove a cor de fundo da janela
janela.title('Aplicação e botão e LED numa Raspberry Pi')

imagem = tk.PhotoImage(file='Screenshot_2.png') #Define um objeto tipo imagem para aplicação


labelImagem = tk.Label(janela, image=imagem) #Ferramenta Label que irá apresentar a imagem
labelImagem.place(x = 0, y = 0, relwidth = 1.0, relheight = 1.0)# Tamanho relativo do Label à janela


janela.mainloop()

