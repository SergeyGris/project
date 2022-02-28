
# 1. открыть ямл
# 2. Разделить файл на строки
# 3. Как-то обработать строки, чтобы понять на какому уровне находится файл
# 4. Создать список файлов уровня
# 5. Создать файл из списка

import os

first_level={}
second_level={}
third_level={}
fourth_level={}
space=' '
with open(os.path.join('config_2.yaml'), encoding='utf-8') as file_1:
    for line in file_1:
    #     if '-' not in line:
    #         first_level[line.strip()]=''
        if line.startswith('  - '):
            while
    dir_list=file_1.readlines()
    # first_level=[]


# def function_1(dir_list):
















    # root_path={}
    # dir_list=file_1.read()
    # dir_list_1=dir_list.split(':\n')
    # dir_list_2=[]
    # for dirs in dir_list_1:
    #     if '  - ' not in dirs:
    #         root_path[dirs]=None
    #         continue
    #     _,next_dir=dirs.split('  - ')
    #     dir_list_2.append(next_dir)
    # for first_dir in dir_list_1:
    #     dir_list_2=first_dir.split(':\n    - ')
    #     for second_dir in dir_list_2:
    #         dir_list_3 = second_dir.split(':\n    - ')
    #             print(dir_list_2)




    # root_name='my_project'
    # dir_list=['settings','mainapp','adminapp','authapp']
    # for dirs in dir_list:
    #     dir_path=os.path.join(root_name,dirs)
    #     if not os.path.exists(dir_path):
    #         os.makedirs(dir_path)
    # print(dir_list_1)