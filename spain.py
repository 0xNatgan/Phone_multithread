import random

def spain():
    mid = '+346'
    for n in range (8):
        mid += str(random.randint(0,9))
    print(mid,"\n")
    return mid
