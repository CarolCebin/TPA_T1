# Author: Ana carolina Cebin Pereira
# Problema: Vauvau
# Problem ID: vauvau
# Submissao: 

import sys

def dogsAttackVerification(agressiveBehavior, calmBehavior, timeOfArrival):
    
    timeOfArrival =  timeOfArrival % (agressiveBehavior + calmBehavior ) 
    
    print(timeOfArrival)
    
    if ( (timeOfArrival <= agressiveBehavior)  and ( timeOfArrival > 0)):
        
        return 1
    
    return 0


def main():
    #Entrada de Dados
    dogsBehaviors = input().split()
    timeOfArrival = input().split()

    #Conversao para lista de inteiros
    dogsBehaviors = list(map(int, dogsBehaviors))
    timeOfArrival = list(map(int, timeOfArrival))

    templateAnwser = ["none", "one", "both"]
    
    for i in range(len(timeOfArrival)):

        #dogs atack
        dogsAttack = 0

        dogsAttack += dogsAttackVerification(dogsBehaviors[0], dogsBehaviors[1], timeOfArrival[i])
        dogsAttack += dogsAttackVerification(dogsBehaviors[2], dogsBehaviors[3], timeOfArrival[i])

        print("%s" % (templateAnwser[dogsAttack]))

main()
