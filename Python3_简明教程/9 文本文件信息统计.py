#! python3
"""让我们试着编写一个程序，对任意给定文本文件中的制表符、行、空格进行计数。"""

import os
import sys

def pase_file(path):

    fd = open(path,encoding='utf-8')
    i=space_num=table_num=0
    for i,line in enumerate(fd):
        space_num += line.count(' ')
        table_num+=line.count('#')

    fd.close()

    return  space_num,table_num

path=r"C:\Users\Liuyang_TP\PycharmProjects\shiyanlou\Python3_简明教程\说明.md"
print(pase_file(path))
