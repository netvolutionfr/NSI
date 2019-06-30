import turtle


wn = turtle.Screen()
tac = turtle.Turtle()

tac.color('blue', 'pink')

tac.begin_fill()

for i in range(4):
    tac.forward(100)
    tac.right(90)

tac.end_fill()

tac.left(120)
tac.forward(100)
tac.left(60)
tac.forward(100)
tac.left(60)
tac.forward(100)


turtle.done()
