s="123-456-789".split("-")
print(s)
print(type(s))

s=[]    #创建列表s

s=[1,.1,123+123j]
print(s)

s=[1,[2,1]]
print(s)

s.append(4)#末尾添加元素
print(s)
s.insert(2,"x")#索引位置插入元素
print(s)

s.pop()#删除末尾
print(s)
s.pop(1)#删除引位置元素
print(s)

s.remove(1)#移除指定元素，重复值只移除第一个
print(s)
s.remove("x")
print(s)

s=[1,.1,123+123j,1,1,2,1]
print(s.count(1))#查找指定元素出现的数量
s=[1,2,5,3,4,6,9,7]
s.sort()#从小到大排序
print(s)
s.reverse()#从大到小排序
print(s)

s=[1,.1,123+123j,1,1,2]
print(s[0])
print(s[-1])#倒数
s[:]      #相当于s[0:4]
s[:3]
s[4:]=[1,2,2,2,2,2,]
print(s)
s.append(11)

m=s+[4,2,3]
print(m)
m*=3
print(m)
print(m.index(2))
print(2 in s)
print(max(m))


