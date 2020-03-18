

def mywhilefun():
    print("--------------while-----------------")

    x = float(input("please input a num x :"))
    n = term = num = 1
    res = 1.0
    while n<=100:
        term *= x/n
        res+=term
        n+=1
        if term <0.0001:
            break
    print("No of times = {} ; Sum = {}".format(n,res))
    print("--------------while-----------------")

def mylist():
    print('----------list first----------------')
    a = [1,2,3,4,5,'a','b','c']

    #切片：
    print('a[0],a[1],a[-1]:',a[0],a[1],a[-1])
    print('a[0:5]:',a[0:5])
    print('a[-1:5]:', a[-1:5])
    print('a[5:-1]:', a[5:-1])
    print('a[1::2]',a[1::2])

    a[5:8] = ['A','B','C']
    print('after a[5:8] = [\'A\',\'B\',\'C\'] a:',a)
    a[5:8]=[]
    print('after a[5:8]=[] a:', a)
    print('-----------for x in a-----------------')
    for x in a:
        print(x,end=' ')
    print('\n')
    print('-----------for x in a[::2]-----------------')
    for x in a[::2]:
        print(x,end=' ')




def for_else():
    """顺利完成就进入else，bureak中断循环就不进入"""

    for i in range(0,10):
        print(i,end=' ')
    else:
        print('\nwell, finish for without break\n')

    for i in range(0,10):
        print(i,end=' ')
        if i == 8:
            break
    else:
        print('\nwell, finish for without break\n')


for_else()