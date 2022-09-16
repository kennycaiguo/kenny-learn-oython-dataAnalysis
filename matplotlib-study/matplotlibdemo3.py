from matplotlib import pyplot as plt
import random

#做一个显示10点到12点每分钟温度图表。温度随机生成
fig = plt.figure(figsize=(20,8),dpi=80) #dpi的作用，使图片更加清晰,这个fig是全局的，可以在以后的代码调用它的配置
x = range(0,120) #数据在x轴位置，是一个可迭代对象，
y = [random.randint(20,35) for i in range(120)] #数据在y轴，是一个可迭代对象

plt.plot(x, y) #传入x 和 y，通过plot绘制折线图
#设置x轴的刻度
plt.xticks(x[::5])
plt.yticks(range(min(y), max(y)+1))
#plt.savefig("./tem-2-hr.png")
#plt.savefig("./tem-2-hr.svg") #保存为svg矢量格式
plt.show() #显示图形


