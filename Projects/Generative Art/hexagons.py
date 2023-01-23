# make a geometric pattern
from time import sleep
import turtle
import random
pen = turtle.Turtle()
pen.speed(0)
pen.pensize(2)
s = turtle.Screen()
s.colormode(255)
s.bgcolor('black')
for n in range(36):
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    pen.pencolor(r,g,b)
    # repeat 6 times - move forward and turn
    for i in range(6) :
        pen.forward(100)
        pen.left(60)
    pen.right(10) # add a turn

sleep(10)