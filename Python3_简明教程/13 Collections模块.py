#这个模块实现了一些很好的数据结构
import collections

#print(help(collections))

print('-----------Counter类--------------')
"""Counter 是一个有助于 hashable 对象计数的 dict 子类。
它是一个无序的集合，其中 hashable 对象的元素存储为字典的键，
它们的计数存储为字典的值，计数可以为任意整数，包括零和负数。"""

"""Counter是一个简单的计数器,实际上是dict的一个子类"""
from collections import Counter

c = Counter()

for ch in "programming":
    c[ch] = c[ch]+1

print(c)
print(list(c.elements()))#乱序set
print(c.most_common())#按频次排序

#看看记录单词的频次
import re
path = r'C:\Users\Liuyang_TP\PycharmProjects\shiyanlou\Python3_简明教程\说明.md'
words = re.findall('\w+',open(path,encoding='utf-8').read().lower())
print(Counter(words).most_common(10))#显示按照re

print('-----------defaultdict类--------------')
"""使用dict时，如果引用的Key不存在，就会抛出KeyError。如果希望key不存在时，返回一个默认值，就可以用defaultdict"""
from collections import defaultdict

ddm=defaultdict(lambda :'N/A')
ddm['k1']=1
print(ddm['k1'])
print(ddm['k2'])

#其他和dict一样了
s = [('a',1),('b',2),('c',3),('a',1),('b',2)]
d = defaultdict(list)
for k,v in s:
    d[k].append(v)
print(d)
print('-----------OrderDict--------------')
"""使用dict时，Key是无序的。在对dict做迭代时，我们无法确定Key的顺序。如果要保持Key的顺序(按插入顺序)，可以用OrderedDict："""

from collections import OrderedDict

d = dict( [('a',1),('b',2),('c',3)])#普通dict是无序的???
print('dict:',d)
od = OrderedDict([('a',1),('b',2),('c',3)])
print('Od:',od)

print('-----------deque--------------')

from collections import deque
myl = 'a b c'.split()
q = deque(myl)
print(q)
q.append('x')
q.appendleft('Y')
print(q)

q.pop()
print(q)

q.popleft()
print(q)

print('-----------namedtuple--------------')
"""命名元组有助于对元组每个位置赋予意义，并且让我们的代码有更好的可读性和自文档性。
你可以在任何使用元组地方使用命名元组。在例子中我们会创建一个命名元组以展示为元组每个位置保存信息。"""

"""但是，看到(1, 2)，很难看出这个tuple是用来表示一个坐标的。
定义一个class又小题大做了，这时，namedtuple就派上了用场"""

from collections import namedtuple

Point = namedtuple('Point',['x','y'])
p = Point(1,y=2)

print("(x,y)=",p.x,p.y)