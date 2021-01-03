import math
from math import *
from random import *
import time


def wordToNumber(chaine):
    res = 0
    tailleChaine = len(chaine)
    if (tailleChaine == 1):
        return wordToNumberLen1(chaine)
    else:
        i = 0
        for lettre in chaine:
            if (i == tailleChaine - 1):
                res += wordToNumberLen1(lettre)
            else:
                res += (wordToNumberLen1(lettre) + 1) * (26 ** (((tailleChaine - 1) - i)))
            i = i + 1
    return res


def wordToNumberLen1(caractere):
    return ord(caractere) - 65


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


def zTab(nb):
    chaine = ""
    for i in range(0, nb):
        chaine += "Z"
        print(wordToNumber(chaine))


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
    q = n
    while (testPrime(q) == False):
        q += 1
    return q


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


def aleaE(p, q):
    # test s'ils sont premier et renvoie un nombre aléatoire compris dans {2, 3, … , (p*q) − 1} et qui est premier avec (𝑝 − 1)(𝑞 − 1).
    if (testPrime(p) == False):
        return False
    if (testPrime(q) == False):
        return False
    n = p * q
    e = randrange(2, n, 1)
    while (premiers_entre_eux(e, (p - 1) * (q - 1)) == False):
        e = randrange(2, n, 1)  #randrange(min, max, pas)

    return e


def puiModIte(x, e, n):
    A = x
    b = 1
    while (e != 0):
        if ((e % 2) != 0):
            b = (A * b) % n
        e = e // 2
        A = (A * A) % n
    return b


def puiModRec(x, e, n):
    #e fonction calculant 𝑥𝑒(modulo n)

    if (e == 0):
        return 1
    if (e == 1):
        return x
    if (e % 2 == 0):
        b = puiModRec(x, e / 2, n)
        return (b * b) % n
    else:
        b = puiModRec(x, (e - 1) / 2, n)
        return (b * b * x) % n


def mod_inverse(x, m):
    for n in range(m):
        if (x * n) % m == 1:
            return n
            break
        elif n == m - 1:
            return "Null"
        else:
            continue


# print(aleaE(nextPrime(55),nextPrime(15)))


# tps1=time.perf_counter()
# print((4**3)%20)
# print (time.perf_counter()-tps1)
# tps2 =time.perf_counter()
# print(puiModIte(4,3,20))
# print(time.perf_counter()-tps2)
# tps3 =time.perf_counter()
# print(puiModRec(4,3,20))
# print (time.perf_counter()-tps3)
# (x+1)Ã—26+y
# (x+1)Ã—26^(2)+(y+1)Ã—26+z


# Partie 3

def chiffreRSA(n, e, liste):
    listeRes = list()
    for mot in liste:
        M = wordToNumber(mot)
        listeRes.append(numberToWord(puiModRec(M, e, n)))

    return listeRes


MESSAGE=["LE", "CHAT", "DORT"]
print(MESSAGE)
n=(nextPrime(555)*nextPrime(155)) #n produit de deux nombres premieres
e=aleaE(nextPrime(555),nextPrime(155))
MessageCode=chiffreRSA(n, e, MESSAGE)
print(MessageCode)
d=mod_inverse(e, ((nextPrime(555)-1)*(nextPrime(155)-1)))
print(chiffreRSA(n, d, MessageCode))


def fact(n):
    p = nextPrime(0)
    q = nextPrime(0)
    while (p < n):
        while (q < n):
            if (p * q == n):
                break
            q = nextPrime(p)
        p = nextPrime(p)
    if (p * q == n):
        return (p, q)
    else:
        return "erreur"


# print(fact(n))
print(mod_inverse(5, 6))
