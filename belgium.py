import random

def belgium():
    mid = '+324'
    for n in range (8):
        mid += str(random.randint(0,9))
    print(mid,"\n")
    return mid
