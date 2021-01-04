import time
from math import sqrt
from random import randrange


def letterToNumber(lettre):
    return ord(lettre)-65

def wordToNumber(chaine):
    res = 0
    tailleChaine = len(chaine)
    if (tailleChaine == 1):
        return letterToNumber(chaine)
    else:
        i = 0
        for lettre in chaine:
            if (i == tailleChaine - 1):
                res += letterToNumber(lettre)
            else:
                res += (letterToNumber(lettre) + 1) * (26 ** (((tailleChaine - 1) - i)))
            i = i + 1
    return res


def numberToWordLen1(num):
    return chr(num + 65)


def numberToWord(n):
    res = ""
    while (n >= 0):
        b = n % 26
        res = numberToWordLen1(b) + res
        n = n // 26
        n = n - 1
    return res

def ZK(nommdreDeZ):
    res=""
    for i in range(nommdreDeZ):
        res+="Z"
    return wordToNumber(res)

def testPrime(n):
    if n < 7:
        if n in (2, 3, 5):
            return True
        else:
            return False
    # si n est pair et >2 (=2: cas traitÃ© ci-dessus), il ne peut pas Ãªtre premier
    if n & 1 == 0:
        return False
    # autres cas
    k = 3
    r = sqrt(n)
    while k <= r:
        if n % k == 0:
            return False
        k += 2
    return True

def nextPrime(n):
    while (not testPrime(n)):
        n=n+1
    return n

def createN():
    return nextPrime(randrange(5000, 9000, 1)) * nextPrime(randrange(1000, 4000, 1))


def premiers_entre_eux(a, b):
    if (pgcd(a, b) == 1):
        return True
    return False


def pgcd(a, b):
    """pgcd(a,b): calcul du 'Plus Grand Commun Diviseur' entre les 2 nombres entiers a et b"""
    if b == 0:
        return a
    else:
        r = a % b
        return pgcd(b, r)

def  aleaE(p,q):
    if (testPrime(p) == False):
        return False
    if (testPrime(q) == False):
        return False

    res=randrange(2, p*q-1, 1)
    while(not premiers_entre_eux(res,(p-1)(q-1))):
        res=randrange(2, p * q - 1, 1)
    return res
t1=time.time()
def puiMod(x,e,n):
    A=x
    b=1
    while(e!=0):
        if (e%2==0):
            b=A*b%n
        e=e//2
        A=A*A%n
    return b


print (puiMod(3556567890,23435675,204567345673456756))
print(time.time()-t1)

print(ZK(2))
print(nextPrime(90))


def  chiffreRSA(n,e,liste):

