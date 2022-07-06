# -*- coding:utf-8 -*-
import os

from aligo import Aligo, Auth

auth = Auth() #首次运行打开
ali = Aligo()


def searsh_file_list(ids, n=0):
    n = n + 1
    for file in ali.get_file_list(ids):
        try:
            name = '\t' * n + str(file.name)
            # print(name)
            file_list.write(name + '\n')
        except:
            continue
        if file.type == 'folder':
            searsh_file_list(file.file_id, n)


if __name__ == '__main__':
    print('go')
    idd=input('id:')
    with open('文件树.txt', 'w') as file_list:
        searsh_file_list(idd)
        file_list.close()
    os.system('文件树.txt')
