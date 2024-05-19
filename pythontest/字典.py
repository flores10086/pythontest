# 字典dict key-value key不可重复
d = {"key": 1}
print(type(d))

d = dict(a=1, b=2)
print(d)

print(d["a"])
print(d.get("a"))
print(d.get("ad"))
print("a"in d)
print("asd" in d)

print(d.keys())
print('a' in d.keys())
print(d.values())
print(d.items())
print(len(d))
print(list(d))
print(d)
d['d']=4
print(d)
d_2={"x":"X","y":"Y"}
d.update(d_2)
print(d)

d.pop('x')
print(d)
print(d.pop('xx', '不存在'))

print(d.setdefault('xxx', '123'))
print(d.setdefault('x', 'asd'))

d.clear()
print(d)
