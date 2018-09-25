# -*-coding: UTF-8 -*-
'''
Description：按组分析时，将fa文件cat到一起
Example：python cat_fa.py map.txt(自己写一个map文件)

Create on 2018.9.25
@Author: houfeixiang
'''

import sys
import os

map = sys.argv[1]


def main(map):
    """按组分析时，将fa文件cat到一起"""

    with open(map) as m:
        m = [line.strip().split('\t') for line in m.readlines()]
        print(m)

    # 将组名存到列表中
        zu_name = []
        for lines in m:
            zu_name.append(lines[1])
        print(zu_name)

        zu_name = list(set(zu_name))  # 去除重复的组名，并转换为列表
        print(zu_name)

    # 根据组名，将样本cat到一起
        os.system('mkdir project_zu')
        for i in zu_name:
            for j in m:
                if j[1] == i:
                    os.system('cat {}.fa >> project_zu/{}.fa'.format(j[0], i))
                else:
                    pass

if __name__ == "__main__":
    main(map)
