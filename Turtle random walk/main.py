import turtle as t
import random

tim = t.Turtle()
tim.shape('turtle')
tim.pensize(15)
tim.speed('fastest')
t.colormode(255)

directions = (0, 90, 180, 270)


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r, g, b)


# basically tim the turtle hunts for food simulation
for _ in range(200):
    tim.color(random_color())
    tim.forward(30)
    tim.setheading(random.choice(directions))
