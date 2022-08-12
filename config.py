#Ur Instagram username and password
username = 'USERNAME or EMAIL'
password = 'PASSWORD'

url = f'https://www.instagram.com/accounts/login/'
ajax_url = f'https://www.instagram.com/accounts/login/ajax/'
p_url = f'https://i.instagram.com/api/v1/users/web_profile_info/?username='

path = r'./data/'

headers = {
'authority': 'www.instagram.com',
'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
'accept-language': 'zh-TW,zh;q=0.9',
'dnt': '1',
'sec-ch-prefers-color-scheme': 'dark',
'sec-ch-ua': '".Not/A)Brand";v="99", "Google Chrome";v="103", "Chromium";v="103"',
'sec-ch-ua-mobile': '?0',
'sec-ch-ua-platform': '"Windows"',
'sec-fetch-dest': 'document',
'sec-fetch-mode': 'navigate',
'sec-fetch-site': 'none',
'sec-fetch-user': '?1',
'sec-gpc': '1',
'upgrade-insecure-requests': '1',
'user-agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 12_3_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 Instagram 105.0.0.11.118 (iPhone11,8; iOS 12_3_1; en_US; en-US; scale=2.00; 828x1792; 165586599)',
'viewport-width': '1707',
'X-Requested-With': 'XMLHttpRequest',
}