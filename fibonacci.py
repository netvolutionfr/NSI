import sys


def fibs():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b


fibs = fibs()
fibonacci = list(next(fibs) for _ in range(20))


print(fibonacci)
print(sys.getrecursionlimit())

