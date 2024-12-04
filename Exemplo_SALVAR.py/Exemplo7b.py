#Escrever dados em um arquivo externo:
with open('Dados' + '.txt','w') as arquivo:
    arquivo.write('teste')
print('Dado escrito')

#Ler dados de um arquivo externo:
with open('dados' + '.txt','r') as arquivo:
    linha_lida = arquivo.readline()
print('Dados lidos: '+linha_lida)