import turtle as t
import random
t.colormode(255)

for i in range(20):
    red=random.randint(0,255)
    green=random.randint(0,255)
    blue=random.randint(0,255)

    x=random.randint(-220,220)
    y=random.randint(-100,220)

    t.penup()
    t.goto(x,y)
    t.pendown()


    t.color(red,green,blue)

    t.begin_fill()
    t.circle(30)
    t.end_fill()
    t.right(90)
    t.forward(30)
    t.left(90)


input()















