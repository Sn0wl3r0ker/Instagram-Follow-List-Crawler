# from pprint import pprint
from bs4 import BeautifulSoup
import requests
import re
from config import username,password,headers,url,ajax_url,p_url
from datetime import datetime
from openpyxl import Workbook
import compare

def ask_excel(ask_option):
    flag =''
    yes_list = ['y','Y','yes']
    no_list = ['n','N','no']
    while flag not in yes_list and flag not in no_list:
        flag = input(f'Do u want {ask_option} ? y/n: ')
        if(flag not in yes_list and flag not in no_list):
            print('plz enter y or n !!!')
    # print(f'flag={flag}')
    if(flag in yes_list):
        return 1
    elif(flag in no_list):
        return 0

def do_excel(uid,date,opt_title,option,root_json):              # 跑生成excel
    wb = Workbook()
    ws = wb.active
    title = ['username', 'full_name', 'profile_pic']
    ws.append(title)
    for users in root_json['users']:
        id = []
        id.append('@'+users['username'])
        id.append(users['full_name'])
        id.append(users['profile_pic_url']+'.jpg')
        ws.append(id)
    wb.save(f'{uid}{date}{opt_title[option]}.xlsx')

def do_txt(uid,date,opt_title,option,root_json):                # 跑生成txt 
    i=1
    with open(f'{uid}{date}{opt_title[option]}.txt', 'w+',encoding='utf-8') as f:
        for users in root_json['users']:
            # id = (f'{i}','@'+users['username'], users['full_name'])
            id = (f'@'+users['username'], users['full_name'])
            i+=1
        # reresponse = response.text.replace('\\u0026','&')
            f.write(str(id)+'\n')
        f.write(f'Total: {i-1} records!')
    print(f'Got {i-1} records!!!')

def main():
    date = datetime.now().strftime("%Y%m%d-%H%M")
    time = int(datetime.now().timestamp())
    payload = {
        'username': f'{username}',
        'enc_password': f'#PWD_INSTAGRAM_BROWSER:0:{time}:{password}',
        'queryParams': {},
        'optIntoOneTap': 'false'
    }
    uid = str(input('Enter id: '))
    option = str(input('following/followers: '))
    fcount = str(input('Enter max num of following/followers: '))
    opt_title = {
        'following': 'fwi',
        'followers': 'fwr',}
    ask = ask_excel('Excel file')
    # print(ask)
    with requests.session() as session:         #session = requests.sess.....
        res = session.get(url)
        csrf = re.findall(r"csrf_token\":\"(.*?)\"",res.text)[0]
        cookies = res.cookies                   #res獲取第一次cookie和csrf
        cookies['csrf'] = csrf
        headers['x-csrftoken'] = csrf
        headers['Referer'] = f'https://www.instagram.com/{uid}/following/'
        # print(cookies)
        session.post(ajax_url, data=payload, headers=headers, cookies=cookies)          #用現有cookie和csrf token 去取得登入的session
        # print(req2.text)

        fsi=session.get(p_url+uid,cookies=cookies,headers=headers)      
        friendid = str(re.findall(r"id\":\"(.*?)\"",fsi.text)[1])   
        print("userid:",friendid)
        # print(fsi.text)

        # url的後輟 可以像翻頁一樣去增加再爬取 或是直接爆max來爬取
        params = {
        'count': fcount,
        'max_id': ''}
        response = session.get(f'https://i.instagram.com/api/v1/friendships/{friendid}/{option}/', params=params, cookies=cookies, headers=headers)
        # print(response.text)
        root_json = response.json()
    if(ask == 1):
        do_excel(uid,date,opt_title,option,root_json)
    # pprint(response.text)
    do_txt(uid,date,opt_title,option,root_json)
    ask2 = ask_excel('compare with old file')
    if(ask2 == 1):
        f1 = input(f'Enter first filename(older file): ')+'.txt'
        f2 = input(f'Enter second filename(newer file): ')+'.txt'
        compare.compare_file(f1, f2)

if __name__ == '__main__':
    main()
