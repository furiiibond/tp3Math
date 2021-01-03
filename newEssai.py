
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



print(wordToNumber("AAA"))
