import random

def uk():
    mid = '+447'
    for n in range (9):
        mid += str(random.randint(0,9))
    print(mid,"\n")
    return mid
