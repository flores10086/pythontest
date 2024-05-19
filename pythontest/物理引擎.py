import turtle as t
import time as ti
# define G 9.8
# 重力加速度
t.speed(0)
t.hideturtle()

#######################################################################################################################################
posx = 50 #小球初始x坐标
posy = -100 #小球初始y坐标
xSpeed = 0#水平初速度
ySpeed = -50#竖直初速度
consume = 0.8#动能损耗
leftBorder = -100 #左边距 (相距与中点)
rightBorder = 100 #右边距
topBorder = 100 #上边距
bottomBorder = -100 #下边距
#######################################################################################################################################
count = 0#碰壁次数

#输入
# print("请输入小球初始坐标")
# posx = int(input())# 输入小球起始点x
# posy = int(input())# 输入小球起始点y
# print("请输入小球水平初速度(向右代表正方向)")
# xSpeed= int(input())
# print("请输入小球竖直初速度(向上代表正方向)")
# ySpeed= int(input())

# 外边框1000*1000(原点0,0)
def map():
    t.pu()
    t.goto(0,0)
    t.pd()
    #t.circle(1)
    t.pu()
    t.goto(rightBorder,0)#右边中点
    t.setheading(0)#方向向右
    t.pd()
    t.left(90)#方向向上
    t.forward(topBorder)
    t.left(90)#方向向左
    t.forward(2 * rightBorder)
    t.left(90)
    t.forward(2 * topBorder)
    t.left(90)
    t.forward(2 * rightBorder)
    t.left(90)
    t.forward(topBorder)

def ball(x,y):
    t.pu()
    t.goto(x,y)
    t.pd()
    t.begin_fill()
    t.circle(10)
    t.end_fill()

while(True):
    t.clear()
    t.tracer(False)
    map()#地图边框
    ball(posx,posy)#球
    posx -= xSpeed
    posy -= ySpeed
    ySpeed += 1#重力加速度

    if count > 10:
        consume = 0.6
        if count > 15:
            consume = 0.3
    if posy <= bottomBorder:#触底
        posy = bottomBorder
        ySpeed *= consume * -1  # 反弹时速度减小并改变方向
        xSpeed *=consume
        count+=1
    if posy >= topBorder:#触顶
        posy = topBorder
        ySpeed *= consume * -1  # 反弹时速度减小并改变方向
        count+=1
    if posx <= leftBorder:#左碰壁
        posx = leftBorder
        xSpeed *= consume * -1  # 反弹时速度减小并改变方向
        count += 1
    if posx >= rightBorder:#右碰壁
        posx = rightBorder
        xSpeed *= consume * -1  # 反弹时速度减小并改变方向
        count += 1
    t.update()
    ti.sleep(0.02)

t.done()