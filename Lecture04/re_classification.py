#!/usr/bin/env python3
# -*- coding:utf-8 -*-

'''
按类别重新存放文件
'''

__author__ = 'Zha Yongchun'
__email__ = 'yooongchun@foxmail.com'

import sys
import os
import shutil
from datetime import datetime as dt


class ReClassifyFiles(object):
    def __init__(self, target_dir, source_dir):
        self.__target = target_dir
        self.__source = source_dir

    def __load_files(self):
        file_path = {}  # 保存结果的字典，以路径为key
        if not os.path.isdir(self.__source):  # 判断参数合法性
            return file_path

        # 迭代遍历获取文件及其路径
        for root, _, files in os.walk(self.__source):
            for file in files:
                path = os.path.join(root, file)
                if os.path.isfile(path):
                    file_path[path] = {
                        'file': file, 'root': root}
        return file_path

    def re_classify(self):
        # 如果目标文件夹不存在则创建
        if not os.path.isdir(self.__target):
            os.mkdir(self.__target)
        # 加载文件
        files = self.__load_files()
        cnt = 1  # 计数
        total = len(files)  # 总文件数
        print(f'一共有{total}个文件需要处理')

        # 遍历所有文件处理
        start = dt.now()
        for file_path, val in files.items():
            file_name = val['file']
            file_type = os.path.splitext(file_name)[1]
            if file_type == '':  # 如果文件没有后缀则设为notype
                file_type = "notype"
            # 拼接路径
            target_type_dir = os.path.join(self.__target, file_type)
            # 目标文件夹不存在则创建
            if not os.path.isdir(target_type_dir):
                os.mkdir(target_type_dir)
            target_path = os.path.join(target_type_dir, file_name)
            # 拷贝文件
            shutil.copy(file_path, target_path)
            print(f'{cnt}/{total}\t复制文件：{file_name}到目标文件夹：{target_type_dir}')
            cnt += 1
        end = dt.now()
        print(f"一共复制{total}个文件，用时：{(end-start).total_seconds()}秒")


if __name__ == "__main__":
    source = r"E:\Files\Project\MathematicsModelingCourse"
    target = "target"
    reclassifier = ReClassifyFiles(target, source)
    reclassifier.re_classify()
