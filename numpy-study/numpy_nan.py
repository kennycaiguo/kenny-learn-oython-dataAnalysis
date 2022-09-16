import numpy as np


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
    t1 = np.arange(24).reshape((4, 6)).astype("float")
    t1[1, 2:] = np.nan
    print(t1)
    print("==================================================")
    t1 = replace_nan(t1)
    print(t1)
