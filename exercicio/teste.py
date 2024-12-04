import tkinter as tk
from tkinter import ttk, messagebox

def acaoLED(): #Função que apresenta mensagem com informações sobre o componente eletrônico LED
    messagebox.showinfo(title='LED',message='Curso Técnico \n em Informática.')#Apresenta janela de mensagem

def acaoBotao(*args):
    print(args)
    messagebox.showinfo(title='Chave táctil',message='Este é um botão.')
    
def acaoResistor():
    messagebox.showinfo(title='Resistor',message='Este é um resistor.\n'+
                        'Ele tem a função de limitar a corrente elétrica da alimentação do LED',
                        icon='error')

def acaoProcessador():
    messagebox.showinfo(title='Processador',message='Este é o microcontrolador da Raspberry Pi.')

def acaoAlimentacao():
    messagebox.showinfo(title='Alimentação',message='Este é o conector de alimentação da Raspberry Pi.'+
                        ' Tensão de alimentação de 5V, capacidade recomendada de 3A. Conector tipo microUSB')

def acaoJ8():
    messagebox.showinfo(title='J8 - Bloco de acesso aos IOs',message='Este é o conector de acesso aos IOs da Raspberry Pi.')

def acaoHDMI():
    messagebox.showinfo(title='Conector HDMI',
                        message='Este é o conector de áudio e vídeo pelo padrão HDMI.\n' +
                        ' Para a Raspberry Pi 4 este conector é o microHDMI')

janela = tk.Tk() #Cria uma nova janela da interface
janela.geometry('425x550') #Personaliza o tamanho da interface
janela.resizable(0,0)
janela.config(background=None) #Remove a cor de fundo da janela
janela.title('Aplicação e botão e LED numa Raspberry Pi')

imagem = tk.PhotoImage(file='9594.png') #Define um objeto tipo imagem para aplicação
imgLED = tk.PhotoImage(file='LED_VM.png')
imgBotao = tk.PhotoImage(file='ChaveTactil.png')
imgResistor = tk.PhotoImage(file='Res100Ohms.png')
imgProcessador = tk.PhotoImage(file='BCM2837.png')
imgAlimentacao = tk.PhotoImage(file='RaspPi_PowerSupply.png')
imgJ8 = tk.PhotoImage(file='RaspPi_J8.png')
imgHDMI = tk.PhotoImage(file='RaspPi_HDMI.png')

labelImagem = tk.Label(janela, image=imagem) #Ferramenta Label que irá apresentar a imagem
labelImagem.place(x = 0, y = 0, relwidth = 1.0, relheight = 1.0)# Tamanho relativo do Label à janela

cmd_LED = tk.Button(janela, image = imgLED, command = acaoLED, border = 0)
cmd_LED.place(x = 142, y = 4) #Localização do canto  superior esquerdo da ferramenta
cmd_Botao = tk.Button(janela, image = imgBotao, command = lambda: acaoBotao("Este é um parâmetro"), border = 0)
cmd_Botao.place(x = 45, y = 111)
cmd_Resistor = tk.Button(janela, image = imgResistor, command = acaoResistor, border = 0)
cmd_Resistor.place(x = 155, y = 112)
cmd_Processador = tk.Button(janela, image = imgProcessador, command = acaoProcessador, border = 0)
cmd_Processador.place(x = 106, y = 364)
cmd_Alimentacao = tk.Button(janela, image = imgAlimentacao, command = acaoAlimentacao, border = 0)
cmd_Alimentacao.place(x = 52, y = 509)
cmd_J8 = tk.Button(janela, image = imgJ8, command = acaoJ8, border = 0)
cmd_J8.place(x = 53, y = 293)
cmd_HDMI = tk.Button(janela, image = imgHDMI, command = acaoHDMI, border = 0)
cmd_HDMI.place( x= 127, y = 485)
janela.mainloop()