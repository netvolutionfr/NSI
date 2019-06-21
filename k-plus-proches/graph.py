import pandas
import matplotlib.pyplot as plt
from sklearn.neighbors import KNeighborsClassifier


# traitement CSV
iris = pandas.read_csv("./iris.csv")
x = iris.loc[:, "petal_length"]
y = iris.loc[:, "petal_width"]
lab = iris.loc[:, "species"]
# fin traitement CSV

# valeurs
fleurtrouvee = {
    'longueur': 2.5,
    'largeur': 0.75
}
k = 5


longueur = fleurtrouvee['longueur']
largeur = fleurtrouvee['largeur']

# fin valeurs


# graphique
plt.scatter(x[lab == 0], y[lab == 0], color='g', label='setosa')
plt.scatter(x[lab == 1], y[lab == 1], color='r', label='virginica')
plt.scatter(x[lab == 2], y[lab == 2], color='b', label='versicolor')
plt.scatter(longueur, largeur, color='k')
plt.legend()
# fin graphique


# algo knn
d = list(zip(x, y))
model = KNeighborsClassifier(n_neighbors=k)
model.fit(d, lab)
prediction = model.predict([[longueur, largeur]])
# fin algo knn


# Affichage résultats
resultat = "Résultat : "
if prediction[0] == 0:
    resultat = resultat + "Setosa"
if prediction[0] == 1:
    resultat = resultat + "Virginica"
if prediction[0] == 2:
    resultat = resultat + "Versicolor"

plt.text(3, 0.5, f"Largeur : {largeur} cm Longueur : {longueur} cm", fontsize=12)
plt.text(3, 0.3, f"k : {k}", fontsize=12)
plt.text(3, 0.1, resultat, fontsize=12)
# fin affichage résultats


plt.show()

