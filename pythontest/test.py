import turtle as t
import time
t.hid()
# 设置窗口大小和标题
t.setup(width=600, height=600)
t.title("自由落地运动")

# 设置小球初始位置和速度
posx = 0
posy = 250
speed_y = 0

# 绘制边界
def draw_boundary():
    t.pensize(3)
    t.penup()
    t.goto(-250, -250)
    t.pendown()
    for _ in range(4):
        t.forward(500)
        t.left(90)

# 绘制小球
def draw_ball(x, y):
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.begin_fill()
    t.circle(20)
    t.end_fill()

# 自由落地运动
while True:
    t.clear()
    t.tracer(False)
    draw_boundary()
    draw_ball(posx, posy)

    # 自由落体运动
    speed_y -= 1  # 重力加速度
    posy += speed_y

    # 触底反弹
    if posy <= -230:
        posy = -230
        speed_y *= -0.9  # 反弹时速度减小并改变方向

    t.update()
    time.sleep(0.01)



t.done()
