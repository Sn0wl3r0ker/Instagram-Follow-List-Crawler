from config import path

def sorted_to_compare(f1):
    with open(f1, 'r', encoding="utf-8") as r1:
        word1 = r1.readlines()
    Total = word1[-1]
    with open(f1, 'w+', encoding="utf-8") as c1:
        # c1.writelines(sorted(word1, key=lambda word1: (word1.split('\n')[-1][3:-1])))
        c1.writelines(sorted(word1[0:-1]))
        c1.writelines(Total)
    # word_deleted = set(word1) - set(word2)
    # print(word_deleted)
    # word_new = set(word2) - set(word1)
    # print(word_new)

if __name__ == '__main__':
    f1 = path+input(f'Enter filename to sort(no need.txt): ')+'.txt'
    sorted_to_compare(f1)
