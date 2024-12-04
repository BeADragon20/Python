import tkinter as tk
from tkinter import *  
from tkinter import messagebox



# POSIÇÃO DA JANELA 

window = tk.Tk()
window.geometry('300x250')
window.title('CALCULADORA IMC')

# Campo de entrada

Label(window, text='Peso (Kg):').place(x=50, y=30)
entrada_peso = Entry(window)
entrada_peso.place(x=150, y=30)



Label(window, text='Altura (m):').place(x=50, y=60)
entrada_altura = Entry(window)
entrada_altura.place(x=150, y=60)



def salvar_imc():
    global imc
    try:
        with open('Dados' + '.txt','w') as arquivo:
            arquivo.write(entrada_peso.get()+'\n')
            arquivo.write(entrada_altura.get()+'\n')
            arquivo.write(str(imc)+'\n')
            arquivo.write(resultado_class.cget("text"))
        print('Dado escrito')
    except:
        messagebox.showerror(title="Erro", message="Cálculo não realizado!")
        
def carregar_imc():
    global imc
    with open('dados' + '.txt','r') as arquivo:
        peso = arquivo.readline()
        altura = arquivo.readline()
        imc = arquivo.readline()
        classificacao = arquivo.readline()

    entrada_peso.insert(0,peso)
    entrada_altura.insert(0,altura)
    resultado_imc.config(text="imc: {:.2f}".format(float(imc)))
    resultado_class.config(text=classificacao)

# CALCULO IMC
def calcular_imc():
    global imc
    peso = float(entrada_peso.get())  
    altura = float(entrada_altura.get())  
    imc = peso / (altura ** 2)  
    resultado_imc.config(text=f'IMC: {imc:.2f}') 

    # DEFINE A CLASSIFICAÇÃO
    if imc < 18.5:
        resultado_class.config(text='Abaixo do peso')

    elif 18.5 <= imc <= 24.9:
        resultado_class.config(text='Peso normal')

    elif 25.0 <= imc <= 29.9:
        resultado_class.config(text='Excesso de peso')

    elif 30.0 <= imc <= 34.9:
        resultado_class.config(text='Obesidade 1')

    elif 35.0 <= imc <= 39.9:
        resultado_class.config(text='Obesidade 2')

    else:
        resultado_class.config(text='Obesidade 3')



# LIMPAR OS CAMPOS

def limpar():
    entrada_peso.delete(0, END)  
    entrada_altura.delete(0, END)  
    resultado_imc.config(text='')  
    resultado_class.config(text='')    





# Botões

botao_calcular = Button(window, text='Calcular', command=calcular_imc)
botao_calcular.place(x=100, y=100)


botao_limpar = Button(window, text='Limpar', command=limpar)
botao_limpar.place(x=200, y=100)

botao_salvar = Button(window, text='Salvar', command=salvar_imc)
botao_salvar.place(x=150, y=160)

botao_carregar = Button(window, text='Carregar', command=carregar_imc)
botao_carregar.place(x=143, y=190)

# Campo de saida

resultado_imc = Label(window, text='')
resultado_imc.place(x=50, y=140)


resultado_class = Label(window, text='')
resultado_class.place(x=150, y=140)


window.mainloop()