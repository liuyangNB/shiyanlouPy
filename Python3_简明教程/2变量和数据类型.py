"""
知识点：
    1 python 关键字
    2 变量的定义与赋值
    3 input() 函数     num = int(input("请输入整数"))
    4 字符串的格式化   print("对应的华氏度是：{:5.2f}" .format(num_f))#格式化输出
"""
def myinputfun():
    num = int(input("请输入整数"))

    if num<0:
        print("你输入的是负数",num)
    else:
        print("你输入的是正数",num)

def C2F_deg():
    num_c = float(input("请输入摄氏度："))

    num_f = (num_c-32)/1.8

    #print("对应的华氏度是：",num_f )
    print("对应的华氏度是：{:5.2f}" .format(num_f))#格式化输出


#单行定义多个变量或赋值
def exchange():
    a,b = 1,2
    print("交换之前a,b:",a,b)
    a,b = b,a
    print("交换之后a,b:", a, b)

    #元组拆封
    data = ("wo","shi","shui?")
    a,b,c = data
    print("a,b,c:",a,b,c)




exchange()