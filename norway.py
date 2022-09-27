import random

def norway():
    mid = '+47'
    prefixe = ['4','9']
    mid += prefixe[random.randint(0,(len(prefixe)-1))]
    for n in range (7):
        mid += str(random.randint(0,9))
    print(mid,"\n")
    return mid
