CANVAS_SIZE = 500
DENSITY = 15
from time import sleep
import turtle
import random

t = turtle.Turtle()
t.speed(0)
t.pensize(2)
s = turtle.Screen()
s.colormode(255)
s.bgcolor("black")
s.setup(CANVAS_SIZE, CANVAS_SIZE)
t.penup()

def draw_line(row, col):
    t.pencolor(random.randint(0, 255),random.randint(0, 255),random.randint(0, 255))
    lower_left = (
        (col * CANVAS_SIZE / DENSITY) - CANVAS_SIZE / 2,
        (row * CANVAS_SIZE / DENSITY) - CANVAS_SIZE / 2
    )
    upper_right = (
        ((col + 1) * CANVAS_SIZE / DENSITY) - CANVAS_SIZE / 2,
        ((row + 1) * CANVAS_SIZE / DENSITY) - CANVAS_SIZE / 2
    )
    lower_right = (
        ((col + 1) * CANVAS_SIZE / DENSITY) - CANVAS_SIZE / 2,
        (row * CANVAS_SIZE / DENSITY) - CANVAS_SIZE / 2
    )
    upper_left = (
        (col * CANVAS_SIZE / DENSITY) - CANVAS_SIZE / 2,
        ((row + 1) * CANVAS_SIZE / DENSITY) - CANVAS_SIZE / 2
    )
    res = random.randint(0, 1) 
    if res == 0:
        t.goto(upper_left)
        t.pendown()
        t.goto(lower_right)
        t.penup()
    else:
        t.goto(lower_left)
        t.pendown()
        t.goto(upper_right)
        t.penup()


for row in range(DENSITY):
    for col in range(DENSITY):
        draw_line(row, col)    

sleep(10)