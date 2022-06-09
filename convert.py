import os

# 第一个版本，将所有文件写入到一个文件中去
path = "dd"
files = os.listdir(path)
files.sort()
# 全文件
print(files)

data = []


# 读取所有文件
for file in files:
    file_name = path + "/" + file
    if os.path.isfile(file_name):
        f = open(file_name)
        content = f.read()

        content += "\n"     # 手动添加一个换行
        f.close()
        data.append(content)

# 预览打印
print(data)

# 写入文件
with open('aa.md', 'w') as target:
    for item in data:
        target.write(item)
