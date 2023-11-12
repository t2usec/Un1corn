"""离散坐标绘图
author: ElaBosak233
date: 2023/11/12
team: 灵曄兮/Sparkle
problem: ZJCTF 2023 决赛

源文件应当类似如下，若不同需要可以更改后续代码
495 314
495 313
495 312

另附类似于 (x,y) 文件的正则表达式匹配代码
pattern = re.match(r"\((-?\d+),(-?\d+)\)", input_string)
x = pattern.group(1)
y = pattern.group(2)
"""

import matplotlib.pyplot as plt

with open("index.dat", "r") as f:  # 原文件
    data = f.readlines()

x = []
y = []

for line in data:
    line = line.strip().split()
    x.append(int(line[0]))
    y.append(int(line[1]))

plt.scatter(x, y, s=1, marker="o", color="blue")
plt.xlabel("X")
plt.ylabel("Y")
plt.savefig("output.png")  # 输出文件
plt.show()
