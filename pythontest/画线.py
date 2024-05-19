import turtle as t
import random as rd
def line():
    

    return

def P_P_line(Pa,Pb):#两点法
    try:
        pos=t.pos()
        t.pu()
        t.goto(Pa)
        t.pd()
        t.goto(Pb)
        t.pu()
        t.goto(pos)
        return True
    except Exception as e:
        print("绘画失败!",e)
        return False


