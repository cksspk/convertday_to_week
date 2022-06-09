from datetime import datetime
import os
import re

# 升级，提取文件名中的日期， 转换成每周。
# 组成格式 {'第1周':['周一','周二'...], '第2周':['周一','周二'...]...}

# 将每日数据，按周归集，重新生成每周文件

path = "dd"
files = os.listdir(path)
files.sort()
# 全文件
print("文件及文件夹总数：", len(files))

file_dict = {}

# 读取文件
def read_file( file_name ):
    f = open(file_name)
    content = f.read()
    f.close()
    content += "\n"  # 手动添加一个换行

    return content


# 读取所有文件, 并构建对象
for file in files:
    # 提取日期
    match = re.search('\d{4}-\d{2}-\d{2}', file)
    if match:
        date_str = match.group()  # 日期字符串 "2022-09-09"
        y = datetime.strptime(date_str, '%Y-%m-%d')  # 转成日期对象

        # 年的第几周
        week = datetime.strftime(y, '周-%Y-第%W周')    # 日期格式化-新的文件名
        # print(file + "： " + week)
        if week not in file_dict:
            # 初始化数组
            file_dict[week] = []
        content = read_file(path + "/" + file)
        file_dict[week].append(content)

print(file_dict.keys())

# 将对象写入到文件中
for key, values in file_dict.items():
    # 按每周生成文件
    file = "week/" + key + ".md"
    with open(file, 'w') as target:
        for item in values:
            target.write(item)
    # print(key)
    # print(values)



