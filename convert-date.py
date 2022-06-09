from datetime import datetime
import os
import re

# 升级，提取文件名中的日期， 转换成每周。
# 组成格式 {'第1周':['周一','周二'...], '第2周':['周一','周二'...]...}

path = "dd"
files = os.listdir(path)
files.sort()
# 全文件
print("文件及文件夹总数：", len(files))

file_dict = {}

# 读取所有文件
for file in files:
    # 提取日期
    match = re.search('\d{4}-\d{2}-\d{2}', file)
    if match:
        date_str = match.group()
        # 转成日期格式
        y = datetime.strptime(date_str, '%Y-%m-%d')
        week_date = y.isocalendar()

        # 年的第几周
        week = datetime.strftime(y, '周-%Y-第%W周')
        # print(file + "： " + week)
        if week not in file_dict:
            # 初始化数组
            file_dict[week] = []
        file_dict[week].append(file)    # 添加 周几 添加到 该周

for key, values in file_dict.items():
    print(key)
    print(values)
