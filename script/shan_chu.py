#!/allwegene3/soft/public/python/Python-v3.6.5/bin/python
# -*-coding: UTF-8 -*-
'''
Description：字符替换

Created on 2018.8.6
@Author: houfeixiang
'''

with open('trans_mapping_L6.txt') as data:
    data_lines = data.readlines()

with open('out.txt', 'w') as data2:
    for data_line in data_lines:
        data_line = data_line.strip()
        data2.write(data_line.replace('|unidentified', '').replace('|Other', '') + '\n')
        # data2.write(data_line.replace('|unidentified', '') + '\n')
