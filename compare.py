import sys
import difflib
import os
from config import path


def create_folder(path):
    if not os.path.isdir(path):
        os.makedirs(path)

# 讀取配置文件函數
def read_file(file_name):
    try:
        file_handle = open(file_name, 'r', encoding="utf-8")
        text = file_handle.read().splitlines()  # 讀取後以行進行分割
        file_handle.close()
        return text
    except IOError as error:
        print('Read file Error: {0}'.format(error))
        sys.exit()


# 比較兩個文件並輸出html格式的結果
def compare_file(file1_name, file2_name):
    if file1_name == "" or file2_name == "":
        print('文件路徑不能為空: file1_name的路徑為: {0}, file2_name的路徑為: {1} .'.format(file1_name, file2_name))
        sys.exit()
    text1_lines = read_file(file1_name)
    text2_lines = read_file(file2_name)
    print_list = ['+','-']
    no_print_list = ['!']
    d = difflib.Differ()
    diff_print = [a for a in d.compare(text1_lines, text2_lines) if a[0] in print_list and a[-1] not in no_print_list ]
    if diff_print:
        print('record of compare will be storage in compared.txt and result.html !')
        try:
            with open(path+'compared.txt', 'w', encoding="utf-8") as result_file:
                result_file.write('\n'.join(diff_print))
            print('\n'.join(diff_print))
        except IOError as error:
            print('寫入compare.txt文件時發生錯誤:{0}'.format(error))

    else:
        print(f"It's all same as old file")
    diff = difflib.HtmlDiff()  # 創建htmldiff 對象
    result = diff.make_file(text1_lines, text2_lines)  # 通過make_file 方法輸出 html 格式的對比結果
    #  將結果保存到result.html文件中並打開
    try:
        with open(path+'result.html', 'w', encoding="utf-8") as result_file:      #同 f = open('result.html', 'w') 打開或創建一個result.html文件
            result_file.write(result)                      #同 f.write(result)
    except IOError as error:
        print('寫入html文件錯誤:{0}'.format(error))


if __name__ == '__main__':
    create_folder(path)
    f1 = path+input(f'Enter first filename(older file): ')+'.txt'
    f2 = path+input(f'Enter second filename(newer file): ')+'.txt'
    compare_file(f1, f2)
