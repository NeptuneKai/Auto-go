import os


def searsh_file_list(file, n=0):
    n = n + 1
    if os.listdir(file) != 0:
        for i in os.listdir(file):
            try:
                name = '\t' * n + str(i)
                print(name)
                file_list.write(name + '\n')
            except:
                continue
            try:
                searsh_file_list(file + '/' + str(i), n)
            except:
                pass

if __name__ == '__main__':
    with open('文件树.txt', 'w') as file_list:
        searsh_file_list('path') # 需要生产文件树的目录
        file_list.close()
    os.system('文件树.txt')
