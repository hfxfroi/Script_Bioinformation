# -*-coding: UTF-8 -*-
'''
Description：统计每个样本(或组)所含有的otu(除去0)

Create on 2018.9.13
@Author: houfeixiang
'''

import sys

otu = sys.argv[1]


def main(otu):
    """统计每个样本(或组)中所含有的otu"""
    with open(otu) as o:
        o = o.readlines()
        oa = [a.strip().split('\t') for a in o][0]  # 取出表头
        sample_num = len(oa)-2  # 样本个数
        print(sample_num)

        ob = [b.strip().split('\t') for b in o][1:]  # (除了表头)取出其它行

        print(oa[1:-1])

        otu_one = []
        otu_all = []

        for i in range(sample_num):
            for ob_line in ob:
                if int(ob_line[i+1]) > 0:
                    otu_one.append(ob_line[0])
            otu_all.append(otu_one)
            otu_one = []

        # 统计每个样本所含otu的个数
        length = []
        for i in range(sample_num):
            length.append(len(otu_all[i]))
        max_num = max(length)  # 查看最长的长度
        print(length)
        print(max_num)

        # 在每个列表后边补全空字符（因为转置的矩阵不能长短不一）
        add_list = ['']
        # add_list = add_list*3
        add_list = add_list*(max_num - len(otu_all[0]))
        # print(add_list)

        for i in range(sample_num):
            add_list = add_list*(max_num - len(otu_all[i]))
            otu_all[i].extend(add_list)
        # print(otu_all)

        # 将列表装置（几种方法）
        # otu_all = map(list, zip(*otu_all))
        # otu_all = list(zip(*otu_all))  # zip(*) 将所有输入的对象行转置为列
        otu_all = [list(row) for row in zip(*otu_all)]

        # 写入表头(样本名)
        with open('otu_number_result.txt', 'w') as r:
            for sample_name in oa[1:-1]:
                r.write(sample_name + '\t')
            r.write('\n')

            for i in otu_all:
                for j in i:
                    r.write(j + '\t')
                r.write('\n')

if __name__ == "__main__":
    main(otu)
