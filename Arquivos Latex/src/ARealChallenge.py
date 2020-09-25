# Author: Ana carolina Cebin Pereira
# Problema: A Real Challenge
# Problem ID: areal
# Submissao: 6017929

import sys
import math

#Entrada de dados
area = int(input())

#Calcula o perimeto da area
perimeter = (math.sqrt(area)) * 4

#Imprime o tamanho da cerca nessesario para o pasto
print("%f" % (perimeter))