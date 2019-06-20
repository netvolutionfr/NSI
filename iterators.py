import itertools

des = [1, 2, 3, 4, 5, 6]
lancers = itertools.combinations_with_replacement(des, 2)

print(list(lancers))

