# coding: UTF-8
import chardet
import os
import linecache
import random

def testfile():
    filename = "wechat/meng-chinese.txt"

    fd = open(filename, 'r')
    count = len(fd.readlines())

    ra = random.randint(0, count)

    while True:
        ra = random.randint(0, count)
        content = linecache.getline(filename, ra)
        if content.strip():
            if content[0] != "=":
                break

    fd.close()

    return content
