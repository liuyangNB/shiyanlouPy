#!/usr/bin/env python3
import sys

def Min2Hous(minus):
    if minus<0:
        raise ValueError("输入的数据要求是正数")
    else:
        print("{} H,{} M".format(minus//60,minus%60))


try:
    Min2Hous(int(input("please inout Minutes:")))
except:
    print("Parameter Error")