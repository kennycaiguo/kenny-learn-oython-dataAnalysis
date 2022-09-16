import numpy as np
import matplotlib
from matplotlib import pyplot as plt


# 数据来源： https://www.kaggle.com/datasnaek/youtube/data

def replace_nan(ndarr):  # 自己封装的方法，可以替换任意数组中的nan
    # 处理nan，将其替换为这一列所有非nan是数值的均值
    for i in range(ndarr.shape[1]):
        tmp_col = ndarr[:, i]
        nan_count = np.count_nonzero(tmp_col != tmp_col)
        if nan_count != 0:  # 说明这一列有nan
            # 将这一列的非nan取出来计算平均值
            tmp_non_nan_col = tmp_col[tmp_col == tmp_col]
            avg = tmp_non_nan_col.mean()
            tmp_col[tmp_col != tmp_col] = avg
    return ndarr


if __name__ == '__main__':
    #  加载数据
    # 1st method,这个方法比较好查错
    # t_uk = np.loadtxt("./uk_videos.csv", dtype=int, delimiter=',', skiprows=1)
    t_uk = np.loadtxt("./gb_videos.csv", dtype=int, delimiter=',', skiprows=1)
    # t_uk = np.genfromtxt("./uk_videos.csv", dtype=int, delimiter=",",skip_header=1)
    # 使用散点图显示uk数据这like和comments的关系
    # t_uk = replace_nan(t_uk)
    # np.savetxt("uk_data.csv", t_uk, delimiter=",", fmt="%s")
    # 将那些非常稀疏的数据筛选掉
    t_uk = t_uk[t_uk[:, 1] <= 500000]
    # 获取评论数
    uk_comment = t_uk[:, -1]
    # 获取喜欢数
    uk_like = t_uk[:, 1]

    # 设置图表大小
    plt.figure(figsize=(15, 8), dpi=80)
    plt.scatter(uk_like, uk_comment)
    plt.show()
