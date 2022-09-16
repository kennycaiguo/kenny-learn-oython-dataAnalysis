from matplotlib import pyplot as plt
import matplotlib
import random

a = [1, 0, 1, 1, 2, 4, 3, 2, 3, 4, 4, 5, 6, 5, 4, 3, 3, 1, 1, 1]
b = [1, 0, 3, 1, 2, 2, 3, 3, 2, 1, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1]

x = range(11, 31)
# y = [random.randint(0,30) for i in x]

# 设置matplotlib支持中文
font = {'family': 'SimHei',
        'weight': 'bold',
        'size': 14}
matplotlib.rc('font', **font)
# 需要标明那一条线是谁的，所以需要label参数，此外还需要添加图例，使用legend()方法，否则没有效果
# plot方法还可以传递颜色，线条样式，线宽、透明度等等参数
"""
红色：'r' 白色:'w'
蓝色:'b'  青色:'c'
绿色:'g'  洋红:'m'
黄色:'y'  黑色:'k'
**Line Styles**

        =============    ===============================
        character        description
        =============    ===============================
        ``'-'``          solid line style实线
        ``'--'``         dashed line style虚线
        ``'-.'``         dash-dot line style点划线
        ``':'``          dotted line style点线
        =============    ===============================

"""
plt.plot(x, a, label="本人", color='m', linestyle='-', linewidth=3)
plt.plot(x, b, label="同桌", color='c', linestyle='--')

# 添加图例，如果中文显示不正常这里可以传递一个prop=font参数，还可以传递一个loc参数指定图例的位置
plt.legend(loc='upper left')
# plt.legend(loc='lower center')
xt = ["{}岁".format(i) for i in x]
plt.xticks(x[::2], xt[::2])
# 绘制网格,可以不传递参数，也可以传递一个alpha参数来修改透明度，它的值是从0-1之间
plt.grid(alpha=0.4, linestyle='--')  # 这里也是可以设置linestyle参数的
plt.xlabel("年龄")
plt.ylabel("交女性朋友的个数")
plt.title("11岁到30岁这个年龄阶段每年新交女性朋友图")

plt.show()
