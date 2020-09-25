# Author: Ana carolina Cebin Pereira
# Problema: Odd Man Out
# Problem ID: oddmanout
# Submissao: 6018054

import sys

#Entrada de dados de dados
numberOfCases = int(input())

for i in range(numberOfCases):
    numberGuests = int(input())
    invitationCodes = input().split();

    #inicializacao de variavel
    tickets = []
    
    #Percorre a lista que contem os codigos dos convites
    for ticket in invitationCodes:
        #Se o codigo do convite ja existe, entao o codigo eh removido, Caso contrario, pode
        if ticket in tickets:
            tickets.remove(ticket)
        else:
            tickets.append(ticket)
    #Exibe o numero do caso, junto com o numero do convidado que esta sozinho
    print("Case #%d: %s" % (i+1, tickets[0]))