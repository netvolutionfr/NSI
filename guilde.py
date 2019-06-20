# https://callicode.fr/pydefis/Algorithme/txt

# initialiser a, b, c, k et n respectivement à 1, 2, 5, 1 et 0
a, b, c, k, n = 1, 2, 5, 1, 0

while k < 1000-n:
    a = b
    b = c + a
    c = 3*c + 4*a - b
    n = a + b
    k = k + 1

print (a, b, c)

# répéter tant que k est strictement inférieur à 1000-n
#     a ← b
#     b ← c + a
#     c ← 3*c + 4*a - b
#     n ← a + b
#     augmenter k de 1
# fin répéter