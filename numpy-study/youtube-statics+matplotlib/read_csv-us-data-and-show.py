import numpy as np
import matplotlib
from matplotlib import pyplot as plt
# 数据来源： https://www.kaggle.com/datasnaek/youtube/data

#  加载数据
# 1st method,这个方法比较好查错
t_us = np.loadtxt("./us_videos.csv", dtype=int, delimiter=',', skiprows=1)


# 获取评论数
us_comment = t_us[:, -1]
# 因为绝大多数的数据都集中在5000以前的区域(超过90%)，所以我们只需要筛选5000以前的数据
us_comment = us_comment[us_comment <= 5000]
d = 250
bin_count = (us_comment.max()-us_comment.min())//d
plt.figure(figsize=(15, 8), dpi=80)
# xt = [i for i in range(us_comment.min(), us_comment.max())]
plt.hist(us_comment, bin_count)
plt.show()


