#print格式化、eval()、input()

Tempstr = input("请输入当前温度：")
if Tempstr[-1] in ['F','f']:
    C = (eval(Tempstr[0:-1]) - 32)/1.8
    print("转换后温度是：{:.2f}C".format(C))
elif Tempstr[-1] in ['c','C']:
    F = 1.8*eval(Tempstr[0:-1]) + 32
    print("转换后温度是：{:.2f}F".format(F))
else:
    print("输入格式有误")