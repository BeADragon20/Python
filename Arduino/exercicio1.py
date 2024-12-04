# ------------------------+
# Gustavo Carvalho - 9594 |
# Catia Cilene - 9627     |
# ------------------------+
import tkinter as tk
from tkinter import*
import serial

def conectar():
    global comunicacao
    comunicacao = serial.Serial('COM4','9600')
    print('conectado')
    
def desconectar():
    comunicacao.close()
    print('desconectado')
    
def Liga_LED1():
    codigo = 'a'
    comunicacao.write(codigo.encode())
    
def Desliga_LED1():
    codigo = 'b'
    comunicacao.write(codigo.encode())
    
def Liga_LED2():
    codigo = 'c'
    comunicacao.write(codigo.encode())
    
def Desliga_LED2():
    codigo = 'd'
    comunicacao.write(codigo.encode())

def Liga_LED3():
    codigo = 'e'
    comunicacao.write(codigo.encode())
    
def Desliga_LED3():
    codigo = 'f'
    comunicacao.write(codigo.encode())
    
janela = tk.Tk()
janela.title("Comunicação - Arduino")
janela.geometry('480x170')

botao0 = Button(janela, text='Conectar', command=conectar, width=15, height=2)
botao0.place(x=20, y=20)

botao1 = Button(janela, text='Desconectar', command=desconectar, width=15, height=2)
botao1.place(x=150, y=20)

botao2 = Button(janela, text='Ligar LED 1', command=Liga_LED1, width=15, height=1, bg='#FF8888')
botao2.place(x=20, y=90)

botao3 = Button(janela, text='Desligar LED 1', command=Desliga_LED1, width=15, height=1, bg='#FF8888')
botao3.place(x=20, y=120)

botao4 = Button(janela, text='Ligar LED 2', command=Liga_LED2, width=15, height=1, bg='#88FF88')
botao4.place(x=150, y=90)

botao5 = Button(janela, text='Desligar LED 2', command=Desliga_LED2, width=15, height=1, bg='#88FF88')
botao5.place(x=150, y=120)

botao6 = Button(janela, text='Ligar LED 3', command=Liga_LED3, width=15, height=1, bg='#bb00ff')
botao6.place(x=300, y=90)

botao7 = Button(janela, text='Desligar LED 3', command=Desliga_LED3, width=15, height=1, bg='#bb00ff')
botao7.place(x=300, y=120)

janela.mainloop()

