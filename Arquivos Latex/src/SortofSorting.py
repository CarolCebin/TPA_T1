# Author: Ana Carolina Cebin Pereira
# Problema: Sort of Sorting
# Problem ID: sortofsorting
# Submissao: 6025325

import sys

numberOfNames = int(input())

while numberOfNames > 0:
    names = []
    for i in range(numberOfNames):
        names.append(input())
        
    names.sort(key = lambda x: x[:2])

    print('\n', *names, sep='\n')

    numberOfNames = int(input())
