import turtle


wn = turtle.Screen()
alex = turtle.Turtle()


def koch(tortue, n, l):
    if n == 0:
        tortue.forward(l)
    else:
        koch(tortue, n - 1, l / 3)
        tortue.left(60)
        koch(tortue, n - 1, l / 3)
        tortue.right(120)
        koch(tortue, n - 1, l / 3)
        tortue.left(60)
        koch(tortue, n - 1, l / 3)


alex.color('blue', 'green')
alex.begin_fill()
alex.speed(0)
alex.penup()
alex.backward(250)
alex.pendown()

for i in range(3):
    koch(alex, 5, 500)
    alex.right(120)

alex.end_fill()

turtle.done()

