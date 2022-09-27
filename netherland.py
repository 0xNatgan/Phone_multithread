import random

def netherland():
    mid = '+316'
    prefixe = ['0','1','2','3','4','5','6','8','9']
    mid += prefixe[random.randint(0,8)]
    for n in range (7):
        mid += str(random.randint(0,9))
    print(mid,"\n")
    return mid
