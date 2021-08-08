#!/usr/bin/env python3
import math
import random
import string
import time

mot_de_passe = input("Quel est le mot de passe à trouvé ? ") # le mot de passe à trouver

def mot_aleatoire():
    # lettres = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','w','y','z']
    lettres = string.ascii_letters
    suivant = ""
    resultat = ""
    for i in range (0, len(mot_de_passe)):
        while mot_de_passe[i] != suivant:
            print(resultat + suivant+"\n")
            suivant = random.choice(lettres)
        resultat += suivant
    return resultat

debut = time.time()

print(mot_aleatoire())
print(" Durée : " + str(time.time() - debut) + " secondes")

<<<<<<< HEAD
Retest
=======
test
>>>>>>> a092ad0 (trainnning python security2)
