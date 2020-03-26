# -*- coding: utf-8 -*-
"""
Éditeur de Spyder
Haroun 
Ceci est un script temporaire.
"""

p = input("entrez votre prénom : ")
print("Bienvenue sur le jeu Bubble sort !")


def bubbleSort(li):
    n = len(li)
 
    # Parcourez tous les éléments du tableau
    for i in range(n):
 
        #Les i derniers éléments sont déjà en place
        for j in range(0, n-i-1):
 
            # On parcourt le tableau de 0 à n-i-1
            # On échange si l'élément trouvé est supérieur
            # à l'élément suivant
            if li[j] > li[j+1] :
                li[j], li[j+1] = li[j+1], li[j]
 
#test
li = [64, 34, 25, 12, 22, 11, 90]
 
bubbleSort(li)

print ("Le tableau obtenus est:")
for i in range(len(li)):
    print ("%d" %li[i]),


