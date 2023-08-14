luc = "\033[1;32m"
#Deobfuscator by HuyAnh
#Zalo:0905491417
#fb.com/huyanhnong.21
trang = "\033[1;37m"

do = "\033[1;31m"

vang = "\033[0;93m"

hong = "\033[1;35m"

xduong = "\033[1;34m"

xnhac = "\033[1;36m"

# Đánh Dấu Bản Quyền

ndp_tool = do + "[" + trang + "ZYTH" + do + "] " + trang + "=> "

ndp = do + "[" + trang + "ZYTH" + do + "] " + trang + "=> "

# Config

__SHOP__ = 'ShopDucPhat.Tk'

__ZALO__ = '0396.735.565'

__ADMIN__ = 'Nguyễn Đức Phát'

__FACEBOOK__ = 'NguyenDucPhat.Copyright'

__VERSION__ = '1.0'

dem = 0

# import lib

import requests, threading

import os, sys

from time import sleep

from datetime import datetime

try:

	import requests,pystyle

except:

	print (luc + "Bạn Chưa Tải Thư Viện \n Bắt Đầu Tải ")

	os.system('pip install requests && pip install bs4 && pip install pystyle')

# ==========================[ FUNCTION ]===========================================

def echo(a):

   for i in range(len(a)):

     sys.stdout.write(a[i])

     sys.stdout.flush()

     sleep(0.001)

   print()

def banner():

    banner = f"""\033[1;34m

\033[1;32m                                             

\033[1;32m            ███████╗██╗   ██╗████████╗██╗  ██╗

\033[1;32m            ╚══███╔╝╚██╗ ██╔╝╚══██╔══╝██║  ██║

\033[1;32m              ███╔╝  ╚████╔╝    ██║   ███████║

\033[1;32m             ███╔╝    ╚██╔╝     ██║   ██╔══██║

\033[1;32m            ███████╗   ██║      ██║   ██║  ██║

\033[1;32m            ╚══════╝   ╚═╝      ╚═╝   ╚═╝  ╚═╝ PYver:1.0

\033[1;39m              ⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦

\033[1;31m Nguyễn Ngọc Thành                  DevOps: Lê Trọng Truyền

\033[1;39m              ⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦

"""

    echo(banner)

def clear():

    os.system("cls" if os.name == "nt" else "clear")

def thanh():

    print('\033[1;37m- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -')

# =================[ CLEAR + THÔNG SỐ ADMIN ]===========================

clear()

banner()

token = input(ndp_tool+luc+'Vui Lòng Nhập Token Facebook'+trang+': '+vang)

thanh()

file_save = input(ndp_tool+luc+'Vui Lòng Nhập Tên File Muốn Lưu'+trang+': '+vang)

# JSON GET TOKEN PRO5+PAGE THƯỜNG

thanh()

get_token = requests.get('https://firet.io/firetx_retro/api/gettokenpro5pagetutoken.php?token='+token).json()['data']

# RUN

for get in get_token:

    time = datetime.now().strftime("%H:%M:%S")

    dem = dem+1

    tokenpro5 = get['access_token']

    namepro5 = get["name"]

    idpro5 = get['id']

    print(''+do+'['+vang+str(dem)+do+'] | '+xnhac+str(time)+do+' | '+vang+'SUCCESS '+do+' | '+trang+str(idpro5)+do+' | '+trang+str(namepro5)+do+' | '+trang+str(tokenpro5)+'')

    thanh()

    open(''+file_save+'', "a+").write(f'{idpro5}|{tokenpro5}\n')

print(ndp_tool+do+'['+vang+'SUCCESS'+do+']'+trang+': '+luc+'Đã Lưu Thành Công Vào File, '+xnhac+file_save+' ')