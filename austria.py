import random

def austria():
    mid = '+9715'
    prefixe = ['60','99','64','76','50','80','81','65','88','77','70','90']
    mid += prefixe[random.randint(0,(len(prefixe)-1))]
    for n in range (7):
        mid += str(random.randint(0,9))
    print(mid,"\n")
    return mid
