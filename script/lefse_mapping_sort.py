# -*-coding: UTF-8 -*-
'''
Description：对mapping进行排序
Example：python lefse_mapping_sort.py mapping.txt

Created on 2018.9.12
'''

import sys

m = sys.argv[1]


def lefse_map_sort(m):
    """根据组名的个数，从大到小对mapping进行排序"""
    with open(m) as m:
        m = m.readlines()
        ma = [a.strip().split('\t') for a in m][1:]  # （除了表头）取出其它行
        mb = [b.strip().split('\t')[1] for b in m][1:]  # 取出其它行的第二列（组名）
        # print(ma)
        # print(mb)  # ['A', 'B', 'B', 'C', 'C', 'C', 'D', 'D', 'D', 'D', 'E', 'E', 'E', 'E', 'F', 'F']

    c = list(set(mb))  # 将组名去除重复，并转换为列表形式：['B', 'C', 'A', 'D', 'F', 'E']

    # 对组名出现的次数进行：计数！！！！！
    group_num = dict()  # dict() 函数用于创建一个字典
    for i in c:
        num = 1
        for j in ma:
            if i == j[1]:
                num += 1
        group_num[i] = num  # 统计每个组名出现的次数

    # print(group_num)  # {'B': 3, 'C': 4, 'A': 2, 'D': 5, 'F': 3, 'E': 5}

    d = sorted(group_num.items(), key=lambda x: x[1], reverse=True)  # 对字典进行排序
    # print(d)  # [('D', 5), ('E', 5), ('C', 4), ('B', 3), ('F', 3), ('A', 2)]

    with open('new_mapping2', 'w') as new_map:
        new_map.write('#SampleID Description\n')
        for i in d:
            for j in ma:
                if i[0] == j[1]:
                    new_map.write('\t'.join(j) + '\n')

lefse_map_sort(m)
