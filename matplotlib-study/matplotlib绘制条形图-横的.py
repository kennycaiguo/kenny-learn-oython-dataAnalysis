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

# 资料数据:2017年内地票房的前20的电影
a = ["战狼2", "速度与激情8", "功夫瑜伽", "西游伏妖篇", "变形金刚5:最后的骑士", "摔跤吧!爸爸", "加勒比海盗5:死无对证",
     "金刚:骷髅岛", "极限特工:终极回归", "生化危机6:终章", "乘风破浪", "神偷奶爸3", "智取威虎山", "大闹天竺",
     "金刚狼3:殊死一战", "蜘蛛侠:英雄归来", "悟空传", "银河护卫队2", "情圣", "新木乃伊"]
b = [56.01, 26.94, 17.53, 16.49, 15.45, 12.96, 11.8, 11.61, 11.28, 11.12, 10.49
     ,  10.3, 8.75, 7.55, 7.32, 6.99, 6.88, 6.86, 6.58, 6.23]  # 单位:亿

_x = range(len(a))  # 注意plt.bar方法不能菜单字符串,只能传递它对应的索引,这里获取索引

# 设置图形大小
plt.figure(figsize=(20, 11), dpi=80)
#绘制横着的条形图使用的是barh方法
plt.barh(_x, b, color='deeppink')
# _xt = ["{}亿".format(i) for i in b]
# plt.xticks(_x[::5], _xt[::5])
plt.yticks(_x, a)

# 设置x轴和y轴的标签
plt.xlabel("电影票房")
plt.ylabel("电影名称")
# 设置标题
plt.title("2017年内地票房的前20的电影")
# plt.savefig("./2017年内地票房的前20的电影.png")
plt.grid(alpha=0.4)
plt.show()

