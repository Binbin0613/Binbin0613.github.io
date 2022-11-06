# -*- coding = utf-8 -*-
# @Time  : 2022/11/6 21:59
# @Author: Bin
# @File  : fileReNameOrder.py
# @Software :PyCharm
# java是世界上最好的语言！

# -*- coding:utf8 -*-

import os
import re
import shutil
from pathlib2 import Path


# 批量命名图片
def renamePic(srcImgDir):
    i = 18
    for item in srcImgDir.rglob("*.jpg"):
        # 获取图片名
        imgName = item.name
        newName = str(i) + ".jpg"
        i = i + 1
        # 重命名
        print(f"prepare to rename {imgName}")
        item.rename(newName)


if __name__ == '__main__':
    # 文件路径--跟代码同目录
    srcImgPath = Path("./")
    renamePic(srcImgPath)