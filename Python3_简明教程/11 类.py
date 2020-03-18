"""
主要的知识点：
    简单定义
    __init__的方法
    python的继承
    多继承
    删除对象
    属性的读取方法
    装饰器
"""
print('--------------基本定义---------------------')
class MyClass(object):
    i = 123456
    def fun(self):
        return 'hello word'

#类对象的创建
x = MyClass()
print(x.fun())

print('--------------类的初始化__init__()，相当于构造函数------------')
class Comples:
    def __init__(self,realpart, imagpart):
        #self指类对象，同c++的self指针
        self.r = realpart
        self.i = imagpart

x = Comples(1,2)
print(x.r,x.i)

print('--------------继承------------')
"""继承父类所有功能（变量和方法）等"""
class Person(object):

    def __init__(self,name='无名',gender='不知'):
        self.name = name
        self.gender = gender

    def get_details(self):
        print("name is:{}; gender is :{}".format(self.name,self.gender))


class Student(Person):
    def __init__(self,name='无名',gender='不知',branch='不知'):
        Person.__init__(self,name,gender)#student这个类作为person的角色也是要初始化的
        self.branch = branch

    def get_details(self):
        print("这是一个学生，先看看作为人的信息：{}；再看看作为学生的信息：{}".format((self.name,self.gender),self.branch))

person1 = Person()
person1.get_details()

st1 = Student(gender='man',branch='1')
st1.get_details()

print('--------------多继承------------')
"""就是一个类可以继承多个类，具有父类所有的变量和方法"""

class Superman(Person,MyClass,Comples):
    def __init__(self):
        Person.__init__(self)
        MyClass.__init__(self)
        Comples.__init__(self)

print('--------------删除对象------------')
"""用del，实际上是使对象的引用计数减一，当对象的引用计数变为0时候，垃圾回收会删除这个对象"""

del st1
st1.get_details()

print('--------------装饰器------------')
"""调整控制属性访问权限，使用@property装饰器，就是负责把一个方法编程属性调用的"""

#举个栗子，银行账户例子：
    #没人能设置金额为负数
    #要有个只读属性cny返回换算成rmb的金额
class Account(object):
    def __init__(self,rate):
        self.__amt = 0
        self.rate = rate

    @property
    def amount(self):
        return self.__amt

    @property
    def cny(self):
        return self.__amt*self.rate

    @property
    def amount(self,value):
        if value < 0:
            print("sorry, no negative amount in the account")
            return
        self.__amt=value

acc=Account(rate=6.6)
acc.amount = 20

print("Dollar:",acc.amount)
print("CNY:",acc.cny)

acc.amount=-10
print("Dollar amount:",acc.amount)