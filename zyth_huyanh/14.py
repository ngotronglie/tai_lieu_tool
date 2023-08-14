import time, os, random, requests
#Deobfuscator by HuyAnh
#Zalo:0905491417
#fb.com/huyanhnong.21
from time import sleep

from datetime import date

import os, sys

from tracemalloc import stop

from urllib import request

from requests import session

from colorama import Fore, Style

import requests, random, re, time





def logo():



    os.system('cls')

    log = '''                                      

\033[1;32m            ███████╗██╗   ██╗████████╗██╗  ██╗

\033[1;32m            ╚══███╔╝╚██╗ ██╔╝╚══██╔══╝██║  ██║

\033[1;32m              ███╔╝  ╚████╔╝    ██║   ███████║

\033[1;32m             ███╔╝    ╚██╔╝     ██║   ██╔══██║

\033[1;32m            ███████╗   ██║      ██║   ██║  ██║

\033[1;32m            ╚══════╝   ╚═╝      ╚═╝   ╚═╝  ╚═╝ BUFF FOLLOW BẰNG PAGE V1

\033[1;39m              ⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦

\033[1;32m Nguyễn Ngọc Thành                  DevOps: Lê Trọng Truyền

\033[1;39m              ⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦

    '''

    import sys

    for oo in log:

        sys.stdout.write(oo)

        sys.stdout.flush()

        sleep(0.003)



logo()

tokenfb = input('\033[1;32mNhập Token Của Bạn (Dạng EAAB): ')

infor = requests.get('https://graph.facebook.com/v13.0/me?fields=name&access_token='+tokenfb).json()

try:

    print("\033[1;32mTên Tài Khoản Facebook: "+infor['name'])

    print("\033[1;35mID Tài Khoản : "+infor['id'])

except:

    print("\033[1;52mToken Die Hoặc Sai")

print('Nếu Muốn Lấy Toàn Bộ Page Trong Acc Thì Nhập Nhỏ Hơn 1 Page So Với Số Lượng Page Đang Có')

print('Nếu Số Page Nhiều Thì Quá Trình Này Sẽ Lâu')

sllpagebuff = input('Nhập Số Lượng Page Cần Buff: ')

page = requests.get('https://graph.facebook.com/v11.0/me?fields=facebook_pages.limit(2000222222222)%7Bid%7D&access_token='+tokenfb).json()

stt =0

f = open("/sdcard/download/zyth/idpage.txt", "w")

logo()

print("Bắt Đầu Quá Trình Lấy Token Page")

print('TOOL BUFF FOLLOW BẰNG PAGE VERSION 1.0')

for i in range(int(sllpagebuff)):

    try:

        stt +=1

        id = page['facebook_pages']['data'][stt]['id']

        laytokenpage = requests.get('https://graph.facebook.com/v13.0/'+id+'?fields=access_token&access_token='+tokenfb).json()

        tokenpage = laytokenpage['access_token']

        print('['+str(stt)+'] Lấy Thành Công Token, ID Page Là: '+str(id))

        f.write(id+"|"+tokenpage+"\n")

        stt = stt

    except:

        print('Lấy Token Lỗi Hoặc Số Lượng Page Nhập Vào Vượt Quá Số Lượng Page Có Trong Acc')

        time.sleep(4.5)

        quit()

f.close()



print('Lấy Thành Công '+str(stt)+' Page')



idpro = input('Nick Cần Buff FOLLOW Là: ')

logo()

print('TOOL BUFF FOLLOW BẰNG PAGE VERSION 1.0')

filetoken = open("/sdcard/download/zyth/idpage.txt", "r").readlines()

i = 0



for buff in filetoken:



    idpage = buff.split('|')[0]

    tokenpagefile = buff.split('|')[1]

    i += 1



    bufffl = requests.post('https://graph.facebook.com/'+idpro+'/subscribers?access_token='+tokenpagefile).json()



    if bufffl == True:

        print('['+str(i)+']Buff Thành Công Cho ID '+idpro+' Với ID Page Là '+idpage)





    else:

        print('['+str(i)+']Buff Thất Bại, Page Bị Block ')







