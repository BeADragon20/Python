'''
exemplolista = list() #cria lista vazia
print(len(exemplolista)) # retorna numero de elementos da coleção
exemplolista.append('SEG') #adiciona o texto á coleção
print(len(exemplolista))
exemplolista += ['TER','QUAR','QUIN','SEX'] #concatena á coleção mais valores
print(exemplolista)
exemplolista.sort()
print(exemplolista) #Classifica os valores de texto
print(exemplolista[2]) # retorna o terceiro valor da coleção '''

exemplotupla = ('TER','QUAR','QUIN','SEX') #Cria uma tupla
print(len(exemplotupla)) #retorna o número de elementos da coleção
print(exemplotupla) # retorna a coleção de valores
print(exemplotupla[2]) #retorna o terceiro valor da coleção
print('DOM' in exemplotupla)