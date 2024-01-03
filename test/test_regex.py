import re
# f = open('res.txt', 'r', encoding='utf-8')
# # print(re.findall(r"csrf_token\\\":\\\"(.*?)\"", f.read()))
# print(re.findall(r"jazoest=(.*?)\"",f.read()))

# https://www.instagram.com/ajax/qm/?__a=1&__user=0&__comet_req=7&jazoest=2898

# f = open('debug.txt', 'r', encoding='utf-8')
# print(re.findall(r"csrf_token\\\":\\\"(.*?)\"", f.read()))
# print(re.findall(r"\"next_max_id\":\"(.*?)\"",f.read()))

with open('list.txt', 'w', encoding='utf-8') as w:
    s = re.sub(r"==(.*)", '', str_p)
    w.write(s)

test_list = ['100', '100', '100', '100', '100', '300']
print(test_list[-1])


