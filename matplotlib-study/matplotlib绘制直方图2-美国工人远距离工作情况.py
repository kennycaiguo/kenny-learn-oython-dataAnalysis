from matplotlib import pyplot as plt
import matplotlib

# 条形图适用于显示一些离散的数据
# 设置支持中文
font = {
    'family': "Arial",
    'weight': 'bold',
    'size': 12
}

matplotlib.rc('font', **font)

interval = [0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 60, 90]
width = [5, 5, 5, 5, 5, 5, 5, 5, 5, 15, 30, 60]
quantity = [836, 2737, 3723, 3926, 3596, 1438, 3273, 642, 824, 613, 215, 47]

# 对不起,以上的数据都不能直接用来绘制直方图,因为直方图需要的是原始数据
# 可以使用条形图的方法,绘制条形图时如果宽度是一个列表,就会有类似直方图的效果
plt.figure(figsize=(20, 8), dpi=80)
# plt.bar(range(len(quantity)), quantity,width=width)  # 为什么会有负数?
# plt.bar(range(len(quantity)), quantity)  # 为什么会有负数?
#  如何将普通条形图变为直方图?条形图的默认宽度是0.8,把它设置为1就会全部粘在一起
plt.bar(range(12), quantity,width=1)
# 设置x轴刻度
_xt = [i - 0.5 for i in range(13)]
_ticks = interval + [150]
plt.xticks(_xt, _ticks)
plt.show()
