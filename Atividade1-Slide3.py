def soma(a,b):
    return a+b
def sub(a,b):
    return a-b
def mult(a,b):
    return a*b
def div(a,b):
    return a/b

Funcao = input("Digite o tipo de conta que você quer: ")

if(Funcao == "Soma"):
    print('A Soma é: {}'.format(soma(int(input('Digite o Valor da A: ')),int(input('Digite o Valor da B: ')))))
    
if(Funcao == "Subtração"):
    print('A Subtração é: {}'.format(sub(int(input('Digite o Valor da A: ')),int(input('Digite o Valor da B: ')))))

if(Funcao == "Multiplicação"):
    print('A Multiplicação é: {}'.format(mult(int(input('Digite o Valor da A: ')),int(input('Digite o Valor da B: ')))))

if(Funcao == "Divisão"):
    print('A Divisão é: {}'.format(div(int(input('Digite o Valor da A: ')),int(input('Digite o Valor da B: ')))))


