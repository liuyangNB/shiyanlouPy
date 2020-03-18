
print("------------迭代器--------------")
"""迭代器可以看作是一个特殊的对象，
每次调用该对象时会返回自身的下一个元素，
从实现上来看，一个迭代器对象必须是定义了__iter__()方法和next()方法的对象。"""

class Counter(object):
    def __init__(self,low,high):
        self.current = low
        self.hig = high

    def __iter__(self):
        return self

    def __next__(self):
        #返回下一个值，直到当前值大于high
        if self.current > self.hig:
            raise StopIteration
        else:
            self.current+=1
            return self.current-1


c = Counter(5,7)

print(next(c))
print(next(c))
print(next(c))
#print(next(c)) 到头了

print("------------生成器表达式--------------")
# [列表解析] --> (生成器)
mlist = [x*x for x in range(5)]
print(mlist)

g = (x*x for x in range(5))
print(g)
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
#print(next(g)) Stop

print("------------生成器 yield--------------")
def odd():
    for i in range(5):
        if i%2 == 0:
            yield i

myo = odd()
print(myo)
print(next(myo))
print(next(myo))
print(next(myo))
#print(next(myo))

print("------------闭包--------------")
""" 是什么，长什么样子的？
        嵌套至少两层函数，返回最内函数名
        
    有什么用，为了解决什么问题？
        保存函数的状态信息，使函数的局部变量信息可以保存"""

def add_number():

    num = 0
    def adder(number):
        return num + number
    return adder

a = add_number()    #a其实是一个“函数指针”
print(a(10))
print(a(2))


print("------------装饰器--------------")
"""
形式：
    闭包
作用：
    拓展函数功能；因为大型项目函数里面直接修改东西不好，会产生其他意想不到的事情，不改变原函数而添加功能就使用装饰器
"""



#函数为参
def mydecorator(fun):

    def dec_fun(*argv,**kwargs):
        print("new_add_before")
        fun(*argv,**kwargs)
        print("new_add_after")

    return dec_fun


def my_originfun(num_dec=0):
    print("这是我的原始函数:",num_dec)

@mydecorator
def my_originfun1(num_dec=0):
    print("这是我的原始函数_加入语法糖:", num_dec)

print('1---------')
my_originfun()
print('2---------')
mynewfun = mydecorator(my_originfun)#一定是要函数指针噢
mynewfun(1)
print('3---------')
my_originfun1()

