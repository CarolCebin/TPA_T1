# Author: Ana Carolina Cebin Pereira
# Problema: Sort of Sorting
# Problem ID: sortofsorting
# Submissao: 6015860

import sys

#Entrada de Dados
for line in sys.stdin:
    
    #Divide a linha em duas strings seprardas por espaço
    numbers = line.split();
    
    #encontra a diferença absoluta com a funçao abs e transformando as strings para inteiros
    result = abs( int(numbers[0]) - int(numbers[1]) )
    
    #exibe o resultado
    print(result)
