import numpy as np

# numpy创建数组的3种方法
a = np.array([1, 2, 3, 4, 5])
b = np.array(range(1, 6))
c = np.arange(1, 6)

print(type(a), type(b), type(c))  # 都是<class 'numpy.ndarray'> numpy.array 和arange方法创建的是ndarray
print(a.dtype)  # 这个列表的元素的数据类型:int32
print(c.dtype)  # 这个列表的元素的数据类型:int32
