import random

def french():
    mid = '+33'
    mid += str(random.randint(6,7))
    for n in range (7):
        mid += str(random.randint(0,9))
    return mid
