import numpy as np

filePath = "city-aic.csv"
# data = np.loadtxt(filePath, dtype=str, delimiter=',', skiprows=1)
# print(data[:5])

# 可以修改列的显示顺序，第一种加载方式，也可以不用跳过表头，这个方法一定要指定数据类型否则报错
# data = np.loadtxt(filePath, dtype=str, delimiter=',', usecols=(2,0,1,3))
# print(data[:5])

# 另外一种加载方式，可以不用跳过表头，当然也可以跳过，建议跳过，这个可以不用指定数据类型，此时只能正确加载数字，字符串显示nan，不过建议指定数据类型
data = np.genfromtxt(filePath, dtype=str, delimiter=',', skip_header=1)
print(data[:5])

# 此外，numpy还可以保存csv文件
a = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
np.savetxt("nums.csv", a, fmt="%s", delimiter=",")

# 加载保存的数据
nums = np.genfromtxt("nums.csv", dtype=np.int8, delimiter=",")
print(nums)
