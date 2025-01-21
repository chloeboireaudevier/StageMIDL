"""
Objectif :

- comprendre la nécessité dans cet exercice de parcourir un tableau suivant les indices
- savoir construire un tableau en partant d'un tableau vide et en utilisant append

Au moment de réaliser cet exercice, la plupart n'ont jamais entendu parler de
construction en compréhension et même parmi les élèves qui l'auraient vu en
classe de Terminale, aucun à mon avis ne se souvenais réellement et surtout
avec le filtre if ; donc clairement la solution 1 est la seule que j'attendais
ma solution 2 n'a probablement été proposée par aucun binome.

Concernant un bareme possible d'un tel exercice sur la partie tableau explicitement
(construction, accès et modification) sur 3 pts par exemple je mettrai :

- 1 pt pour la construction (0.5 pour l'initialisation avec [] et 0.5 pour le append)
- 1 pt si la boucle est présente (sur les indices)
- 1 pt pour les accès dans le if 
"""

# Solution 1

def coincide(tab_1, tab_2):
    positions = []
    for i in range(len(tab_1)):
        if tab_1[i] == tab_2[i]:
            positions.append(i)
    return positions

# Solution 2

def coincide_2(tab_1, tab_2):
    return [i for i in range(len(tab_1)) if tab_1[i] == tab_2[i]]
