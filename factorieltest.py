# fact1 : On commence par 0 et on teste si i <= n donc on fait n+1 boucles : on obtient donc (n+1)!
# trouver un contre exemple
def fact1(n):
    i = 0
    F = 1
    while i <= n:
        i += 1
        F *= i
    return F


"""
fact2 : démonstration de la correction partielle
invariant : P(F,i) = "F = i!" et i<=n
1. Initialisation : 
i = 0, F = 1, donc P(1,0) est vraie
De plus, comme n est un entier positif, i et bien inférieur ou égal à n.

2. Hérédité :
Notons F et i les valeurs à l'entrée de la boucle.
Notons F' et i' les valeurs en sortie de boucle.
Supposons que P(F,i) est vraie et montrons que P(F',i') est aussi vraie.
    Après la première ligne, i' = i+1
    A la deuxième ligne, F' = F * i' = F * (i+1)
    Or F = i!, donc F' = i! * (i+1) = (i+1)!
    Donc F' = i'!
    On a donc démontré que si P(F,i) est vraie, alors P(F', i') est aussi vraie
Deuxième partie de l'invariant : en entrée de boucle, on sait que i < n. L'invariant est vrai au début.
    En sortie de boucle, i' est aussi 

3. Conclusion :
En sortie de boucle, on sait que l'invariant (première partie) est satisfait (F = i!).
La condition de continuation de la boucle est fausse (i >= n) donc i vaut exactement n, donc l'invariant
(deuxième partie i<=n) est encore vrai.
"""


def fact2(n):
    i = 0
    F = 1
    while i < n:
        i += 1
        F *= i
    return F


def fact3(n):
    i = 1
    F = 1
    while i <= n:
        F *= i
        i += 1
    return F

# fact4 : On commence à zéro et on multiplie par zéro : on obtient toujours zéro.
def fact4(n):
    i = 0
    F = 1
    while i < n:
        F *= i
        i += 1
    return F


