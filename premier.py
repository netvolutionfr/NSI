import math


def estpremier(n):
    """estpremier(n): dit si un nombre est premier (renvoie True ou False)"""
    if n<7:
        if n in (2,3,5):
            return True
        else:
            return False
    # si n est pair et >2 (=2: cas traité ci-dessus), il ne peut pas être premier
    if n & 1 == 0:
        return False
    # autres cas
    k=3
    r=math.sqrt(n)
    while k<=r:
        if n % k == 0:
            return False
        k+=2
    return True

k = 1000001
trouve = False
while trouve == False:
    trouve = estpremier(k)
    k = k+2

print (k)