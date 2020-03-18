import numpy as np



#统计数组中位数
a = np.array([[1,4,3],
              [6,2,9],
              [4,7,2]])
print("中位数：np.median(a,axis = 0)\n",np.median(a,axis=0))#axis = 0 是对列做处理，投影到x轴 ；axis = 1 反之

#统计平均数
print("平均数：np.mean(a,axis=1)\n",np.mean(a,axis=1))

#统计各个行的的加权平均
print('加权平均：np.average(a,axis=0)\n',np.average(a,axis=0))

#统计各行标准差
print("方差：np.var(a,axis=0)\n",np.var(a,axis=0))

#统计各行标准差
print("标准差：np.std(a,axis=0)\n",np.std(a,axis=0))