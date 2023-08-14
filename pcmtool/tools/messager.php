import requests, os
import socket
os.system("clear")
from time import sleep
ip=socket.gethostbyname(socket.gethostname())
th='- - - - - - - - - - - - - - - - - - - - - - - - -'
def banner():
  print(f'''
  \033[1;36m_______    ____     ____    _      
 |__   __|  / __ \   / __ \  | |     
    | |    | |  | | | |  | | | |     
    | |    | |  | | | |  | | | |     
    | |    | |__| | | |__| | | |____ 
    |_|     \____/   \____/  |______|

        \033[1;33mTOOL SPAM MESSENGER
\033[1;35m= = = = = = = = = = = = = = = = = = = = = = = = = = = = = 
''')
banner()
id=input('\033[1;31m[🔥\033[1;31m] \033[1;37m=> \033[1;32mNhập id người cần gửi\033[1;37m: ')
while True:
    ck=input('\033[1;31m[🔥\033[1;31m] \033[1;37m=> \033[1;32mNhập cookie facebook\033[1;37m: ')
    try:
        get=requests.get(f'https://mbasic.facebook.com/privacy/touch/block/confirm/?bid={id}&ret_cancel&source=profile',headers={'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','accept-language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5','cookie': ck,'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="102", "Google Chrome";v="102"','sec-ch-ua-mobile': '?0','sec-ch-ua-platform': '"Windows"','sec-fetch-dest': 'document','sec-fetch-mode': 'navigate','sec-fetch-site': 'same-origin','sec-fetch-user': '?1','upgrade-insecure-requests': '1'}).text
        fb_dtsg=get.split('<input type="hidden" name="fb_dtsg" value="')[1].split('" autocomplete="off" />')[0]
        jazoest=get.split('<input type="hidden" name="jazoest" value="')[1].split('" autocomplete="off" />')[0]
        os.system('cls')
        break
    except:
        print('Cookie Die!!')
        
nd=input('\033[1;31m[🔥\033[1;31m] \033[1;37m=> \033[1;32mNhập nội dung\033[1;37m: ')
so_luong=int(input('\033[1;31m[🔥\033[1;31m] \033[1;37m=> \033[1;32mNhập số tin nhắn muốn gửi\033[1;37m: '))
delay=int(input('\033[1;31m[🔥\033[1;31m] \033[1;37m=> \033[1;32mNhập delay\033[1;31m(\033[1;33mkhuyến cáo trên 10s\033[1;31m)\033[1;37m: '))
headers = {
    'authority': 'm.facebook.com',
    'accept': '*/*',
    'accept-language': 'vi,en;q=0.9,vi-VN;q=0.8,fr-FR;q=0.7,fr;q=0.6,en-US;q=0.5',
    # Requests sorts cookies= alphabetically
    'cookie': ck,
    'origin': 'https://m.facebook.com',
    'referer': 'https://www.facebook.com',
    'sec-ch-ua': '"Chromium";v="104", " Not A;Brand";v="99", "Google Chrome";v="104"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36',
    'x-requested-with': 'XMLHttpRequest',
    'x-response-format': 'JSONStream',
}

params = {
    'icm': '1',
}

data = {
    f'ids[{id}]': id,
    'body': nd,
    'waterfall_source': 'message',
    'fb_dtsg': fb_dtsg,
    'jazoest': jazoest,
}
os.system("clear")
banner()
for i in range(1,so_luong+1):
    response = requests.post('https://m.facebook.com/messages/send/', params=params, headers=headers, data=data)
    print(f'\033[1;35m{i} \033[1;37m| \033[1;32mGửi Tin Nhắn Thành Công \033[1;37m| \033[1;33m{nd}')
    sleep(delay)      