def soma(a,b):
    resultado = a+b
    return resultado
 
def subtracao(a,b):
    resultado = a-b
    return resultado
 
def multiplicacao(a,b):
    resultado = a*b
    return resultado
 
def divisao(a,b):
    resultado = a/b
    return resultado
try:
    num1 = input('Digite o 1° número: ')
    while num1.isnumeric() == False:
        num1 = input('Digite o 1° número (NÃO DIGITE LETRA): ')
    num1 = int(num1)
    
    num2 = input('Digite o 2° número: ')
    while num2.isnumeric() == False:
        num2 = input('Digite o 2° número (NÃO DIGITE LETRA): ')
    num2 = int(num2)
    
    print('1-soma')
    print('2-subtração')
    print('3-multiplicação')
    print('4-divisão')
    opcao=input('Digite a opção escolhida:')
    
    if opcao == "1":
        print("O resultado da soma é: {}".format(soma(num1,num2)))
    if opcao == "2":
        print("O resultado da subtração é: {}".format(subtracao(num1,num2)))
    if opcao == "3":
        print("O resultado da multiplicação é: {}".format(multiplicacao(num1,num2)))
    if opcao == "4":
        print("O resultado da divisão é: {}".format(divisao(num1,num2)))

except:
    print('DEU ERRO OTARIO')