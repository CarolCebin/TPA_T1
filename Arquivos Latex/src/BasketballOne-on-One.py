# Author: Ana carolina Cebin Pereira
# Problema: Basketball One-on-One
# Problem ID: basketballoneonone
# Submissao: 6017807

import sys

#Inicializacao de variaveis 
playerA = 0
playerB = 0

#Entrada de dados
recordGame = input()

#Percorre a lista com o incremento de 2
for jogada in range(0,len(recordGame), 2):
    
    #Verifica de qual jogador foi a jogada
    player = recordGame[jogada]
    #verifica qual a pontuacao da jogada
    points = int(recordGame[jogada + 1])

    #Adiciona a pontuacao da jogada para o jogador 
    if (player == 'A'):
        playerA += points
    else:
        playerB += points 
    
#Verifica e exibe o ganhador
if (playerA > playerB ):
    print('A')
else:
    print('B')