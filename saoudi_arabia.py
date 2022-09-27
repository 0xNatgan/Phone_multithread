import random

def saoudi_arabia():
    mid = '+9975'
    for n in range (8):
        mid += str(random.randint(0,9))
    print(mid,"\n")
    return mid
