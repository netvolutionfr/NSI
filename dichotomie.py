import random
import statistics


maximum = 50000
liste = []


def cherchevitrine():
    vitrine = random.randint(1, 50000)
    prix = int(maximum / 2)
    i = 1

    while prix != vitrine:
        if prix > vitrine:
            prix = prix - int(maximum / (2**i)) - 1
        else:
            prix = prix + int(maximum / (2**i)) + 1
        i = i + 1

    return i


for i in range(0, 100):
    liste.append(cherchevitrine())

print(statistics.mean(liste))


