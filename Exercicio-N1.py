import tkinter as tk
from tkinter import*
 
 
def evento_limpar():
    MassaEnt.delete(0, END)
    AlturaEnt.delete(0, END)
    valor.config(text='000-00')
    peso.config(text='NULO')
 
def evento_calcular():
    massa = float(MassaEnt.get())
    Altura = float(AlturaEnt.get())
    imcCalc = (massa/(Altura * Altura))
    valor.config(text=imcCalc)
 
def evento_selecao():
    massa = float(MassaEnt.get())
    Altura = float(AlturaEnt.get())
    imcCalc = (massa/(Altura * Altura))
    if imcCalc < 18.4:
        peso.config(text="Abaixo do peso normal")
    elif imcCalc >= 18.5 and imcCalc <= 24.9:
        peso.config(text="Peso normal")
    elif imcCalc >= 25.0 and imcCalc <= 29.9:
        peso.config(text="Excesso de peso")
    elif imcCalc >= 30.0 and imcCalc <= 34.9:
        peso.config(text="Obesidade classe I")
    elif imcCalc >= 35.0 and imcCalc <= 39.9:
        peso.config(text="Obesidade classe II")
    elif imcCalc >= 40.0:
        peso.config(text="Obesidade classe III")
 
def CalculoeTexto():
    evento_calcular()
    evento_selecao()
 
window = tk.Tk()
window.geometry('250x350')
window.title('Exercicio 18/10')
window.iconbitmap('python.ico')
window.resizable(0,0)
 
imc = LabelFrame(window, text='IMC')
resultado = LabelFrame(window, text='Resultado')
 
 
massa = Label(imc, text="Massa (kg): ")
massa.place(x=10,y=10)
MassaEnt =Entry(window)
MassaEnt.place(x=100, y=39)
 
 
 
altura = Label(imc, text="Altura (M): ")
altura.place(x=10,y=50)
AlturaEnt =Entry(window)
AlturaEnt.place(x=100, y=79)
 
botaoCal = Button(window,text='Calcular' ,command=CalculoeTexto)
botaoCal.place(x=70, y= 110)
botaoLim = Button(window,text='Limpar',command=evento_limpar)
botaoLim.place(x=130, y= 110)
 
altura = Label(imc, text="Altura (M): ")
valor = Label(imc, text="000.00")
valor.place(x=100, y= 120)
 
 
imc.config(borderwidth=1,foreground="red",width=230,height=170)
 
 
peso = Label(resultado, text="NULO")
peso.place(x=80,y=50)
 
resultado.config(borderwidth=1,foreground="red",width=230,height=160)
 
 
 
imc.place(x=10, y=10)
resultado.place(x=10, y=180)
 
 
 
window.mainloop()