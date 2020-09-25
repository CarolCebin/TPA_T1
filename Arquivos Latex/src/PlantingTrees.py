# Author: Ana Carolina Cebin Pereira
# Problema: Planting Trees
# Problem ID: plantingtrees
# Submissao: 6025252

import sys

numberOfSeedlings = int(input())

daysToGrow = input().split()

daysToGrow = list(map(int, daysToGrow))

daysToGrow.sort(reverse = True)

maxGrowth = 0

for i in range(numberOfSeedlings):

    daysToGrow[i] += i + 2
    if (maxGrowth < daysToGrow[i]):
        maxGrowth = daysToGrow[i]


print(maxGrowth)