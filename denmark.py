import random

def denmark():
    mid = '+45'
    prefixe = ['30','31','40','41', '42', '50', '51', '52', '53', '60', '61', '71', '81','20']
    mid += prefixe[random.randint(0,(len(prefixe)-1))]
    for n in range (6):
        mid += str(random.randint(0,9))
    print(mid,"\n")
    return mid
