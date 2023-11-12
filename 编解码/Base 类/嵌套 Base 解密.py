"""嵌套 Base 解密
author: ElaBosak233
date: 2023/10/19
team: 灵曄兮/Spark1e
"""

from base64 import *


class BaseDecoder:
    def __init__(self, s):
        self.s = s.encode()

    def decode_once(self):
        encodings = ["Base16", "Base32", "Base64", "Base85"]
        cur_encoding = 0
        while True:
            try:
                decoded = b16decode(self.s) if cur_encoding == 0 else \
                    b32decode(self.s) if cur_encoding == 1 else \
                        b64decode(self.s) if cur_encoding == 2 else \
                            b85decode(self.s)
                print(f"{encodings[cur_encoding]}: {decoded.decode()}")
                return decoded
            except Exception:
                cur_encoding += 1
                if cur_encoding == len(encodings):
                    print("--------End--------")
                    return None
                continue

    def decode(self):
        decoded = self.decode_once()
        while decoded is not None and decoded != self.s:
            self.s = decoded
            decoded = self.decode_once()


if __name__ == "__main__":
    with open("base.txt", "r") as f:  # 从 base.txt 中读取信息
        p = f.readlines()
    decoder = BaseDecoder(p[0])  # p[0] 可用任意字符串代替
    decoder.decode()
