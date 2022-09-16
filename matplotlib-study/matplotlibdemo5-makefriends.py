from matplotlib import  pyplot as plt
import matplotlib
import  random

x = range(11,31)
y = [random.randint(0,30) for i in x]

#设置matplotlib支持中文
font = {'family': 'SimHei',
              'weight': 'bold',
              'size': 14}
matplotlib.rc('font',**font)

plt.plot(x,y)
xt=["{}岁".format(i) for i in x]
plt.xticks(x[::2], xt[::2])
#绘制网格,可以不传递参数，也可以传递一个alpha参数来修改透明度，它的值是从0-1之间
plt.grid(alpha=0.4)
plt.xlabel("年龄")
plt.ylabel("交女性朋友的个数")
plt.title("11岁到30岁这个年龄阶段每年新交女性朋友图")

plt.show()
