from matplotlib import pyplot as plt
#对的一个demo进行适当改进，使别人更容易看懂
#改进1，设置图片大小
fig = plt.figure(figsize=(20,8),dpi=80) #dpi的作用，使图片更加清晰,这个fig是全局的，可以在以后的代码调用它的配置
x = range(2, 26, 2) #数据在x轴位置，是一个可迭代对象，这个range不包括26
y = [15, 13, 14.5, 17, 20, 25, 26, 26, 27, 22, 18, 15] #数据在y轴，是一个可迭代对象
# x轴和y轴一起组成需要绘制的点
# 分别是(2,15),(4,13),(6,14.5)...
plt.plot(x, y) #传入x 和 y，通过plot绘制折线图
#设置x轴的刻度
#plt.xticks(x) #根据x这个range的每一个值来绘制刻度
#把刻度设置得再密集一些
plt.xticks(range(2, 25))
#修改y轴的刻度
# _y = range(1,28)
# plt.yticks(_y[::1])
#plt.yticks(range(1, 28))
plt.yticks(range(min(y), max(y)+5))
#plt.savefig("./tem-2-hr.png")
#plt.savefig("./tem-2-hr.svg") #保存为svg矢量格式
plt.show() #显示图形


