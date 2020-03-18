#! python3
#-*-coding:utf-8 -*-
# fobj = open("说明.md",encoding='utf-8')
#
# print(fobj.readline())
# print(fobj.readline())
# fobj.close()
# #print(fobj.readline()) #关掉了就读不了
#
# name = input("enter the file name:")
# fobj = open(name,encoding='utf-8')
#
# print(fobj.readline())


"""写个模块作为拷贝到另一个文件"""
import sys
if len(sys.argv)<3:
    print("参数输入有误：")
    print("./脚本名.py filename_s filename_d")
    sys.exit(1)
f1 = open(sys.argv[1])
s = f1.read()
f1.close()
f2 = open(sys.argv[2],'w')
f2.write(s)
f2.close()