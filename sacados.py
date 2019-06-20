liste = [
    ['Téléphone', 400, 600, 6],
    ['Ordinateur', 1500, 1500, 3],
    ['Tablette', 1000, 800, 4],
    ['Montre connectée', 250, 200, 10]
]

def sac(poids):
    poids_grammes = poids * 1000
    total = 0
    sac = [
        ['Téléphone', 0],
        ['Ordinateur', 0],
        ['Tablette', 0],
        ['Montre connectée', 0]
    ]
    indice = 0
    montant = 0
    while total < poids_grammes and indice < 4:
        element = liste[indice]
        if int(element[3]) > 0 and poids_grammes - total >= int(element[1]):
            sac[indice][1] = int(sac[indice][1] + 1)
            element[3] = element[3] - 1
            total = total + int(element[1])
            montant = montant + int(element[2])
        else:
            indice = indice + 1
    print(montant)
    print(total/1000)
    return sac


print(sac(13))
