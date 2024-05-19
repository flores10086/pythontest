import turtle as t
import random

def tree(deep,long):
    if deep<1:
        return
    t.pd()
    t.pensize(deep)
    t.forward(long)
    rd=random.randint(15,20)
    ld=random.randint(15,20)
    long1=random.randint(5,10)
    if deep>0:
        t.right(rd)
        tree(deep-1,long-long1)
        t.left(ld+rd)
        tree(deep-1,long-long1)
        t.right(ld)
    if deep<6:
        pos=t.pos()
        # times=random.randint(10, 15)


        red = random.randint(250, 255)
        green = random.randint(185, 195)
        blue = random.randint(195, 210)
        for i in range(15):
            locx = random.randint(-25, 25)
            locy = random.randint(-25, 25)
            t.color(red,green,blue)
            t.pu()
            t.goto(t.xcor()+locx,t.ycor()+locy)
            t.pd()
            rd=random.randint(0,100)
            r=random.randint(3,5)
            if rd%2==0:
                t.begin_fill()
                t.circle(r)
                t.end_fill()
            else:
                t.circle(5)
        t.color('black')
        t.pu()
        t.setpos(pos)
        t.pd()
    t.backward(long)


t.hideturtle()
t.colormode(255)
t.bgcolor(240, 230, 230)
t.ht()
t.speed(0)
t.tracer(0,0)
t.pensize(16)
t.pu()
t.right(90)
t.forward(500)
t.pd()
t.left(180)
t.pd()
t.forward(200)
tree(10,75)



t.done()
