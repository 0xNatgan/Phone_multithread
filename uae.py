import random

def uae():
    mid = '+9715'
    prefixe = ['0', '5']
    mid += prefixe[random.randint(0,1)]
    for n in range (7):
        mid += str(random.randint(0,9))
    print(mid,"\n")
    return mid
