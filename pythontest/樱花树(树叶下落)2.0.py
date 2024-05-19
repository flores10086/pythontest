import turtle as t
import random

# 常量定义
INITIAL_DEPTH = 10  # 初始树的深度
INITIAL_LENGTH = 75  # 初始树枝的长度
BRANCH_ANGLE_MIN = 15  # 树枝分叉的最小角度
BRANCH_ANGLE_MAX = 20  # 树枝分叉的最大角度
LENGTH_DECREASE_MIN = 5  # 每层树枝长度减少的最小值
LENGTH_DECREASE_MAX = 10  # 每层树枝长度减少的最大值
DECORATION_RADIUS_MIN = 3  # 装饰点的最小半径
DECORATION_RADIUS_MAX = 5  # 装饰点的最大半径
DECORATION_COUNT = 15  # 每层树枝上的装饰点数量
DECORATION_COLOR_R_MIN = 250  # 装饰点红色分量的最小值
DECORATION_COLOR_R_MAX = 255  # 装饰点红色分量的最大值
DECORATION_COLOR_G_MIN = 185  # 装饰点绿色分量的最小值
DECORATION_COLOR_G_MAX = 195  # 装饰点绿色分量的最大值
DECORATION_COLOR_B_MIN = 195  # 装饰点蓝色分量的最小值
DECORATION_COLOR_B_MAX = 210  # 装饰点蓝色分量的最大值
LEAF_FALL_SPEED = 10  # 叶子下落的速度

# 全局变量定义
leaves = []  # 记录所有叶子的位置和颜色

def draw_branch(deep, length):
    """递归绘制树枝"""
    if deep < 1:
        return

    t.pd()  # 放下画笔开始绘制
    t.pensize(deep)  # 设置画笔的粗细
    t.forward(length)  # 前进指定的长度

    if deep > 0:
        rd = random.randint(BRANCH_ANGLE_MIN, BRANCH_ANGLE_MAX)  # 随机生成右转角度
        ld = random.randint(BRANCH_ANGLE_MIN, BRANCH_ANGLE_MAX)  # 随机生成左转角度
        length_decrease = random.randint(LENGTH_DECREASE_MIN, LENGTH_DECREASE_MAX)  # 随机生成减少的长度

        t.right(rd)  # 右转指定角度
        draw_branch(deep - 1, length - length_decrease)  # 递归调用生成右侧树枝
        t.left(ld + rd)  # 左转回到主干方向再左转
        draw_branch(deep - 1, length - length_decrease)  # 递归调用生成左侧树枝
        t.right(ld)  # 右转回到主干方向

    # 当树的深度小于6时，添加一些装饰点
    if deep < 6:
        add_decorations()

    t.backward(length)  # 返回到初始位置

    # 每次绘制粗树枝时更新画布
    if deep >= 6:
        t.update()

def add_decorations():
    """在树枝上添加装饰点"""
    pos = t.pos()  # 记录当前位置
    red = random.randint(DECORATION_COLOR_R_MIN, DECORATION_COLOR_R_MAX)
    green = random.randint(DECORATION_COLOR_G_MIN, DECORATION_COLOR_G_MAX)
    blue = random.randint(DECORATION_COLOR_B_MIN, DECORATION_COLOR_B_MAX)

    for _ in range(DECORATION_COUNT):
        locx = random.randint(-25, 25)
        locy = random.randint(-25, 25)
        leaf_position = (t.xcor() + locx, t.ycor() + locy)
        t.color(red, green, blue)  # 设置装饰点颜色
        t.pu()  # 抬起画笔移动到新位置
        t.goto(leaf_position)  # 移动到随机位置
        t.pd()  # 放下画笔开始绘制
        if random.randint(0, 100) % 2 == 0:  # 随机选择填充圆或空心圆
            t.begin_fill()
            t.circle(random.randint(DECORATION_RADIUS_MIN, DECORATION_RADIUS_MAX))
            t.end_fill()
        else:
            t.circle(5)
        leaves.append((leaf_position, (red, green, blue)))  # 记录叶子的位置和颜色

    t.color('black')  # 恢复画笔颜色为黑色
    t.pu()  # 抬起画笔
    t.setpos(pos)  # 返回到原位置
    t.pd()  # 放下画笔

def setup_turtle():
    """初始化海龟画布和画笔"""
    t.hideturtle()  # 隐藏海龟形状
    t.colormode(255)  # 设置颜色模式为RGB
    t.bgcolor(240, 230, 230)  # 设置背景颜色
    t.ht()  # 隐藏海龟
    t.speed(0)  # 设置绘制速度为最快
    t.tracer(0, 0)  # 关闭自动更新画布，手动更新
    t.pensize(16)  # 设置初始画笔粗细
    t.pu()  # 抬起画笔
    t.right(90)  # 右转90度
    t.forward(500)  # 前进500个单位
    t.pd()  # 放下画笔
    t.left(180)  # 左转180度
    t.pd()  # 放下画笔
    t.forward(200)  # 前进200个单位

def fall_leaves():
    """模拟叶子下落的过程"""
    global leaves
    new_leaves = []
    for pos, color in leaves:
        t.color(color)  # 设置叶子的颜色
        t.pu()
        t.goto(pos)
        t.pd()
        if random.randint(0, 100) % 2 == 0:  # 随机选择填充圆或空心圆
            t.begin_fill()
            t.circle(random.randint(DECORATION_RADIUS_MIN, DECORATION_RADIUS_MAX))
            t.end_fill()
        else:
            t.circle(5)

        # 模拟叶子下落
        new_pos = (pos[0], pos[1] - LEAF_FALL_SPEED)
        if new_pos[1] > -250:  # 只有叶子还在画布内才保留
            new_leaves.append((new_pos, color))

    leaves = new_leaves  # 更新叶子列表

    t.update()  # 更新画布显示

    if len(leaves) > 0:
        t.ontimer(fall_leaves, 100)  # 设置定时器，每100毫秒调用一次 fall_leaves

def main():
    """主函数"""
    setup_turtle()  # 初始化画布和画笔
    draw_branch(INITIAL_DEPTH, INITIAL_LENGTH)  # 绘制树枝
    t.update()  # 更新画布显示
    t.ontimer(fall_leaves, 1000)  # 1秒后开始叶子下落动画
    t.done()  # 完成绘制

if __name__ == "__main__":
    main()

