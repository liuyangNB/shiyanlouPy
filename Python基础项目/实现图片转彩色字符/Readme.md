# 了解Pillow和Docopt

##知识点：
* 使用Pillow库操作图像
* 使用docopt库构建命令行解析器
* 使用转移字符改变Bash界面中输出的字符样式

[Pillow文档](https://pillow-zh-cn.readthedocs.io/zh_CN/latest/handbook/overview.html)

###docopt
docopt 是 Python 的一个第三方参数解析库，可以根据使用者提供的文档描述自动生成解析器。
因此使用者可以用它来定义交互参数与解析参数。

docopt 最大的特点在于不用考虑如何解析命令行参数，而是当你把心中想要的格式按照一定的规则写出来后，解析也就完成了。

有了 docopt 这样的神器之后，构建命令行解析器简直如鱼得水。而我们唯一需要做的就是好好考虑程序需要接受哪些参数，然后编写帮助文档



##程序逻辑
1 获取命令行参数并解析
2 加载处理的指定图像
3 将图像像素转换为对的字符
4 在终端按指定格式输出彩色的字符图像



import  os
os.system("")#按照网上的说法，加上这个就玄学般可以在cmd显示转义序列