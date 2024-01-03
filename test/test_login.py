import requests, pickle
import re
from config import username,password,headers,url,ajax_url,p_url,path
from datetime import datetime
from openpyxl import Workbook, load_workbook
import compare, urlToPic, sort
import os, sys, time
import platform


system = platform.system()
date = datetime.now().strftime("%Y%m%d-%H%M")
time = int(datetime.now().timestamp())
payload = {
    'username': f'{username}',
    'enc_password': f'#PWD_INSTAGRAM_BROWSER:0:{time}:{password}',
    'queryParams': {},
    'optIntoOneTap': 'false',
	'stopDeletionNonce': '',
	'trustedDeviceRecords': {}
}
session = requests.Session()
res = session.get(url)
# with open('res.txt','a+', encoding='utf-8') as f:
#     f.write(res.text)
csrf = re.findall(r"csrf_token\\\":\\\"(.*?)\\\"",res.text)[0]
print(f'csrf={csrf}')
jazoest = re.findall(r"jazoest=(.*?)\"",res.text)[0]
print(f'jazoest={jazoest}')
cookies = res.cookies                   #res獲取第一次cookie和csrf
cookies['csrftoken'] = csrf
headers['x-csrftoken'] = csrf
# print("\n",headers,"\n")
r = session.post(ajax_url, data=payload, headers=headers, cookies=cookies)
print(r.status_code)
print(r.json)
print(r.cookies)