import random

def australia():
    mid = '+614'
    for n in range (8):
        mid += str(random.randint(0,9))
    print(mid,"\n")
    return mid
