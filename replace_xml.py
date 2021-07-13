import os
import io
#paths文件目录，files保存文件路径以及名字
paths='/home/fu/PycharmProjects/nanodet_cigar/train_data/val/ann/'
files=[]
oldStr='/home/fu/label_img/images/traffic_ligth/yellow/'
newStr='/home/fu/PycharmProjects/nanodet_cigar/train_data/val/img/'
for file in os.listdir(paths):
    if file.endswith('.xml'):
        files.append(paths+file)
for file in files:
    with open(file, "r", encoding="utf-8") as f:
        lines = f.readlines()  # 将文件内容保存到内存
    with open(file, "w", encoding="utf-8") as f_w:
        for line in lines:  # 将内存中的文件逐行读取
            if oldStr in line:
                line = line.replace(oldStr, newStr)    # 新内容代替旧内容
            f_w.write(line)
# ————————————————
# 版权声明：本文为CSDN博主「小布米」的原创文章，遵循CC 4.0 BY-SA版权协议，转载请附上原文出处链接及本声明。
# 原文链接：https://blog.csdn.net/xiaobumi123/article/details/112252781
