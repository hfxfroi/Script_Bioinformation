#!/allwegene3/soft/public/python/Python-v3.6.5/bin/python
# -*-coding: UTF-8 -*-
'''
Description：将 *.result.txt 转换为另一种形式，这里只转换一个文件
Example：python only_one_result_txt.py 1.result.txt

Create on 2018.9.16
@Author: houfeixiang
'''

import sys
data = sys.argv[1]


def main(data):
    """转换一个result.txt的形式"""

    # 需要哪一个种类，就在下边的head处写哪个
    # ['Kingdom', 'Phylum', 'Class', 'Order', 'Family', 'Genus', 'Species']

    # 输入文件
    with open(data) as input_data:
        # strip()：默认删除空白符（包括'\n','\r','\t','')，所以在这里，输入文件的第一行的第一个空被删掉了
        lines = [lines.strip() for lines in input_data.readlines()]

    # 输出文件
    with open('result.txt', 'w') as output_data:
        # 写入输出文件的表头
        head = '{}\tx\ty\n'.format('Phylum')  # 注意根据需要来更换菌种名字
        output_data.write(head)

    # 取出输入文件的第一例(菌种分类)，从第二行开始取，因为第一行是样本名字
        taxon_list = [line.split('\t')[0] for line in lines[1:]]

    # 写入每一行(前边已经写入表头，这里将从第二行开始写入)
        for i in range(len(lines[0].split('\t'))):
            for j in range(len(taxon_list)):
                m = taxon_list[j] + '\t' + lines[0].split('\t')[i] + '\t' + lines[1:][j].split('\t')[1:][i] + '\n'
                output_data.write(m)

if __name__ == "__main__":
    main(data)
