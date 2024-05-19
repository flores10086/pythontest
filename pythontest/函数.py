# 定义和调用
def hello():
    print("hello")
    print("dd")
hello ()
hello ()
hello ()

# 函数的参数
def hello2(hi,name="1"):
    print("hello",name)
hello2("d")
hello2("d]s")

def f(l=[]):
    l.append(1)
    print(l)
f()
f()

def ff(*args,**kwargs):
    print(args)
    print(kwargs)
    print("-"*20)
ff(1,2,3)
ff(same="same")
ff()

# 函数的返回值
a=ff()
print(a)
def add(a,b):
    c=a+b
    print(f"{a}+{b}的计算结果是：",c)
    return [a,b,c]
res=add(1,10)
print(res)
print(add(res[2],100))

# 匿名函数
def f(add):
    print("收到函数{}".format(add))
    print("调用函数{}".format(add(1,2)))
f(lambda a,b:a+b)

# 内置函数
type()#查看数据类型
isinstance()#判断变量是否为某一类型
dir()#查看变量拥有的函数
help()#获取变量的帮助信息
id()#查看地址
