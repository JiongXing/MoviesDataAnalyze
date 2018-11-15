# MoviesDataAnalyze
Python练习之 Numpy & Pandas 基础用法

一个小例子，对一份电影数据文件作简单分析，并统计电影类别的出现次数

1. 读入这份[电影数据集](https://github.com/JiongXing/MoviesDataAnalyze/blob/master/IMDB-Movie-Data.csv)：
```python
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt

df = pd.read_csv("IMDB-Movie-Data.csv")
```

2. 取电影类别数据，并对Genre类别字段的值以,为分隔构建数组：
```python
genre_data = df["Genre"].str.split(",")
print(genre_data.head(5))
```
打印：
```
0     [Action, Adventure, Sci-Fi]
1    [Adventure, Mystery, Sci-Fi]
2              [Horror, Thriller]
3     [Animation, Comedy, Family]
4    [Action, Adventure, Fantasy]
Name: Genre, dtype: object
```

3. 取所有电影类别：
```python
genre_list = list()
for genre in genre_data:
    genre_list.extend(genre)
genre_series = pd.Series(genre_list).unique()
print(genre_series)
```

打印：
```
['Action' 'Adventure' 'Sci-Fi' 'Mystery' 'Horror' 'Thriller' 'Animation'
 'Comedy' 'Family' 'Fantasy' 'Drama' 'Music' 'Biography' 'Romance'
 'History' 'Crime' 'Western' 'War' 'Musical' 'Sport']
```

4. 以电影为行，以类别为列，构建以0填充的DataFrame：
```python
matrix = np.zeros((len(genre_data), len(genre_series)), int)
matrix = pd.DataFrame(matrix, columns=genre_series)
print(matrix.head(5))
```

打印：
```
0       0          0       0        0  ...          0    0        0      0
1       0          0       0        0  ...          0    0        0      0
2       0          0       0        0  ...          0    0        0      0
3       0          0       0        0  ...          0    0        0      0
4       0          0       0        0  ...          0    0        0      0

[5 rows x 20 columns]
```

5. 给矩阵赋值
```python
for index in range(len(genre_data)):
    genre = genre_data[index]
    # loc方法可以传入列名数组，选出所有列
    matrix.loc[index, genre] = 1
print(matrix.head(5))
```

打印：
```
   Action  Adventure  Sci-Fi  Mystery  ...    Western  War  Musical  Sport
0       1          1       1        0  ...          0    0        0      0
1       0          1       1        1  ...          0    0        0      0
2       0          0       0        0  ...          0    0        0      0
3       0          0       0        0  ...          0    0        0      0
4       1          1       0        0  ...          0    0        0      0

[5 rows x 20 columns]
```

6. 统计电影各类别出现次数
```python
genre_count = matrix.sum(axis=0)
print(genre_count)
```

打印：
```
Action       303
Adventure    259
Sci-Fi       120
Mystery      106
Horror       119
Thriller     195
Animation     49
Comedy       279
Family        51
Fantasy      101
Drama        513
Music         16
Biography     81
Romance      141
History       29
Crime        150
Western        7
War           13
Musical        5
Sport         18
dtype: int64
```

7. 绘制条形图
```python
plt.figure(figsize=(20, 8), dpi=80)

_x = genre_count.index
_y = genre_count.values
plt.bar(_x, _y)

plt.show()
```

![电影类别频数统计](https://upload-images.jianshu.io/upload_images/2419179-ef996f139fdd8b21.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
