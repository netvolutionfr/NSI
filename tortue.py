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


alex.speed(0)
alex.penup()
alex.backward(250)
alex.pendown()
koch(alex, 4, 500)

turtle.done()

