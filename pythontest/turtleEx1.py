import turtle as t

'''turtle.circle(半径)'''
t.speed(10)
t.color('red')
t.pensize(10)

t.write('北京 2008',font=('kaiti',32))
for i in range(4):
    t.circle(95)
    t.left(92)
t.penup()
t.goto(-200,0)
t.pendown()
t.circle(95)
# t.circle(100)
# t.left(90)
# t.circle(100)
# t.left(90)
# t.circle(100)
# t.left(90)
# t.circle(100)
# t.left(90)

