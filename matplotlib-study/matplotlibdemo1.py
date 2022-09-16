from matplotlib import pyplot as plt

x = range(2, 26, 2) #数据在x轴位置，是一个可迭代对象，这个range不包括26
y = [15, 13, 14.5, 17, 20, 25, 26, 26, 27, 22, 18, 15] #数据在y轴，是一个可迭代对象
# x轴和y轴一起组成需要绘制的点
# 分别是(2,15),(4,13),(6,14.5)...
plt.plot(x, y) #传入x 和 y，通过plot绘制折线图
plt.show() #显示图形


