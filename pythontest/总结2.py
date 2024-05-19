l = []
d={
"A":[],
"B":[],
}
while True:
    content = input("请输入内容!")   #发言格式:A:xxxx   B:uyyyy
    l=content.split(":")        #列表的第一项是身份，第二项是发言内容
    d.setdefault(tuple([l[0]]),tuple(l[1]))
    d[l[0]].append(l[1])

    print(d)

