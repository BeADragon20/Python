import tkinter as tk
from tkinter import ttk
import serial

arduino = serial.Serial('COM4', 9600, timeout=1)

def ligar_led():
    arduino.write(b'L')

def desligar_led():
    arduino.write(b'D')

def ligar_buzzer():
    freq = int(entry_freq.get())
    arduino.write(f'B{freq}'.encode())

def desligar_buzzer():
    arduino.write(b'B0')

def ler_ldr():
    arduino.write(b'R') 
    if arduino.in_waiting > 0:
        valor_ldr = arduino.readline().decode().strip()
        label_ldr.config(text=f"Valor do LDR: {valor_ldr}")
    janela.after(1000, ler_ldr)

janela = tk.Tk()
janela.title("Controle Arduino")
janela.geometry('210x270')

btn_led_on = ttk.Button(janela, text="Ligar LED", command=ligar_led)
btn_led_on.place(x=10, y=10)

btn_led_off = ttk.Button(janela, text="Desligar LED", command=desligar_led)
btn_led_off.place(x=110, y=10)

btn_buzzer_on = ttk.Button(janela, text="Ligar Buzzer", command=ligar_buzzer)
btn_buzzer_on.place(x=10, y=50)

btn_buzzer_off = ttk.Button(janela, text="Desligar Buzzer", command=desligar_buzzer)
btn_buzzer_off.place(x=110, y=50)

label_freq = ttk.Label(janela, text="Frequência do Buzzer:")
label_freq.place(x=10, y=90)

entry_freq = ttk.Entry(janela)
entry_freq.place(x=10, y=120)

label_ldr = ttk.Label(janela, text="Valor do LDR: ")
label_ldr.place(x=10, y=150)

janela.after(1000, ler_ldr)

janela.mainloop()
