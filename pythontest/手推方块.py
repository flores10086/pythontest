import turtle as t
import time
bt = 30 * (2 ** 0.5)

def hand(locx, locy):
    loc = (locx, locy)
    t.pu()
    t.goto(loc)
    t.pd()
    t.setheading(0)
    t.left(180)
    t.forward(150)
    t.circle(25, 180)
    t.forward(150)
    t.left(180)
    t.circle(20, 180)
    t.forward(50)
    t.backward(50)
    t.left(180)
    t.circle(20, 180)
    t.forward(50)
    t.backward(50)
    t.left(180)
    t.circle(15, 180)
    t.forward(50)
    t.pu()
    t.left(90)
    t.forward(5)
    t.right(90)
    t.pd()
    t.circle(15, 180)
    t.left(180)
    t.circle(18, 180)
    t.left(180)
    t.circle(20, 180)
    t.pu()
    t.right(90)
    t.forward(60)
    t.pd()
    t.backward(40)
    t.left(180)
    t.circle(28, 180)
    t.forward(40)
    t.pu()
    t.backward(20)
    t.right(90)
    t.pd()
    t.forward(200)
    t.pu()
    t.backward(200)
    t.right(90)
    t.forward(125)
    t.left(90)
    t.pd()
    t.forward(300)

def desk():
    t.setheading(0)
    t.pu()
    t.goto(dloc)
    t.pd()
    t.circle(5)
    t.right(120)
    t.forward(300)
    t.left(120)
    t.forward(500)
    t.pu()
    t.goto(sloc)
    t.pd()

def square(loc, arf):
    t.pu()
    t.goto(loc)
    t.pd()
    t.setheading(0)
    t.left(arf)
    t.forward(100)
    t.left(45)
    t.forward(bt)
    t.left(45)
    t.forward(100)
    t.left(90)
    t.forward(100)
    t.left(45)
    t.forward(bt)
    t.left(45)
    t.forward(100)
    t.pu()
    t.backward(100)
    t.left(90)
    t.pd()
    t.forward(100)
    t.left(45)
    t.forward(bt)
    t.backward(bt)
    t.right(135)
    t.forward(100)

t.speed(0)
locx = t.xcor()
locy = t.ycor()
sloc = (locx, locy)
i = 0
j = 50
run = 0
angle = 0
h_movement = 0
t.hideturtle()
dloc = (-100, 100)

while run < 320:
    t.clear()
    t.tracer(False)
    hand(600 - run, 100)
    desk()
    square(sloc, angle)
    time.sleep(0.005)
    t.update()
    run += 1

while True:
    t.clear()
    if i < 250:

        sloc = (locx - i, locy)  # 方块坐标
    if i > 250:
        if angle < 90:
            angle += 5
        if j > 500:
            j = 500
        # sloc = (locx - 250, locy - j*1.5)#改之前
        sloc = (locx - 250-j*0.8, locy - j*1.5)#改之后
        j += 10
    t.tracer(False)
    if run > 600:
        run = 600
    hand(600 - run, 100)
    desk()
    if i > 190 and i < 200:
        square(sloc, angle)
    else:
        square(sloc, angle)
    if i > 190 and i < 200:
        time.sleep(0.01)
    else:
        time.sleep(0.01)
    i += 1
    run += 1
    t.update()

t.done()
