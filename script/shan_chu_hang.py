#!/allwegene3/soft/public/python/Python-v3.6.5/bin/python
# -*- coding: UTF-8 -*-
'''
Description：根据 inputlist 文件，删除某些行
Example：python qu_otu.py -i otu_taxon.txt -l list -o otu_taxon2.txt

Created on 2018.8.5
@Author: houfeixiang
'''

import sys
import getopt


def main():
    """根据 inputlist 文件，删除某些行"""
    try:
        opts, args = getopt.getopt(sys.argv[1:], 'hi:l:o:', ['ifile=', 'ilist=',  'ofile='])
    except getopt.GetoptError:
        print("python ***.py -i <inputfile> -l <inputlist> -o <outputfile>")
        sys.exit(2)
    for opt, val in opts:
        if opt == '-h':
            print("python ***.py -i <inputfile> -l <inputlist> -o <outputfile>")
            sys.exit()
        elif opt in ('-i', '--ifile'):
            inputfile = val
        elif opt in ('-l', '--ilist'):
            inputlist = val
        elif opt in ('-o', '--ofile'):
            outputfile = val

    # 主要程序
    data1 = open('{}'.format(inputfile))
    data2 = open('{}'.format(inputlist))
    outfile = open('{}'.format(outputfile), 'w')

    data1_lines = [line.strip() for line in data1.readlines()]
    data2_lines = [line.strip() for line in data2.readlines()]

    # for —— else
    # 不含有break时：for 循环正常执行结束后，else 语句里面的内容也会正常执行
    # 含有break时：当 for 循环被 break 中断后，其后的 else 语句就不执行了
    # 以下代码含义：当 字符串 在这一行，这一行就不写入文件
    for data1_line in data1_lines:
        for data2_line in data2_lines:
            if data2_line in data1_line:
                break
        else:
            outfile.write(data1_line + '\n')

    data1.close()
    data2.close()
    outfile.close()

if __name__ == "__main__":
    main()
