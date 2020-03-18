
def mylistfun():
    print('-----------列表基础---------------')
    a = [1,2,3,4,5,6,7,8,9]
    a.append(10)        #[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print(a)

    a.insert(0,0)       #[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print(a)

    a.insert(len(a),0)  #[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 0]
    print(a)
    print(a.count(0))

    a.remove(0)#只会删除第一个
    print(a)

    a.reverse()         #[0, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
    print(a)

    b=[10,11,12]
    a.extend(b)         #[0, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 10, 11, 12]
    print(a)

    a.sort()
    print(a)            #[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 11, 12]

    #删除某位置的列表元素
    del a[-1]           #[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 11]
    print(a)

    print('-----------列表作为栈和队列---------------')
    a = [1,2,3,4,5,6]
    print(a)

    print('a.pop',a.pop())
    print(a)

    a.append(10)        #[1, 2, 3, 4, 5, 10]
    print(a)

    #pop(0)是弹出前面的== popfront()
    a.pop(0)            #[2, 3, 4, 5, 10]
    print(a)

    print('-----------列表推导式---------------')

    print( [(x,y) for x in range(0,3) for y in range(0,3)])

    print('-----------列表解析---------------')

    M = [[1,2,3],[4,5,6],[7,8,9]]
    print([r[1] for r in M])
    print([r[1] for r in M if r[1]%2==0])

    print('-----------元组---------------')

    a = (1,2,3,4,5)
    ##del a[0]  不能删除元组元素

    #一个元素时候的元组表示
    b = (1,)
    print(type(b))          #<class 'tuple'>

    #访问
    print(a[1])             # 2

    #不能修改,但是
    a = (1,2,['x','y'])
    print(a)

    # a[2] = ['A','B']
    # print(a)
    a[2][0]='A'
    a[2][1]='B'
    print(a)
    #不能修改是指元组的指向不能改，这里a[2]指向一个list，不能通过元组改list，但是可以直接去到list啊
    ########################
    print('-----------集合---------------')
    """集合是一个无序不重复元素的集。基本功能包括关系测试和消除重复元素。
    集合对象还支持 union（联合），intersection（交），difference（差）
    和 symmetric difference（对称差集）等数学运算。"""

    s = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
    print('apple'in s)

    a = set('apple')
    print('a:',a)
    b = set('orange')
    print('b:',b)
    print('a-b:',a-b)# a 有而 b 没有的字母
    print('a|b:',a|b)
    print('a&b:',a&b)
    print('a^b:',a^b)# 存在于 a 或 b 但不同时存在的字母

    print(s.pop())#随机删除一个元素
    print(s)
    s.add('shit')
    print(s)

    print('-----------字典---------------')
    """key:value;其中key要各不相同，且要求是不可变类型"""
    data = {'kushal': 'Fedora', 'kart_': 'Debian', 'Jace': 'Mac'}
    print(data)

    ##添加新键
    data['lau']='haha'
    print(data)

    ##删除键
    del data['lau']
    print(data)

    ##添加键值对还要判断键在不在字典里，性能低啊，咋么办？
    myd = {2:'b',3:'c'}
    myd.setdefault(1,'a')
    print(myd)
    myd.setdefault(1, 'a')
    print(myd)
    myd[1]='b'#这是修改键值对映射
    print(myd)
    myd.setdefault(1, 'A')#这是判断有没有，有就不加，没用就加
    print(myd)

    #用get(key,defaultval)来索引，如果找不到就会返回defaultval
    print(myd.get('a','can not find'))

def mymatirx():
    n = int(input("Enter the value of n: "))
    print("Enter values for the Matrix A")
    a = []
    for i in range(n):
        a.append([int(x) for x in input().split()])
    print("Enter values for the Matrix B")
    b = []
    for i in range(n):
        b.append([int(x) for x in input().split()])
    c = []
    for i in range(n):
        c.append([a[i][j] * b[i][j] for j in range(n)])
    print("After matrix multiplication")
    print("-" * 7 * n)
    for x in c:
        for y in x:
            print(str(y).rjust(5), end=' ')
        print()
    print("-" * 7 * n)

def mysplitfun():
    a = input("请输入一堆数据，可以分割的：").split()
    print(a)


mysplitfun()
