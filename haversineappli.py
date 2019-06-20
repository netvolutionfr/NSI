from haversine import haversine

lyon = (45.7597, 4.8422) # (lat, lon)
paris = (48.8567, 2.3508)

maison = (50.6445554, 3.0889392)
travail = (50.7369373, 1.6202156)

print(haversine(lyon, paris))
print(haversine(maison, travail))

