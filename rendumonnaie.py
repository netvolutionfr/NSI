# algorithme de rendu de monnaie (glouton)


def rendu(montant):
    facteur = 1000
    montant_int = int(montant * facteur)
    pieces = [0.01, 0.02, 0.05, 0.1, 0.2, 0.5, 1, 2, 5, 10, 20, 50, 100]
    liste_rendu = []
    total = 0
    indice = len(pieces)-1
    while total < montant_int and indice >= 0:
        if int(pieces[indice]*facteur) <= (montant_int-total):
            liste_rendu.append(pieces[indice])
            total = total + int(pieces[indice]*facteur)
        else:
            indice = indice - 1
    return liste_rendu


print(rendu(3.75))
