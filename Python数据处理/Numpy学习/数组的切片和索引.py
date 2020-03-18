import numpy as np

a = np.array([x for x in range(5)])

#一维索引
print('a[0],a[-1]=',a[0],a[-1])
print('a[0:2]=',a[0:2])

#二维数组索引
print('------二维---------')
a = np.array([(1, 2, 3), (4, 5, 6), (7, 8, 9)])
print('a=\n',a)
print("a[0], a[-1] = ",a[0], a[-1])

#二维数组切片
print('取第二列a[:,1]=',a[:,1])
print('取2，3行a[1:3,:]=\n',a[1:3,:])