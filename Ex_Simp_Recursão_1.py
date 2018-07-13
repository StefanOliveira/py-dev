#Exemplo simples recursão

def listsum(numList):
    theSum = 0
    for i in numList:
        theSum += i
    return theSum

print(listsum([1,3,5,7,9]))
