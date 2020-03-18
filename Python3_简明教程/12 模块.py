

print("-------------------模块----------------------------")
"""模块相当于定义了一堆的定义，然后其他的地方可以import并使用"""
import BarModue
BarModue.starbar(10)

from BarModue import hashbar
hashbar(9)

print("-------------------包----------------------------")
"""含有__init__.py文件的目录可以用来作为一个包，目录里所有.py文件都是包的子模块"""
#名字别写错
from mymodule.BarModue import starbar
from mymodule.UtilModue import Utilfun1

starbar(11)
Utilfun1(1)

print("-------------------默认模块----------------------------")