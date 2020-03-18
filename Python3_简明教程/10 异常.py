
"""
几种常见的报错：
    NameError：未定义变量
    Type Error：操作类型不恰当
处理异常：
    try...except
    如果捕获到的异常是你想要捕获的刚好执行下去，如果不是你想要的那就还是报错

"""

def myfun():
    try:
        a = input('input:')#输入的时候按下ctrl +c 中断产生keyboardInterrupt
        return a+2

    except ValueError:
        print("value error")
    except TypeError:
        print("type error")
    except:
        print("unknow error")

myfun()