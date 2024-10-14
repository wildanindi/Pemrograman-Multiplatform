import turtle
nbrSides = 6
for steps in range (nbrSides):
    turtle.color('green')
    turtle.forward(100)
    turtle.right(360/nbrSides)
    for moresteps in range(nbrSides):
        turtle.color('blue')
        turtle.forward(50)
        turtle.right(360/nbrSides)
        turtle.color('pink')
        turtle.forward(100)