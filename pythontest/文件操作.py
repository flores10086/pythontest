# f1=open(file,mode='r',buffering=-1,encoding=None,errors=None,newline=None,closefd=True,opener=None)
# f1.close()

#
# with open(filename,mode,encoding)as fp:
#     #写语句
# with open('test.txt','r')as src,open('texxt_new.txt','w')as dst:
#     dst.write(src.read())


# r 读模式
# w 写模式
# x 写模式，创建新文件
# a 追加模式
# b 二进制模式
# t 文本模式
# + 读写模式

# 文件对象常用属性
# buffer 返回当前文件的缓冲区对象
# closed 判断文件是否关闭
# fileno 文件号
# mode 返回文件的打开模式
# name 返回文件的名称

s='hello world\n'
with open('sample.txt','w')as fp:
    fp.write(s)
with open('sample.txt')as fp:
    print(fp.read())

with open('sample.txt','r')as f:
    s=f.read(5)
print('s=',s)

with open('sample.txt')as fp:
    for line in fp:
        print(line)


s='中国'
fp=open(r'D:\sample.txt','r')
fp.write(s)
fp.close()