import tkinter as tk
import serial

def conectar():
    global comunicacao
    comunicacao = serial.Serial('COM4', 9600)
    print('Conectado')

def desconectar():
    comunicacao.close()
    print('Desconectado')

def enviar_valor(led, valor):
    # Cria uma string no formato "LED:VALOR" e envia ao Arduino
    codigo = f'{led}:{valor}\n'
    comunicacao.write(codigo.encode())

janela = tk.Tk()
janela.title("Comunicação - Arduino")
janela.geometry('280x470')

botao0 = tk.Button(janela, text='Conectar', command=conectar, width=15, height=2)
botao0.place(x=20, y=20)

botao1 = tk.Button(janela, text='Desconectar', command=desconectar, width=15, height=2)
botao1.place(x=150, y=20)

# LED 1
L1 = tk.Label(text="LED-1")
L1.place(x=100, y=100)

volume = tk.Scale(janela, from_=0, to=255, orient='horizontal')
volume.place(x=90, y=130)

botao = tk.Button(janela, text="Enviar LED 1", command=lambda: enviar_valor(1, volume.get()))
botao.place(x=120, y=180)

# LED 2
L2 = tk.Label(text="LED-2")
L2.place(x=100, y=220)

volume2 = tk.Scale(janela, from_=0, to=255, orient='horizontal')
volume2.place(x=90, y=250)

botao2 = tk.Button(janela, text="Enviar LED 2", command=lambda: enviar_valor(2, volume2.get()))
botao2.place(x=120, y=300)

# LED 3
L3 = tk.Label(text="LED-3")
L3.place(x=100, y=340)

volume3 = tk.Scale(janela, from_=0, to=255, orient='horizontal')
volume3.place(x=90, y=370)

botao3 = tk.Button(janela, text="Enviar LED 3", command=lambda: enviar_valor(3, volume3.get()))
botao3.place(x=120, y=420)

janela.mainloop()


# int valorPWM = 0;

# void setup() {
#   pinMode(11, OUTPUT);
#   pinMode(10, OUTPUT);
#   pinMode(7, OUTPUT);
#   Serial.begin(9600);
# }

# void loop() {
#   if (Serial.available() > 0) {
#     int led = Serial.parseInt();   // Lê o número do LED
#     valorPWM = Serial.parseInt();  // Lê o valor PWM

#     if (led == 1) {
#       analogWrite(11, valorPWM);
#     } else if (led == 2) {
#       analogWrite(10, valorPWM);
#     } else if (led == 3) {
#       analogWrite(7, valorPWM);
#     }
#     else{
#       analogWrite(11, LOW);
#       analogWrite(10, LOW);
#       analogWrite(7, LOW);
#     }
#   }
# }
