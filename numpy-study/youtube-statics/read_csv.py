import numpy as np
# 数据来源： https://www.kaggle.com/datasnaek/youtube/data
# data = np.loadtxt("./videos.csv", delimiter=',', dtype=str, skiprows=1,usecols=(0,1,2))
# print(data)
# 1st method
data = np.loadtxt("./gb-videos.csv", dtype=str, delimiter=',', skiprows=1)
data2 = np.loadtxt("./us-videos.csv", dtype=str, delimiter=',', skiprows=1)
# 2nd method
# data = np.genfromtxt("./gb-videos.csv", dtype=str, delimiter=',', skip_header=1)
# data2 = np.genfromtxt("./us-videos.csv", dtype=str, delimiter=',', skip_header=1)
# print("Great Briten:\n", data[:5])
# print("USA:\n", data2[:5])

# print("Great Briten:\n", data[:, :4])
# print("USA:\n", data2[:, :4])


# # numpy中的转置方法1，transpose()
# data_t = data.transpose()
# print(data_t)
#
# # numpy中的转置方法2.
# data2_t = data2.swapaxes(1, 0)
# print(data2_t)
#
# #  numpy中的转置方法3.使用内置属性T表示转置
# print(data_t.T)

# numpy的ndarray的获取行和列的操作
# 获取一行
# print(data[2])  # 取第三行
# 取连续多行
# print(data[2:6])  # 获取地3，4，5，6行，不包括第7行
# 取不连续多行
# print(data[[2, 4, 6, 8]])  # 注意，这里需要两层方括号否则报错
# print(data[100:])   # 表示获取从100行到末尾的所有行
# 获取一列
# print(data[:, 2])  # 获取第三列
# 取连续多列
# print(data[:, 0:3])  # 获取第1，2，3列，不包括第四列
# print(data[:, 2:])  # 获取从第3列开始的所有列

# 获取不连续多列
# print(data[:, [0, 2, 3, 4]])  # 获取第1，第2，第4，第5列

# 同时取多行多列(规则，逗号前面的表示行，逗号后面的表示列)
# print(data[2, 3])  # 获取第3行第4列
# print(data[2:10, 1:3])  # 获取第3到第10行 ，每一行取第2，第3列

# 获取多个不相邻的点
# print(data[[0, 2], [0, 1]])  # 表示获取（0，0）位置的值，和（2，1）位置的值
print(data[[0, 2, 2], [0, 1, 3]])  # 表示获取（0，0）位置的值，（2，1）和(2,3)位置的值
