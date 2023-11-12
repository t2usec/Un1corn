"""固定步长点位提取
author: ElaBosak233
date: 2023/11/23
team: 灵曄兮/Sparkle
problem: TZUCTF 2023
"""

from PIL import Image

original_image = Image.open("scene.bmp")  # 原始图片
original_width, original_height = original_image.size

special_image = Image.new("RGB", (original_width, original_height))

# 逐像素复制颜色值，这里从 (15, 15) 开始，每隔 30px 提取一次
for y in range(15, original_height, 30):
    for x in range(15, original_width, 30):
        pixel = original_image.getpixel((x, y))
        # 放大像素，放大为 15x15
        for i in range(15):
            for j in range(15):
                special_image.putpixel((x + i, y + j), pixel)

special_image.save("scene2.bmp")  # 输出图片
