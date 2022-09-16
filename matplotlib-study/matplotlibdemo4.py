from matplotlib import pyplot as plt
import random
#注意，matplotlib默认不支持中文，需要使用rc来设置一下
import matplotlib
#方法一
font = {'family': 'SimHei',
              'weight': 'bold',
              'size': 14}
matplotlib.rc('font',**font) #这里**的作用是把字典的每一个key:value变为key=value的形式依次传递进来
#方法二
# plt.rcParams["font.sans-serif"]=["SimHei"] #设置字体
# plt.rcParams["axes.unicode_minus"]=False #该语句解决图像中的“-”负号的乱码问题
#demo3的改进
#做一个显示10点到12点每分钟温度图表。温度随机生成
fig = plt.figure(figsize=(20,8),dpi=80) #dpi的作用，使图片更加清晰,这个fig是全局的，可以在以后的代码调用它的配置
x = range(0,121) #数据在x轴位置，是一个可迭代对象
#设置随机数种子
random.seed(10)
y = [random.uniform(20,35) for i in range(121)] #数据在y轴，是一个可迭代对象

plt.plot(x, y) #传入x 和 y，通过plot绘制折线图
#设置x轴的刻度
#写法1
# xt = ["10点{}分".format(i) for i in x if i<60]
# xt +=["11点{}分".format(i-60) for i in x if i>60]
#写法2
xt = ["10点{}分".format(i) for i in range(60)] #range是包头不包尾的
xt +=["11点{}分".format(i-60) for i in range(60, 121)] #这样子12点也可以显示
xt[len(xt)-1]="12:00" #把最后一个修改一下因为11:60就是12:00
#plt.xticks(x[::5], xt[::5], rotation=90) #很难看
plt.xticks(list(x)[::5], xt[::5], rotation=45) #比较好

#plt.savefig("./tem-2-hr.png")
#plt.savefig("./tem-2-hr.svg") #保存为svg矢量格式
#设置x轴和y轴的描述信息
plt.xlabel("时间", fontproperties=font)
plt.ylabel("温度(°C)", fontproperties=font)
#设置标题
plt.title("10点到12点每分钟温度变化图",fontproperties=font)
plt.show() #显示图形


