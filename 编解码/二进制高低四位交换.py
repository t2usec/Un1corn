"""二进制高低四位交换
author: ElaBosak233
date: 2023/11/12
team: 灵曄兮/Sparkle
problem: ZJCTF 2023 初赛
"""


def swap_nibble(b):
    return ((b & 0x0F) << 4) | ((b & 0xF0) >> 4)


i = "yuanshen"  # 原文件名
o = "yuanshen.jpg"  # 输出文件名

with open(i, "rb") as i_file:
    i_data = i.read()

with open(o, "wb") as o_file:
    o_file.write(bytes(swap_nibble(b) for b in i_data))
