# print(1)
# 1/0
# print(2)
# # 停止执行
# # 向上传播
# # 打印错误信息
# assert 1==2
# raise KeyError("hello")

# 捕捉异常
try:
    1/0
except Exception as e:
    print("bu".format(e))
print(1)
