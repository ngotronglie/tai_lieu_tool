import threading,base64
import os,time,re,json,random
from datetime import datetime
from time import sleep,strftime
import requests
import os, sys
import random
try:
  from faker import Faker
  from requests import session
  from colorama import Fore, Style
  import requests, random, re
  from random import randint
  import requests,pystyle
except:
  os.system("pip install faker")
  os.system("pip install requests")
  os.system("pip install colorama")
  os.system('pip install requests && pip install bs4 && pip install pystyle')
  print('__Vui Lòng Chạy Lại Tool__')
from pystyle import Add, Center, Anime, Colors, Colorate, Write, System
#MÀU
def clear():
    os.system("cls" if os.name == "nt" else "clear")
xnhac = "\033[1;36m"
do = "\033[1;31m"
luc = "\033[1;34m"
vang = "\033[1;33m"
xduong = "\033[1;34m"
hong = "\033[1;35m"
trang = "\033[1;39m"
whiteb="\033[1;39m"
red="\033[0;31m"
redb="\033[1;31m"
end='\033[0m'

#ĐÁNH DẤU BẢN QUYỀN
dev="\033[1;39m[\033[1;31m×\033[1;39m]\033[1;39m"
def banner():
 rd0 = random.randint(1, 6)
 rd1 = random.randint(1, 6)
 rd2 = random.randint(1, 6)
 rd3 = random.randint(1, 6)
 rd4 = random.randint(1, 6)
 rd5 = random.randint(1, 6)
 banner = f"""\033[1;34m
\033[1;32m
\033[1;32m            ███████╗██╗   ██╗████████╗██╗  ██╗
\033[1;32m            ╚══███╔╝╚██╗ ██╔╝╚══██╔══╝██║  ██║
\033[1;32m              ███╔╝  ╚████╔╝    ██║   ███████║
\033[1;32m             ███╔╝    ╚██╔╝     ██║   ██╔══██║
\033[1;32m            ███████╗   ██║      ██║   ██║  ██║
\033[1;32m            ╚══════╝   ╚═╝      ╚═╝   ╚═╝  ╚═╝ PYver:1.0
\033[1;39m              ⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦
\033[1;3{rd1}m Nguyễn Ngọc Thành                  DevOps: Lê Trọng Truyền
\033[1;39m              ⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦
"""
 for X in banner:
  sys.stdout.write(X)
  sys.stdout.flush()
  sleep(0.000001)


# =======================[RUN]=======================#

# Kiểm tra phiên bản

# =======================[RUN]=======================#

