l = []    #全局变量
d ={
"A" :[],
"B" :[],
}
def get_input():
    while True:
        content = input("请输入内容!")   # 发言格式:A:xxxx   B:uyyyy
        l=content.split(":")        # 列表的第一项是身份，第二项是发言内容
        try:
            user,text=l[0],l[1]
            return user,text
        except Exception as e:
            print("重新输入")
            continue
def handle(user,text):
    d.setdefault(l[0],[])
    if text=='exit':
        return 'exit'
    elif text=='log':
        print(d)
    else:
        d[user].append(text)
        print(text)
    print(d)
while True:
    get_input()#获取输入
    ret=handle()#处理
    if ret is not None:
        break