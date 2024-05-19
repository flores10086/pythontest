l = []
d ={
"A" :[],
"B" :[],
}
while True:
    content = input("请输入内容!")   # 发言格式:A:xxxx   B:uyyyy
    l=content.split(":")        # 列表的第一项是身份，第二项是发言内容
    try:
        user,text=l[0],l[1]
    except Exception as e:
        print("重新输入")
        continue
    d.setdefault(l[0],[])
    if text=='exit':
        break
    elif text=='log':
        print(d)
    else:
        d[user].append(text)
        print(text)
    print(d)

