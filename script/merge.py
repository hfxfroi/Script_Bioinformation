#!/allwegene3/soft/public/python/Python-v3.6.5/bin/python
# -*- coding: UTF-8 -*-
'''
Description：根据信息表排序

Created on 2018.8.9
@Author: houfeixiang
'''

import pandas as pd

left = pd.read_csv('left.txt', encoding='gbk', sep='\t')
right = pd.read_csv('right.txt', encoding='gbk', sep='\t')

# 如果输入 CSV 文件，要注意格式：CSV逗号分隔
# left = pd.read_csv('left.csv', encoding='gbk')
# right = pd.read_csv('right.csv', encoding='gbk')

res = pd.merge(left, right, on='key')
res.to_csv('result.txt', index=None, encoding='gbk', sep='\t')