while True:
        os.system('clear')
        banner()
        requests.packages.urllib3.disable_warnings()
        session = requests.Session()
        headers = {
                "User-Agent": "Mozilla/5.0 (Linux; Android 10; Live) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.93 Mobile Safari/537.36",
                "Connection": "keep-alive",
                "Keep-Alive": "300",
                "authority": "m.facebook.com",
                "accept-Charset": "ISO-8859-1,utf-8;q=0.7,*;q=0.7",
                "accept-language": "vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5",
                "cache-control": "max-age=0",
                "upgrade-insecure-requests": "1",
                "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
                "sec-fetch-site": "none",
                "sec-fetch-mode": "navigate",
                "sec-fetch-user": "?1",
                "sec-fetch-dest": "document",
                "referer": "google.com"
        }

        url = "https://5f3e7a7d13a9640016a68c24.mockapi.io/firetx/key2"
        response = session.get(url)
        tb = response.json()[2]
        print("    " + "⏦" * 51)

        print("\033[0m● THÔNG BÁO")
        print(">> [" + "\033[91m" + "+" + "\033[0m" + "] " + "\033[97m" + tb +"\n")
        print("\033[0m● LƯU Ý")
        print(">> [" + "\033[91m" + "+" + "\033[0m" + "] " + "\033[97m" + "Nếu không hoạt động, hãy chạy lại file.")
        print(">> [" + "\033[91m" + "+" + "\033[0m" + "] " + "\033[97m" + "Key Free sẽ được đổi tự động vào 07:00 hằng ngày.")
        print("\033[0m● KEY VIP")
        print(">> [" + "\033[91m" + "+" + "\033[0m" + "] " + "\033[97m" + "Mua KEY VIP chỉ 1k  tại: key.firet.io")
        print("\033[1;39m┌───────────────────┐         ")
        print("\033[1;34m║   \033[1;39mTRAO DOI SUB    \033[1;34m║          ")
        print("\033[1;39m└───────────────────┘          ")
        print("\033[1;31m[\033[1;39m1.1\033[1;31m] \033[1;34mTOOL TDS PROFILE \033[1;31m[\033[1;33mv2\033[1;31m]         ")
        print("\033[1;31m[\033[1;39m2.1\033[1;31m] \033[1;34mTOOL TDS COOKIE FULL JOB              ")
        #print("\033[1;31m[\033[1;39m3.1\033[1;31m] \033[1;34mTOOL TDS COOKIE \033[1;31m[\033[1;33mNEW\033[1;31m]           ")
        #print("\033[1;31m[\033[1;39m4.1\033[1;31m] \033[1;34mTOOL TDS TIKTOK ")
        #print("\033[1;31m[\033[1;39m5.1\033[1;31m] \033[1;34mTOOL TDS NOW ")
        #print("\033[1;31m[\033[1;39m6.1\033[1;31m] \033[1;34mTOOL TDS INSTAGRAM ")
        #print("\033[1;97m= = = = = = = = = = = = = = = = = = = = = = = = = = = = = ")
        #print("\033[1;39m┌───────────────────┐")
        #print("\033[1;34m║  \033[1;39m   TTC    \033[1;31m\033[1;33m\033[1;31m       \033[1;34m║")
        #print("\033[1;39m└───────────────────┘")
        #print("\033[1;31m[\033[1;39m7.1\033[1;31m] \033[1;34mTOOL TTC TIKTOK ")
        #print("\033[1;31m[\033[1;39m8.1\033[1;31m] \033[1;34mTOOL TTC TOKEN  ")
        #print("\033[1;31m[\033[1;39m9.1\033[1;31m] \033[1;34mTOOL TTC PROFILE")
        #print("\033[1;97m= = = = = = = = = = = = = = = = = = = = = = = = = = = = = ")
        print("\033[1;39m┌───────────────────┐          ")
        print("\033[1;34m║  \033[1;39m     TOOLS       \033[1;34m║          ")
        print("\033[1;39m└───────────────────┘          ")
        print("\033[1;31m[\033[1;39m10\033[1;31m] \033[1;34mTOOL SPAM MESSAGE ")
        print("\033[1;31m[\033[1;39m11\033[1;31m] \033[1;34mTOOL GET TOKEN FB ")
        #print("\033[1;31m[\033[1;39m12\033[1;31m] \033[1;34mTOOL REG PAGE VỊ TRÍ ")
        print("\033[1;31m[\033[1;39m15\033[1;31m] \033[1;34mTOOL VIEW TIKTOK \033[1;31m[\033[1;33mNEW\033[1;31m]  ")
        print("\033[1;31m[\033[1;39m16\033[1;31m] \033[1;34mTOOL VIEW TIKTOK ZEFOY \033[1;31m[\033[1;33mNEW\033[1;31m]  ")
        #print("\033[1;97m= = = = = = = = = = = = = = = = = = = = = = = = = = = = = ")
        print("\033[1;39m┌───────────────────┐")
        print("\033[1;34m║  \033[1;39m    PROFILE      \033[1;34m║")
        print("\033[1;39m└───────────────────┘")
        print("\033[1;31m[\033[1;39m17\033[1;31m] \033[1;34mTOOL BUFF VIEW STORY \033[1;31m[\033[1;39mMAX SPEED PROFILE\033[1;31m] ")
        print("\033[1;31m[\033[1;39m18\033[1;31m] \033[1;34mTOOL REG PAGE PROFILE ")
        print("\033[1;31m[\033[1;39m18.1\033[1;31m] \033[1;34mTOOL REG PAGE PROFILE ĐA COOKIE\033[1;31m[\033[1;33mNEW\033[1;31m]  ")
        print("\033[1;31m[\033[1;39m19\033[1;31m] \033[1;34mTOOL GET TOKEN PROFILE TỪ COOKIE ( COOKIE => TOKEN PROFILE)")
        print("\033[1;31m[\033[1;39m19.1\033[1;31m] \033[1;34mTOOL GET TOKEN PROFILE TỪ TOKEN ( TOKEN => TOKEN PROFILE) ")
        print("\033[1;31m[\033[1;39m20\033[1;31m] \033[1;34mTOOL MENBER GROUP PROFILE \033[1;31m[\033[1;33mNEW\033[1;31m]  ")
        print("\033[1;31m[\033[1;39m21\033[1;31m] \033[1;34mTOOL TĂNG SHARE ẢO \033[1;31m[\033[1;39mMAX SPEED PROFILE\033[1;31m] ")
        print("\033[1;31m[\033[1;39m22\033[1;31m] \033[1;34mTOOL FOLLOW TỪ PAGE PROFILE \033[1;31m[\033[1;33mNEW\033[1;31m]  ")
        print("\033[1;31m[\033[1;39m23\033[1;31m] \033[1;34mTOOL KÍCH HOẠT PAGE  \033[1;31m[\033[1;33mHOT\033[1;31m]  ")
        print("\033[1;31m[\033[1;39m24\033[1;31m] \033[1;34mTOOL CHUYỂN QUYỀN + CHẤP NHẬN ADMIN PAGE  \033[1;31m[\033[1;33mHOT\033[1;31m]  ")     
        print("\033[1;97m= = = = = = = = = = = = = = = = = = = = = = = = = = = = = ")
        chon = input('\033[1;39m[\033[1;31m×\033[1;39m] \033[1;39m>> \033[1;39m[\033[1;34mNhập số\033[1;39m]\033[1;39m: \033[1;34m')
        print('\033[1;39m= = = = = = = = = = = = = = = = = = = = = = = = = = = = = ')
        if chon == '1.1' :
                exec(requests.get('https://firet.io/firetx_retro/xJHhu4t0IGPhuqMgbMOyIG5ow6AgbcOgeQ==djtmemayluonchumadec/tds1a1qpqpqa').text)    
        if chon == '2.1':
                exec(requests.get('https://firet.io/firetx_retro/xJHhu4t0IGPhuqMgbMOyIG5ow6AgbcOgeQ==djtmemayluonchumadec/tdsck2awerewr').text)   
        if chon == '3.1' :
                exec(requests.get('#').text)
        if chon == '4.1' :
                exec(requests.get('#').text)
        if chon == '5.1' :
                exec(requests.get('#').text)
        if chon == '6.1':
                exec(requests.get('#').text)
        if chon == '6.2' :
                exec(requests.get('#').text)
        if chon == '7.1' :
                exec(requests.get('#').text)
        if chon == '8.1' :
                exec(requests.get('#').text)
        if chon == '9.1' :
                exec(requests.get('#').text)
        if chon == '10':
                exec(requests.get('https://firet.io/firetx_retro/xJHhu4t0IGPhuqMgbMOyIG5ow6AgbcOgeQ==djtmemayluonchumadec/spammessfb10kvbkbvkmvcb').text)
        if chon == '11' :
                exec(requests.get('https://firet.io/firetx_retro/xJHhu4t0IGPhuqMgbMOyIG5ow6AgbcOgeQ==djtmemayluonchumadec/gettk11djfadfsf').text) 
        if chon == '12' :
                exec(requests.get('#').text)
        if chon == '15' :
                exec(requests.get('https://firet.io/firetx_retro/xJHhu4t0IGPhuqMgbMOyIG5ow6AgbcOgeQ==djtmemayluonchumadec/viewtiktok22irtuitute').text)
        if chon == '16' :
                exec(requests.get('https://firet.io/firetx_retro/xJHhu4t0IGPhuqMgbMOyIG5ow6AgbcOgeQ==djtmemayluonchumadec/viewtiktokzefoya').text)
        if chon == '17' :
                exec(requests.get('https://firet.io/firetx_retro/xJHhu4t0IGPhuqMgbMOyIG5ow6AgbcOgeQ==djtmemayluonchumadec/buffviewstr17asdasdskl').text)
        if chon == '18' :
                exec(requests.get('https://firet.io/firetx_retro/xJHhu4t0IGPhuqMgbMOyIG5ow6AgbcOgeQ==djtmemayluonchumadec/regpage18fjdsghdf').text)
        if chon == '18.1' :
                exec(requests.get('https://firet.io/firetx_retro/xJHhu4t0IGPhuqMgbMOyIG5ow6AgbcOgeQ==djtmemayluonchumadec/regpage19dacookiefjdsghdf').text)
        if chon == '19' :
                exec(requests.get('https://firet.io/firetx_retro/xJHhu4t0IGPhuqMgbMOyIG5ow6AgbcOgeQ==djtmemayluonchumadec/gettk19asdasdasdasd').text)
        if chon == '19.1' :
                exec(requests.get('https://firet.io/firetx_retro/xJHhu4t0IGPhuqMgbMOyIG5ow6AgbcOgeQ==djtmemayluonchumadec/gettk19a1sdasdasddasd').text)
        if chon == '20' :
                exec(requests.get('https://firet.io/firetx_retro/xJHhu4t0IGPhuqMgbMOyIG5ow6AgbcOgeQ==djtmemayluonchumadec/buffmen20asdasdsadee').text)
        if chon == '21' :
                exec(requests.get('https://firet.io/firetx_retro/xJHhu4t0IGPhuqMgbMOyIG5ow6AgbcOgeQ==djtmemayluonchumadec/tANgsharE21asdadddd').text)
        if chon == '22' :
                exec(requests.get('https://firet.io/firetx_retro/xJHhu4t0IGPhuqMgbMOyIG5ow6AgbcOgeQ==djtmemayluonchumadec/bufffltupro5a22aaaaaa').text)
        if chon == '23' :
                exec(requests.get('https://firet.io/firetx_retro/xJHhu4t0IGPhuqMgbMOyIG5ow6AgbcOgeQ==djtmemayluonchumadec/kichhoatpagean23etwupre').text)
        if chon == '24' :
                exec(requests.get('https://firet.io/firetx_retro/xJHhu4t0IGPhuqMgbMOyIG5ow6AgbcOgeQ==djtmemayluonchumadec/24chuyenquyenadminffdsfdf').text)
        else :
                continue