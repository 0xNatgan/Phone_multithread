import random

def finland():
    mid = '+3584'
    for n in range (9):
        mid += str(random.randint(0,9))
    print(mid,"\n")
    return mid
