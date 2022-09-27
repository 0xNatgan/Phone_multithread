import random

def qatar():
    mid = '+974'
    prefixe = ['33','55','66','77']
    mid += prefixe[random.randint(0,(len(prefixe)-1))]
    for n in range (6):
        mid += str(random.randint(0,9))
    print(mid,"\n")
    return mid
