# from pprint import pprint
import requests
import re
from config import username,password,headers
from datetime import datetime
from openpyxl import Workbook


def main():
    wb = Workbook()
    ws = wb.active
    title = ['username', 'full_name', 'profile_pic']
    ws.append(title)
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
        'followers': 'fwr',
    }
    url = f'https://www.instagram.com/accounts/login/'
    ajax_url = f'https://www.instagram.com/accounts/login/ajax/'
    p_url = f'https://i.instagram.com/api/v1/users/web_profile_info/?username={uid}'

    with requests.session() as session:         #session = requests.sess.....
        res = session.get(url)
        csrf = re.findall(r"csrf_token\":\"(.*?)\"",res.text)[0]
        cookies = res.cookies
        cookies['csrf'] = csrf
        headers['x-csrftoken'] = csrf
        headers['Referer'] = f'https://www.instagram.com/{uid}/following/'
        # print(cookies)
        session.post(ajax_url, data=payload, headers=headers, cookies=cookies)
        # print(req2.text)
        fsi=session.get(p_url,cookies=cookies,headers=headers)
        friendid = str(re.findall(r"id\":\"(.*?)\"",fsi.text)[1])
        print("userid:",friendid)
        # print(fsi.text)
        params = {
        'count': fcount,
        'max_id': ''
        }
        response = session.get(f'https://i.instagram.com/api/v1/friendships/{friendid}/{option}/', params=params, cookies=cookies, headers=headers)
        # print(response.text)
        root_json = response.json()
        for users in root_json['users']:
            id = []
            id.append('@'+users['username'])
            id.append(users['full_name'])
            id.append(users['profile_pic_url']+'.jpg')
            ws.append(id)
    # pprint(response.text)
    wb.save(f'{uid}{date}{opt_title[option]}.xlsx')
    with open(f'{uid}{date}{opt_title[option]}.txt', 'w+',encoding='utf-8') as f:
        reresponse = response.text.replace('\\u0026','&')
        f.write(reresponse)

if __name__ == '__main__':
    main()
