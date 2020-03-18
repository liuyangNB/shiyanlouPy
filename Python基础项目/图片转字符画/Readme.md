#根据实验楼项目在本地PyCharm实现

1.1 实验知识点
本节实验中我们将实践以下知识：

Linux 命令行操作
Python 基础
pillow 库的使用
argparse 库的使用（参考教程）


# 原理
一个彩色画的像素点怎么用单色表示，引入灰度值的概念了。
> 灰度值：指黑白图像中点的颜色深度，范围一般从0到255，
白色为255，黑色为0，故黑白图片也称灰度图像

gray ＝ 0.2126 * r + 0.7152 * g + 0.0722 * b

#需要的库
pillow


* from PIL import Image
* import argparse

