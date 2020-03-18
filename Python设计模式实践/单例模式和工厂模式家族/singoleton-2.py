# -*- coding: utf-8 -*-

class Singleton:
    """
    单例类装饰器，可以用于实现单例的任何类。注意，不能用于多线程环境。
    """
    def __init__(self,cls):
        """需要的参数是一个类"""
        self._cls = cls

    def Instance(self):
        """返回真正的实例"""
        try:
            return self._instance
        except AttributeError:
            self._instance = self._cls()
            return self._instance

    def __call__(self):
        raise TypeError("Singleton must be accessed through \'Instance()\'.")

    def __instancecheck__(self, inst):
        return isinstance(inst,self._decorated)

@Singleton
class A:
    """一个需要单例模式的类"""
    def __init__(self):
        pass

    def display(self):
        return id(self)

if __name__ == '__main__':
    #s1 = A()#报错：TypeError("Singleton must be accessed through \'Instance()\'.")
    #s2 = A()
    s1 = A.Instance()
    s2 = A.Instance()
    print("s1",id(s1),s1.display())
    print("s2",id(s2),s2.display())

"""
以上代码中，我们用装饰器实现了单例模式，任何想使用单例模式的类，只需要使用 Singleton 装饰器装饰一下就可以使用了。可以看到其核心工作原理其实和第一种实现方式是一致的，也是使用内置的属性 Singleton._instance 来存储实例的。通过使用装饰器的模式我们将代码解耦了，使用更加灵活。其实这里我们也用到装饰者模式啦。

那单例模式在 实验楼 中用到了什么地方呢？实验楼是使用 Web 框架开发的，在常见的 Web 框架中有很多扩展，比如数据库扩展，有了数据库扩展我们可以很方便的在应用中使用数据库了。但是这里面有一个问题就是：是不是每次我们使用数据库的时候都需要连接数据库呢？

当然不是，我们可以使用单例模式来保证连接数据库只会发生一次。下面我们看看一个简单的 Flask Web 框架的 sqlite 扩展。


"""