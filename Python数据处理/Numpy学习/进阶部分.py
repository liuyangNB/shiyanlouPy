import numpy as np

#1 创建5X5的数组，边界为1，其余为0
print("--------------------------")
a = np.ones((5,5))
a[1:-1,1:-1]=0
print('#1:\n',a)

#2 使用数字0将一个全为1的5x5数组包围   [pad]
print("--------------------------")
'''
pad(arr,pad_width,mode,constant_values)
参数： 
    pad_width：维度的各个方向上想要填补的长度,
                如（（1，2），（2，2）），上1下2，左2右2
         
'''
a = np.ones((5,5))
a = np.pad(a,pad_width=((1,1)),mode='constant',constant_values=8)
print('#2:\n',a)

#3. 创建一个 5x5 的二维数组，并设置值 1, 2, 3, 4 落在其对角线下方     [diag]
print("--------------------------")
a = np.diag(1+np.arange(4),k=-1) # np.diag([list]) 以list为对角线形参数组
#a = np.diag(np.arange(4)-1,k=-1)+1#拓展
print('#3:\n',a)


#4 创建一个 10x10 的二维数组，并使得 1 和 0 沿对角线间隔放置    【；；2，1：：2】奇数偶数下标
print("--------------------------")
a = np.zeros((10,10),dtype=int)
a[1::2,::2]=1#行1开始间隔2(奇数行)，对应列的间隔2
a[0::2,1::2]=1#偶数行的奇数列
print('#4:\n',a)

#5 创建一个 0-10 的一维数组，并将 (1, 9] 之间的数全部反转成负数：
print("--------------------------")
#a = [-x if (x>1 and x <=9) else x for x in range(11) ] ##我的想法
a = np.arange(11)
a[(a>1)&(a<=9)] *=-1
print('#5:\n',a)

#6找出两个一维数组中相同的元素：
print("--------------------------")
Z1 = np.random.randint(0,10,10)
Z2 = np.random.randint(0,10,10)
print(Z1,Z2)
a = np.intersect1d(Z1,Z2)
#a = list(set(Z1)&set(Z2))#& | & - 【集合操作】
print('#6:\n',a)

#7使用 NumPy 打印昨天、今天、明天的日期
print("--------------------------")
yesterday = np.datetime64('today', 'D') - np.timedelta64(2, 'D')#多少天以前
today     = np.datetime64('today', 'D')
tomorrow  = np.datetime64('today', 'D') + np.timedelta64(1, 'D')
print('#7')
print("yesterday: ", yesterday)
print("today: ", today)
print("tomorrow: ", tomorrow)


#8使用五种不同的方法去提取一个随机数组的整数部分
print("--------------------------")
a = np.random.uniform(1,10,10)#均匀分布的【1，10）采样10个

print('#8a',a)
print(a//1)
print(a-a%1)
print(np.floor(a))#向下取整
print(np.trunc(a))#截断



#9创建一个 5x5 的矩阵，其中每行的数值范围从 1 到 5
print("--------------------------")
#a = np.random.randint(1,5,(5,5)) 理解错题意了

a = np.zeros((5,5))
a+=np.arange(1,6)
print('#9:\n',a)

#10创建一个长度为 5 的等间隔一维数组，其值域范围从 0 到 1，但是不包括 0 和 1
print("--------------------------")
a = np.linspace(0,1,6,endpoint=False)[1:]  ##划分区间
print('#10:\n',a)