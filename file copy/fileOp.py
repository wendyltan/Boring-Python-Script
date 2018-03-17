#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/3/16 19:24
# @Author  : Wendyltanpcy
# @File    : fileOp.py
# @Software: PyCharm


import os
import os.path
import shutil
import re
from progress.bar import Bar


def dfs_showdir(path, depth):
    '''
    dfs search all directories to print out
    :param path:
    :param depth:
    :return:
    '''
    if depth == 0:
        print("root:[" + path + "]")

    for item in os.listdir(path):
        if '.git' not in item:
            print("|      " * depth + "+--" + item)
            newitem = path +'/'+ item
            if os.path.isdir(newitem):
                dfs_showdir(newitem, depth +1)


def dfs_check_suffix(path,pattern,depth,files_list):
    '''
    using regex pattern to match file suffix to find specific files
    :param path:
    :param pattern:
    :param depth:
    :param files_list:
    :return:
    '''
    for item in os.listdir(path):
        if '.git' not in item:
            match = pattern.match(item)
            if match is not None:
                files_list.append(path+'/'+item)
            newitem = path +'/'+ item
            if os.path.isdir(newitem):
                dfs_check_suffix(newitem, pattern,depth +1,files_list)
    return files_list

def grab_file(path):
    '''
    use suffix patterns to search files and copy them
    :param path:
    :return:
    '''
    file_type = input("Enter suffix of file type(ex: 'txt')\n")

    re_match = ".*\." + file_type+'$'
    pattern = re.compile(re_match)

    files_list = []
    files_list = dfs_check_suffix(path,pattern,0,files_list)

    file_list_len = files_list.__len__()

    if file_list_len!=0:
        for item in files_list:
            print(item)
        print("match " + str(file_list_len) + " files!")
        print('='*10)
        answer = input("Do you want to copy them to current directory?(y/n)\n")
        if answer=="y":
            # make new dir
            path = os.path.curdir+'/fetch'
            if not os.path.exists(path):
                os.mkdir(path)
            os.chdir(path)

            # set fail counter and progress bar
            counter = 0
            bar = Bar('Copying...', max=file_list_len)

            for file_path in files_list:
                try:
                    if file_path.startswith('.'):
                        print("Already under current path,don't have to copy")
                    else:
                        shutil.copy(file_path,os.path.curdir)
                except PermissionError:
                    print("Don't have permission!Pass this file...")
                    counter+=1
                except FileNotFoundError:
                    print("No such file!Pass this file...")
                    counter += 1
                bar.next()
            bar.finish()
            print(str(counter)+" files fail to fetch! "+ str(file_list_len-counter)+" files fetch success!")
        elif answer=="n"or "":
            print("Cancel copy!")
        else:
            print("Answer invalid!")
    else:
        print("Match no file!")


if __name__ == '__main__':
    path = input("Enter path\n")
    # path is empty,default is listing root directory
    if path == "":
        print("showing current root!")
        dfs_showdir('.',0)
        grab_file('.')
    else:
        dfs_showdir(path, 0)
        grab_file(path)
