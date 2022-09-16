from matplotlib import pyplot as plt
import matplotlib
# 条形图适用于显示一些离散的数据
# 设置支持中文
font = {
    'family': "SimHei",
    'weight': 'bold',
    'size': 12
}

matplotlib.rc('font', **font)

a = ["猩球崛起3:\n终极值战", "敦刻尔克", "蜘蛛侠:\n英雄归来", "战狼2"]
b_16 = [15746, 312, 4497, 319]
b_15 = [12357, 156, 2045, 168]
b_14 = [2358, 399, 2358, 362]

x_14 = range(len(a))
bar_width = 0.2
x_15 = [i + bar_width for i in x_14]
x_16 = [i + bar_width for i in x_15]
# 设置图形大小
plt.figure(figsize=(12, 8), dpi=80)
plt.bar(x_14, b_14, width=bar_width, label='14号')
plt.bar(x_15, b_15, width=bar_width, label='15号')
plt.bar(x_16, b_16, width=bar_width, label='16号')
xt = ["{}".format(i) for i in a]
plt.xticks(x_15, xt)
# 设置x,y轴名称
plt.xlabel("电影")
plt.ylabel("票房")
plt.legend()
plt.show()
