#!/allwegene3/soft/public/python/Python-v3.6.5/bin/python
# -*-coding: UTF-8 -*-
'''
Description：如果属水平(g)是未注释的，就将科水平(f)的名字加过来
输出结果举例：f__Bacteroidales_S24-7_group; g__Bacteroidales_S24-7_group__unidentified;

Created on 2018.8.8
@Author: houfeixiang
'''
import re


def main():
    '''如果属水平(g)是未注释的，就将科水平(f)的名字加过来'''
    with open('otu_taxon.txt') as data:
        data_lines = data.readlines()
    with open('otu.txt', 'w') as data2:
        for data_line in data_lines:
            data_line = data_line.strip()
            if ('g__unidentified' in data_line) and ('f__unidentified' not in data_line):
                # pattern = r'f(__\w+)'
                regex = re.compile(r'f(__\w+.\w+)')  # compile：根据包含正则表达式的字符串,创建模式对象
                tmp = regex.search(data_line).group(1)  # search：扫描整个字符串并返回第一个成功的匹配
                # a = tmp.group(1)  # group(1)：列出第一个括号匹配的部分
                data2.write(re.sub('g__unidentified', 'g' + tmp + '__unidentified', data_line) + '\n')
            else:
                data2.write(data_line + '\n')

if __name__ == "__main__":
    main()
