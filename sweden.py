import random

def sweden():
    mid = '+467'
    prefixe = ['0','1','2','3','6','9']
    mid += prefixe[random.randint(0,(len(prefixe)-1))]
    for n in range (8):
        mid += str(random.randint(0,9))
    print(mid,"\n")
    return mid
