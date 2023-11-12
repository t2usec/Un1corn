"""Base64 隐写
date: 2023/11/12
team: 灵曄兮/Sparkle
"""

table = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"
file = open("flag.txt")  # 原文件
flag = ""
tmp_bin = ""

for line in file.readlines():
    line = line.strip("\n")
    if line[-1] == "=":
        if line[-2] == "=":
            i = table.index(line[-3])
            b = bin(i)[2:]
            b = b.zfill(6)
            print(line)
            print(b)
            print(b[-4:] + '\n')
            tmp_bin += b[-4:]
        else:
            i = table.index(line[-2])
            b = bin(i)[2:]
            b = b.zfill(6)
            print(line)
            print(b)
            print(b[-2:] + '\n')
            tmp_bin += b[-2:]

length = len(tmp_bin) / 8
for i in range(int(length)):
    flag += chr(int(tmp_bin[i * 8:i * 8 + 8], 2))

print(flag)
