import random

def germany():
    mid = '+491'
    prefixe = ['51','52','55','59','60','62','63','70','71','72','73','74','75','76','77','78','79']
    mid += prefixe[random.randint(0,(len(prefixe) - 1))]
    for n in range (8):
        mid += str(random.randint(0,9))
    print(mid,"\n")
    return mid
