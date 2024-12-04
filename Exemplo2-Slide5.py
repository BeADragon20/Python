import tkinter as tk
from tkinter import ttk #Acesso as ferramentas

window = tk.Tk()
window.iconbitmap('python.ico')
window.title('Nova Janela')
window.resizable(1,1)

texto1 = ttk.Label(window,
                   text='Este é meu primeiro texto...')
texto1.pack() #Montagem de posicionamento
window.geometry('400x200')
window.mainloop()