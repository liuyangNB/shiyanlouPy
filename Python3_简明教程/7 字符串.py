import  re


def mystringfun():
    print('--------------------一般操作--------------')
    str = 'yo yo yo, say my name'
    print(str.split())
    print(str.split(','))#自带的不能多个分隔符分割，要用正则
    print(re.split(r"[\s,]+",str)) # +筛选出非空的
    print(str.title())
    print(str.upper())
    print(str.lower())
    print(str.title().swapcase())#大小写反一下
    print('--------------------文本搜索--------------')

    print(str.find('say'))
    print(str.startswith('yo'))

    print('--------------------一般操作--------------')





mystringfun()