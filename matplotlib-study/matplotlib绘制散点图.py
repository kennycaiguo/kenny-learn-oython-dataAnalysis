from matplotlib import pyplot as plt
import matplotlib
# 展示北京2016年3,10月份气温随时间变化的规律
a = [11,17,16,11,12,11,12,6,6,7,8,9,12,15,14,17,18,21,16,17,20,14,15,15,15,19,21,22,22,22,23]  # march
b = [26,26,28,19,21,17,16,19,18,20,20,19,22,23,17,20,21,20,22,15,11,15,5,13,17,10,11,13,12,13,6]  # october

# 设置matplotlib支持中文
font = {'family': 'SimHei',
        'weight': 'bold',
        'size': 14}
matplotlib.rc('font', **font)

x_3 = range(1, 32)  # 注意range是包头不包尾的
x_10 = range(51, 82)  # 为了避免图形重合，10月份的x轴需要右移，这个跟柱形图不一样
# 设置图形大小
plt.figure(figsize=(20, 8), dpi=80)
# 绘制散点图需要添加图例，设置label和调用legend方法
plt.scatter(x_3, a, label="3月份")
plt.scatter(x_10, b, label="10月份")
plt.legend(loc='upper left')
# 调整x轴和y轴的刻度
_x = list(x_3)+list(x_10)
_xt_label = ["3月{}日".format(i) for i in x_3] +["10月{}日".format(i-50) for i in x_10]
plt.xticks(_x[::3], _xt_label[::3], rotation=45)
# 添加描述信息
plt.xlabel("月份")
plt.ylabel("温度°C")
plt.title("北京2016年3,10月份气温随时间变化的规律")
plt.show()
