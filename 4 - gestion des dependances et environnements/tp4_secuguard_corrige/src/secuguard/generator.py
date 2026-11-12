from string import ascii_letters, digits, punctuation
import random

def generer_mot_de_passe ( longueur : int = 12, avec_chiffres : bool = True ,
avec_symboles : bool = True ) -> str:
    A = set()
    A = A | set(ascii_letters)

    if avec_chiffres:
        A = A | set(digits)

    if avec_symboles:
        A = A | set(punctuation)

    mot_de_passe = ""

    for i in range(longueur):
        mot_de_passe = mot_de_passe + random.choice(tuple(A))

    return mot_de_passe

    