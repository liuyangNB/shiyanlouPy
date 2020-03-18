# *_*coding:utf-8 *_*
import numpy as np
#--------------------------------------------数组运算）））））））））））））））））
a = np.array([10*i for i in range(1,6)])
b = np.arange(1,6)
print("a,b = ",a,b)

print('a+b',a+b)
print('a-b',a-b)
print('a*b',a*b)#<a,b> 点乘
print('a/b',a/b)


print("------------二维数组-------------")
#生成二维数组（矩阵）
A = np.array([[1,2],[3,4]])
B = np.arange(5,9).reshape(2,2)
print("A：\n",A)
print("B：\n",B)
print("A+B  ：\n",A+B)
print("A-B  ：\n",A-B)
print("A*B  ：\n",A*B)#还是点乘！！！
print("A/B  ：\n",A/B)
print('///矩阵乘法运算，叉乘///')
print("A x B (np.dot(A,B)):\n",np.dot(A,B))
print("np.mat(A) * np.mat(B):\n",np.mat(A)*np.mat(B))

print("3*A:\n",3*A)
print("A.T(转置)\n",A.T)
print("A.inv(求逆)\n",np.linalg.inv(A))#需要nxn矩阵
