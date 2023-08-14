#Deobfuscate by HuyAnh
#Zalo:0905491417
#huyanhnong.21

import requests,sys,os
import random
import string
import time
trang = "\033[1;37m"
xanh_la = "\033[1;32m"
xanh_duong = "\033[1;34m"
do = "\033[1;31m"
vang = "\033[1;33m"
tim = "\033[1;35m"
xanhnhat = "\033[1;36m"
thanh_dep=trang+do+'['+xanh_la+'⟨⟩'+do+'] '+xanh_duong+'➩ Tài Khoản : '+trang
os.system("cls" if os.name == "nt" else "clear")
def banner():
  banner = ("""
    
 \033[1;35m                 ██╗  ██╗██████╗ ████████╗          
 \033[1;36m                 ██║  ██║██╔══██╗╚══██╔══╝          
 \033[1;30m                 ███████║██║  ██║   ██║             
 \033[1;33m                 ██╔══██║██║  ██║   ██║             
 \033[1;32m                 ██║  ██║██████╔╝   ██║             
 \033[1;31m                 ╚═╝  ╚═╝╚═════╝    ╚═╝             
                                   
 \033[1;35m            ████████╗ ██████╗  ██████╗ ██╗     
 \033[1;36m            ╚══██╔══╝██╔═══██╗██╔═══██╗██║     
 \033[1;30m               ██║   ██║   ██║██║   ██║██║     
 \033[1;33m               ██║   ██║   ██║██║   ██║██║     
 \033[1;32m               ██║   ╚██████╔╝╚██████╔╝███████╗
 \033[1;31m              ╚═╝    ╚═════╝  ╚═════╝ ╚══════╝           
                  
                   \033[1;30m➩ \033[1;33mTOOL \033[1;32mREG \033[1;31mACC \033[1;36mGARENA
\033[1;30m==============================================================""")
  
  for i in banner:
    sys.stdout.write(i)
    sys.stdout.flush()
    time.sleep(0.00130)
banner()
def random_string(n):
    chars = string.ascii_letters + string.digits
    return ''.join(random.choice(chars) for _ in range(n))
def run():
    email = random_string(6)
    user = random_string(13)
    cookies = {
        '_ga': 'GA1.1.1387551280.1675945855',
        '_ga_1M7M9L6VPX': 'GS1.1.1679023440.5.0.1679023440.0.0.0',
        'datadome': '7oF0f9z2jcZ6-X1TlRAeHRs95QNPAi22Q5Q2JxNTiXgNR7sgPP~a2eMrJkL3shMtJ4aEVYqQt2zVZUlFhvtyYFVfI7H3gmVKoZyY2QxYSrODIJH9IN0eUI43y6LkHiAg',
    }

    headers = {
        'Accept': 'application/json, text/javascript, */*; q=0.01',
        'Accept-Language': 'en-US,en;q=0.9',
        'Connection': 'keep-alive',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        # 'Cookie': '_ga=GA1.1.1387551280.1675945855; _ga_1M7M9L6VPX=GS1.1.1679023440.5.0.1679023440.0.0.0; datadome=7oF0f9z2jcZ6-X1TlRAeHRs95QNPAi22Q5Q2JxNTiXgNR7sgPP~a2eMrJkL3shMtJ4aEVYqQt2zVZUlFhvtyYFVfI7H3gmVKoZyY2QxYSrODIJH9IN0eUI43y6LkHiAg',
        'Origin': 'https://sso.garena.com',
        'Referer': 'https://sso.garena.com/ui/register?locale=vi',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1 Edg/111.0.0.0',
        'X-Requested-With': 'XMLHttpRequest',
        'x-datadome-clientid': '7oF0f9z2jcZ6-X1TlRAeHRs95QNPAi22Q5Q2JxNTiXgNR7sgPP~a2eMrJkL3shMtJ4aEVYqQt2zVZUlFhvtyYFVfI7H3gmVKoZyY2QxYSrODIJH9IN0eUI43y6LkHiAg',
    }

    data = {
        'username': user,
        'email': f'{email}@gmail.com',
        'password': '37b0842cacde5e00f31bda0acce6e4a82e62ef97dba46b38d5ec41abab71526e9ea41d1a2b0b41db0f20b8aa4b9d5df19cd0dc50e0a09a0060c0e00e39306c1c5fcd0394e8e66ab0e06211d665f501b17e6ac38df2399cc548a8fb078bb70ec6c36fa8cbecb9e9680b22e15fe6a608fc0b4b4fef6f0c178c8989650d4ac604d1',
        'location': 'VI',
        'redirect_uri': '',
        'locale': 'vi',
        'mobile_no': '',
        'otp': '',
        'format': 'json',
        'id': '1679023495865',
    }

    response = requests.post('https://sso.garena.com/api/register', cookies=cookies, headers=headers, data=data).json()
    #print(response)
    check = response['username']
    if check == user:
        print(thanh_dep +user+"  \033[1;32m| Mật Khẩu: \033[1;37m@Khanh2007  \033[1;32m| \033[0;31mĐã lưu Vào File garena.txt")
        with open("garena.txt", "a+", encoding="utf-8") as f:
            f.write(user+" | @Khanh2007"+"\n")
while True:
    try:
        run()
    except:
        print("\033[0;31mLỗi xảy ra, đang thử lại...")
        time.sleep(5)
        continue
    time.sleep(10)