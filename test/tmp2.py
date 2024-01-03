import json
# def do_txt(filename,root_json):                # 跑生成txt 
#     i=1
#     with open(filename+f'.txt', 'w+',encoding='utf-8') as f:
#         for users in root_json['users']:
#             # id = (f'{i}','@'+users['username'], users['full_name'])
#             # print(type(users))
#             # print(f'!!!{users}!!!')
#             id = (f'@'+users['username'], users['full_name'])
#             i+=1
#         # reresponse = response.text.replace('\\u0026','&')
#             f.write(str(id)+'\n')
#         f.write(f'Total: {i-1} records!\n')
# do_txt('tmp3', json.load(open('tmp.txt', 'r', encoding='utf-8').read()))

with open('tmp.json', newline='') as jsonfile:
    data = json.load(jsonfile)
    # 或者這樣
    # data = json.loads(jsonfile.read())
    print(data)