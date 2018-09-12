#!/allwegene3/soft/public/python/Python-v3.6.5/bin/python
# -*-coding: UTF-8 -*-
'''
Description：将 *.result.txt 转换为另一种形式，再用R语言画图，以满足售后的各种要求

Create on 2018.9.16
@Author: houfeixiang
'''


def main():
    """转换 *.result.txt 的格式"""

    # 提前定义输出文件的表头选项
    taxa_list = ['Kingdom', 'Phylum', 'Class', 'Order', 'Family', 'Genus', 'Species']

    for num in range(7):

        # 输入文件
        with open('{}.result.txt'.format(num)) as input_data:
            # strip()：默认删除空白符（包括'\n','\r','\t','')，所以在这里，输入文件的第一行的第一个空被删掉了
            lines = [line.strip() for line in input_data.readlines()]

        # 输出文件
        with open('{}.result_new.txt'.format(num), 'w') as output_data:
            # 写入输出文件的表头
            head = '{}\tx\ty\n'.format(taxa_list[num])
            output_data.write(head)

        # 取出输入文件的第一例(菌种分类)，从第二行开始取，因为第一行是样本名字
            taxon_list = [line.split('\t')[0] for line in lines[1:]]

        # 写入每一行(前边已经写入表头，这里将从第二行开始写入)
            for i in range(len(lines[0].split('\t'))):
                for j in range(len(taxon_list)):
                    m = taxon_list[j] + '\t' + lines[0].split('\t')[i] + '\t' + lines[1:][j].split('\t')[1:][i] + '\n'
                    output_data.write(m)

        # len(line[0].split('\t'))：输入文件的第一行的长度，即：样本的个数
        # len(taxon_list)：输入文件的第一列的长度，即：菌种的个数

        # taxon_list[j]：菌种名字，
        # line[0].split('\t')[i]：样本的名字（line的第一行为样本名字）
        # line[1:][j].split('\t')[1:][i]：该样本中对应菌种所占丰度值

if __name__ == "__main__":
    main()
