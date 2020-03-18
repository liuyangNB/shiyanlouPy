import numpy as np

a = np.random.random((3,2))

print('a=\n',a)

#查看数组形状
print('a.shape=',a.shape)

#更改数组形状（原数组不变）
print('a.reshape(2,3)=\n',a.reshape(2,3))
print('a=\n',a)

#改变形状，改变原数组
#print('a.resize(2,3）=\n',np.resize(a,(2,3)))
print('a.resize(2,3）=\n',a.resize(2,3))#这是个操作，不返回啥
print('a=\n',a)

#展平数组
print('a.ravel()=\n',a.ravel())
print('a=\n',a)

####################
print("垂直拼接")
a = np.random.randint(10, size=(3, 3))
b = np.random.randint(10, size=(3, 3))
print('a=\n',a)
print('b=\n',b)
print('np.vsrack((a,b))=\n',np.vstack((a,b)))

print("水平拼接")
print('np.hsrack((a,b))=\n',np.hstack((a,b)))