
"""一般的定义什么的就不说了"""

# 局域或全局变量；局部的是局部的，全局的是全局的

#默认参数和C++一样，默认了后面的也要默认
#默认值是可变对象比如列表、字典等，每次调用都会影响

def fun(a, data = []):
    data.append(a)
    return data

#避免默认参数累计的情况
def fun2(a,data = None):
    if data == None:
        data = []
    data.append(a)
    return  data

print('--------1---------')
print(fun(1))
print(fun(2))
print(fun(3))
print('--------2---------')
print(fun2(1))
print(fun2(2))
print(fun2(3))
print('--------3---------')
mylist = []
print(fun2(1,mylist))
print(fun2(2,mylist))
print(fun2(3,mylist))
print(mylist)
print('--------4---------')

print("""关键字参数""")
def fun3(a, b=5, c=10):
    print('a =', a,' b = ', b,' c = ', c)

fun3(12,24)
fun3(12,c=24)
fun3(b=12,c=24,a=-1)

print("""强制关键字参数""")
def fun4(a,*,b,c):
    print('a =', a,' b = ', b,' c = ', c)

#fun4(1,2,3)#不现实，是错误的
fun4(1,b=2,c=3)

print('--------5---------')
print("""文档字符串""")

def fun5(a,b):
    """这是我写的加法，看着办吧"""
    return a+b

print(fun5.__doc__)
print(fun5(1,2))

print('--------6---------')
print("""高阶函数;仿函数""")
#可以接受函数作为参数的函数；返回函数
def highfun(list):
    return [i.upper() for i in list]

def fun6(fun,list):
    return fun(list)
print(highfun("abcde".split()))
print(fun6(highfun,"abcde".split()))

print('--------7---------')
print("""map函数（高阶函数）""")
"""map 是一个在 Python 里非常有用的高阶函数。
它接受一个函数和一个序列（迭代器）作为输入，
然后对序列（迭代器）的每一个值应用这个函数，
返回一个序列（迭代器），其包含应用函数后的结果。"""
mylist = [1,2,3,4]#一个坑，用list做变量名有问题噢
def square(i):
    return i*i
v
print(list(map(square,mylist)))#python3 生成的是迭代器 不是list;

