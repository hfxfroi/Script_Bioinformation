#!/allwegene3/soft/public/python/Python-v3.6.5/bin/python
# -*- coding: UTF-8 -*-
'''
Description：根据 inputlist 文件, 复制需要的数据
Example：python cp_data.py -l list -p /allwegene3/work/***/0rawdata/

Created on 2018.8.3
@Author: houfeixiang
'''

import sys
import getopt
import os


def main():
    """根据 inputfile 文件, 复制需要的数据"""
    try:
        opts, args = getopt.getopt(sys.argv[1:], 'hl:p:', ['ilist=', 'pwd='])
    except getopt.GetoptError:
        print("python ***.py -l <inputlist> -p <lu_jing>")
        sys.exit(2)
    # inputfile = ""
    # lu_jing = ""
    for opt, val in opts:
        if opt == '-h':
            print("python ***.py -l <inputlist> -p <lu_jing>")
            sys.exit()
        elif opt in ('-l', '--ilist'):
            inputlist = val
        elif opt in ('-p', '--pwd'):
            lu_jing = val

    # 主要程序
    data = open('{}'.format(inputlist))
    data_lines = [line.strip() for line in data.readlines()]
    for data_line in data_lines:
        os.system('cp {}/{}* .'.format(lu_jing, data_line))
    data.close()

if __name__ == "__main__":
    main()
