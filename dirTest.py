import os
from os.path import exists


def file_name(path):
    if(exists(path)):
        for root, dirs, files in os.walk(path):
            """
            print(root) #当前目录路径
            print(dirs) #当前路径下所有子目录
            print(files) #当前路径下所有非目录子文件
            """
            return files
    else:
        raise FileNotFoundError("Wrong file")