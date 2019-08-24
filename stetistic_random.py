# _*_ coding=utf-8 _*_


import numpy as np

"""统计方法和随机数，随机函数在np.random子包内
"""
"""---统计方法---"""
arr = np.arange(10)
# sum 求和
print(arr.sum())
# mean 求平均数
print(arr.mean())
# std 求标准差
print(arr.std())
# var 求方差
print(arr.var())
# min 最小值
print(arr.min())
# max 最大值
print(arr.max())
# argmin 求最小值索引
print(arr.argmin())
# argmax 最大值索引
print(arr.argmax())

"""---随机函数---"""
# randint随机函数生成整数，给定形状可以生成数组
a = np.random.randint(0, 10, 5)
print(a)
# rand 给定形状生成随机数组（0到1之间的数）
b = np.random.rand(2, 3)
print(b)
# choice给定形状产生随机选择
c = np.random.choice(10, 4)
print(c)
# shuffle 与random.shuffle相同，打乱顺序
d = np.array([2, 3, 4, 5, 6])
np.random.shuffle(d)
print(d)
# uniform 给定形状产生随机数小数，概率相同
e = np.random.uniform(2, 3, 5)
print(e)
