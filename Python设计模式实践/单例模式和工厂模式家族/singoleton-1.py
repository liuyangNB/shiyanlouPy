#-*-coding:utf-8 -*-

class Singleton(object):
    """单例模式"""

    class _A(object):
        """真正干活的对外隐藏"""
        def __init__(self):
            pass

        def display(self):

            return id(self)

    #类变量，用于存储 _A的实例
    _instance = None

    def __init__(self):
        """先判断类变量中是否已经保存了 _A的实例，如果没用则创建一个后返回"""
        if Singleton._instance == None:
            Singleton._instance = Singleton._A()

    def __getattr__(self, item):
        """所有的属性都应该直接从 singleton._instance 获取"""
        return getattr(self._instance,item)



if __name__ == '__main__':
        #创建两个实例
        s1 = Singleton()
        s2 = Singleton()
        #s3 = Singleton(s1) 没用默认的复制构造函数
        print("s1的id：",id(s1),s1._instance.display())
        #print("s1的id：", id(s1), s1.display())
        print("s2的id：", id(s2), s2._instance.display())
        #print("s3的id：", id(s3), s3._instance.display())

"""从输出中可以看到，尽管我们创建了两个不同的实例（实例 ID 不同），
但是访问其属性的时候得到的 ID 是一致的。以上代码虽然很好的实现了单例模式，
但是在真正的项目开发中这种方式却不够灵活，因为我们要将真正干活的类内置在单例类中。 
"""