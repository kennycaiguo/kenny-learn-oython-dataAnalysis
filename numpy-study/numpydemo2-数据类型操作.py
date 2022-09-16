import numpy as np
import random as rnd

# numpy数据类型操作
# 指定创建数组的数据类型
a = np.array([1, 0, 1, 0], dtype='bool')  # 可以指定元素的数据类型
print(a)  # [ True False  True False]
# 修改元素的数据类型
a = a.astype(np.int8)
print(a)
print(a.dtype)

# 随机生成一个浮点型的ndarray,每一个数都是0-1之间的小数
b = np.array([rnd.random() for i in range(10)])
print(b)
# 保留2位小数
b2 = np.round(b, 2)
print(b2)

# 查看数组的形状
print(np.shape(b2))

c = np.array([[rnd.random() for j in range(10)], [rnd.random() for k in range(10)]])
print(c, c.shape)
print("===========================================")
d = c.reshape(5, 4)
print(d, d.shape)
print("============================================")
e = d.reshape(2, 2, 5)
print(e, e.shape)
print("++++++++++++++++++++++++++++++++++++++++++++++")
# 把多维数组变为一维要这样子写
# f = e.reshape((20,))  # 注意  e.reshape((20,1))和e.reshape((1,20)) 返回的都是多维数组
f = e.reshape((e.shape[0]*e.shape[1]*e.shape[2],))  # 注意每一个数都不能为0
print(f, f.shape)
# 也可以使用np.flatten()将多维数组变为一维数组
g = e.flatten()
print(g, g.shape)

arr = np.array([1, 2, 3])
arr2 = arr + 2  # 一个array + 2，它表示的是这个array的每一个元素都+2,减，乘，除都是一样的原理
print(arr2)  # [3,4,5]
print(arr2/2)   # [1.5 2.  2.5]

arr3 = arr + arr2  # 两个ndarray相加，指定是这两个ndarray对于位置的元素相加返回另外一个ndarray
print(arr3)  # [4 6 8]

arr4 = arr * arr2  # =[arr[1]*arr2[1],arr[2]*arr2[2],arr[3]*arr2[3]]
print(arr4)  # [ 3  8 15]

# print(arr/0)  # 一个数组除于0，每一个非0元素得到但是inf就是无穷大，0除于0 得到的是nan

sz1 = np.array([[1,2,3],[4,5,6],[7,8,9],[10,11,12]])
# sz2 = np.arange(3)
# print(sz1,sz2)
# sz3 = sz1 - sz2
# print(sz3)

sz2 = np.arange(4).reshape(4,1)
# sz2 = np.arange(8).reshape(4,2) # 报错
sz3 = sz1-sz2
# print(sz3)

# sz4 = np.array([[1,2,3],[4,5,6]])
# sz5 = sz1 - sz4 # 报错
# print(sz5)
print("------------------------------------------")
arr = np.arange(24).reshape(4, 6)
arr2 = arr
arr3 = arr
print(arr)

# 查看arr中哪些数字小于10
print(arr < 10)  # arr<10就是说要将arr中的每一个元素和10比较返回的是布尔值
# 将arr中所有小于10的数字替换为100
# arr[arr < 10] = 100 # 切片里面可以放一个提交
# print(arr)

# numpy中只需要一步操作就可以吧arr2中所有小于10的数字变为3，把大于10的数字变为10，使用where方法，类似cpp的三目运算符
newArr = np.where(arr < 10, 3, 10)  # 该方法中，第一个参数是一个返回布尔值的表达式，第二个参数是提交成立的值，第三个是条件不成立的值
print(newArr)

# 把arr3中使用小于10的数字变为10，大于20的数字变为20，需要使用numpy的clip方法
resArr = arr3.clip(10, 20)
print(resArr)


t1 = np.arange(12).reshape(2, 6)
t2 = np.arange(12,24).reshape(2, 6)
print(t1)
print(t2)
print("*" * 100)
# 两个数组水平拼接使用numpy的hstack()方法
t_h = np.hstack((t1, t2))  # 返回的结果是一个2行12列的数组
print(t_h)
print("*" * 100)
t_v = np.vstack((t1, t2))  # 返回一个4行6列的数组
print(t_v)


