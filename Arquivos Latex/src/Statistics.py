# Author: Ana carolina Cebin Pereira
# Problema: Statistics
# Problem ID: statistics
# Submissao: 6019065

import sys

#inicializacao da variavel para controle do numero de casos
numberCase = 0

#Lê ate o final do arquivo
for line in sys.stdin:
    
    #entrada de dados
    sampleData = line.split();

    #incrementa a variavel de controle de casos
    numberCase +=1

    #Converte as strings para inteiros 
    sampleData = list(map(int, sampleData))

    #Remove o primeiro item
    del sampleData[0]

    #ordena os valores da amostra
    sampleData.sort()

    #Atribui os valores
    minValue = sampleData[0]
    maxValue = sampleData[len(sampleData) - 1]
    
    #Calcula o range da amostra de dados
    rangeValue = maxValue - minValue

    print("Case %d: %d %d %d" % (numberCase, minValue, maxValue, rangeValue))