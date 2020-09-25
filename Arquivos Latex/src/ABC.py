# Author: Ana carolina Cebin Pereira
# Problema: ABC 
# Problem ID: abc
# Submissao: 6017747

import sys

#inicialização de variavel
orderDisired = []

#Entrada de Dados
inputNumbers = input().split();
orderDisiredString = input();

#converte a lista de strings para inteiros
numbers = list(map(int, inputNumbers))

#Ordena a lista de inteiros 
numbers.sort()

#Cria o vetor com os indices e a ordem de impressao
for i in range(len(orderDisiredString)):
    orderDisired.append( int(ord(orderDisiredString[i])) - 65)

#imprime o resultado usando o vetor com indices de impressao
for i in orderDisired:
    print("%s" % (numbers[i]) , end = ' ' )
