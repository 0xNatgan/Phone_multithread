import random

def swiss():
    mid = '+417'
    prefixe = ['5','6', '7', '8', '9', '4']
    mid += prefixe[random.randint(0,5)]
    for n in range (7):
        mid += str(random.randint(0,9))
    print(mid,"\n")
    return mid
