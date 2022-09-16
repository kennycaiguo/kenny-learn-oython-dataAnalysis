import numpy as np

# 数据来源： https://www.kaggle.com/datasnaek/youtube/data

#  加载数据
# 1st method,这个方法比较好查错
data = np.loadtxt("./gb_videos.csv", dtype=int, delimiter=',', skiprows=1)
data2 = np.loadtxt("./us_videos.csv", dtype=int, delimiter=',', skiprows=1)
# 2nd method，这个方法比较难查错
# data = np.genfromtxt("./gb_videos.csv", dtype=int, delimiter=',', skip_header=1)
# data2 = np.genfromtxt("./us_videos.csv", dtype=int, delimiter=',', skip_header=1)
# print("Great Briten:\n", data[:5])
# print("USA:\n", data2[:5])

# print("Great Briten:\n", data)
# print("USA:\n", data2)

# 添加国家数据
# 构造全为0的数据
us_code = np.zeros((data2.shape[0], 1)).astype("int")
# 构造全为1的数据
uk_code = np.ones((data.shape[0], 1)).astype("int")

# 为国家数据添加一个国家代号，us是0，uk是1
us_data = np.hstack((data2, us_code,))
uk_data = np.hstack((data, uk_code))

# print(us_data)
# print("#" * 100)
# print(uk_data)

# 数据垂直拼接
all_data = np.vstack((us_data, uk_data))
print(all_data)


