import turtle as t
import math
t.colormode(255)

def line(*args):
    if not args:  # 如果没有传入参数
        return Error()
    if isinstance(args[0], str):  # 如果第一个参数是字符串
        return E_line(args[0])  # 调用直线表达式函数
    elif isinstance(args[0], tuple) and isinstance(args[1], tuple) and len(args) == 2:  # 判断是否传入两个元组作为参数
        return P_P_line(args[0], args[1])#两点法-线段
    elif isinstance(args[0], tuple) and len(args) == 3:  # 判断是否传入一个元组和两个数字作为参数
        return P_L_D_line(args[0], args[1], args[2])#一点一长一斜率-线段
    elif isinstance(args[0], tuple) and len(args) == 2 and isinstance(args[1], float):  # 判断是否传入一个元组和一个浮点数作为参数
        return P_D_line(args[0], args[1])#一点一斜率-直线
    return Error()  # 若无法匹配任何情况，则调用 Error 函数报错

def P_P_line(loc_a, loc_b):
    try:
        t.color(120, 190, 140)
        pos = t.pos()
        t.pu()
        t.goto(loc_a)
        t.pd()
        t.goto(loc_b)
        t.pu()
        t.goto(pos)
        t.setheading(0)
        t.color(0, 0, 0)
        print("P_P_line 成功")
        return True
    except Exception as e:
        print("P_P_line 失败:", e)
        return False

def P_L_D_line(loc_a, length, slope):
    try:
        t.color(120, 130, 190)
        pos = t.pos()
        T=math.tan(slope)
        t.pu()
        t.goto(loc_a)
        t.pd()
        t.setheading(0)
        t.left(T)
        t.forward(length/2)
        t.backward(length)
        t.pu()
        t.goto(pos)
        t.setheading(0)
        t.color(0, 0, 0)
        print("P_L_D_line 成功")
        return True
    except Exception as e:
        print("P_L_D_line 失败:", e)
        return False

def P_D_line(loc_a, slope):
    try:
        t.color(180, 130, 140)
        pos = t.pos()
        T = math.tan(slope)
        t.pu()
        t.goto(loc_a)
        t.pd()
        t.setheading(0)
        t.left(T)
        t.forward(10000)
        t.backward(20000)
        t.pu()
        t.goto(pos)
        t.setheading(0)
        t.color(0, 0, 0)
        print("P_D_line 成功")
        return True
    except Exception as e:
        print("P_D_line 失败:", e)
        return False

def E_line(expr):
    try:
        # 解析直线函数表达式并获取斜率和截距
        parts = expr.split("=")
        if len(parts) != 2:
            print("请输入正确的直线表达式(y=kx+b)")
            return False
        line_expr = parts[1].strip()
        if line_expr == "x":  # 如果表达式为 y=x
            t.color(0, 0, 0)  # 黑色
            t.pu()
            t.goto(-200, -200)  # 选择一个起始点
            t.pd()
            t.goto(200, 200)  # 终点
            t.pu()
            print("E_line 成功")
            return True
        else:
            k, b = 1, 0  # 斜率为1，截距为0
            if "x" in line_expr:  # 如果表达式包含x
                if line_expr.startswith("x"):  # 如果表达式以x开头，即斜率为1
                    b = float(line_expr[1:]) if len(line_expr) > 1 else 0  # 截距为表达式中x后面的数值，如果没有则为0
                else:
                    k, b = map(float, line_expr.split("x"))  # 解析斜率和截距
            # 调用直线绘制函数
            t.color(0, 0, 0)  # 黑色
            t.pu()
            t.goto(-10000, k * -10000 + b)
            t.pd()
            t.goto(10000, k * 10000 + b)
            t.pu()
            print("E_line 成功")
            return True
    except Exception as e:
        print("E_line 失败:", e)
        return False

def Error():
    print("未匹配到任何函数")
    return False


t.speed(0)
t.pensize(10)
line("y=x+100")  # E_line 成功，黑色
line((-100, -100),(100,100))#P_P_line 成功，绿色
line((-100, -100),3.1)#P_D_line 成功,,红色
line((50, 50),100,0.5)#P_L_D_line 成功,蓝色
line()#未匹配到任何函数



t.done()
