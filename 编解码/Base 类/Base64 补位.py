"""Base64 补位
author: Haibara
date: 2023/11/12
team: 灵曄兮/Sparkle
"""

import base64

b64chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"

with open("input.txt", "rb") as f:
    bin_str = ""
    for line in f.readlines():
        steg_b64 = "".join(line.decode().split())  # 解码字节数据并去除空格
        row_b64 = "".join(base64.b64encode(base64.b64decode(steg_b64)).decode().split())  # 把内容编码成原生base64

        offset = abs(b64chars.index(steg_b64.replace("=", "")[-1]) - b64chars.index(
            row_b64.replace("=", "")[-1]))  # 文本的base64 - 原生base64
        equal_num = steg_b64.count('=')  # 没有等号则没有偏移量
        if equal_num:
            bin_str += bin(offset)[2:].zfill(equal_num * 2)

    print("".join([chr(int(bin_str[i:i + 8], 2)) for i in range(0, len(bin_str), 8)]))
