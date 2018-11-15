import numpy as np
import pandas as pd
from matplotlib import pyplot as plt


def title(text):
    print("{} {} {}".format("*" * 30, text, "*" * 30))

df = pd.read_csv("IMDB-Movie-Data.csv")

title("取电影类别数据，并对Genre类别字段的值以,为分隔构建数组")
genre_data = df["Genre"].str.split(",")
print(genre_data.head(5))

title("取所有电影类别")
genre_list = list()
for genre in genre_data:
    genre_list.extend(genre)
genre_series = pd.Series(genre_list).unique()
print(genre_series)

title("以电影为行，以类别为列，构建DataFrame")
matrix = np.zeros((len(genre_data), len(genre_series)), int)
matrix = pd.DataFrame(matrix, columns=genre_series)
print(matrix.head(5))

title("给矩阵赋值")
# 遍历电影类别
for index in range(len(genre_data)):
    genre = genre_data[index]
    # loc方法可以传入列名数组，选出所有列
    matrix.loc[index, genre] = 1
print(matrix.head(5))

title("统计电影各类别出现次数")
genre_count = matrix.sum(axis=0)
print(genre_count)

# 绘制条形图
plt.figure(figsize=(20, 8), dpi=80)

_x = genre_count.index
_y = genre_count.values
plt.bar(_x, _y)

plt.show()
