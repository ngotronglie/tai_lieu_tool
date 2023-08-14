
import requests,os,sys, time
from random import choice, randint, shuffle
from pystyle import Add, Center, Anime, Colors, Colorate, Write, System
from os.path import isfile
from bs4 import BeautifulSoup
from datetime import datetime
import re,requests,os,sys
from time import sleep 
from datetime import date
import requests, random
import requests
import base64, json,os
from datetime import date
from datetime import datetime
from time import sleep,strftime
from bs4 import BeautifulSoup
from datetime import datetime
import re,requests,os,sys
from time import sleep
from datetime import date
import requests, random
import uuid, re
from pystyle import Write,Colors
from bs4 import BeautifulSoup
import socket
from datetime import datetime
System.Clear()
System.Title("hdttool")
System.Size(140, 40)
banner = r"""

                 ██╗  ██╗██████╗ ████████╗
                 ██║  ██║██╔══██╗╚══██╔══╝
                 ███████║██║  ██║   ██║
                 ██╔══██║██║  ██║   ██║
                 ██║  ██║██████╔╝   ██║
                 ╚═╝  ╚═╝╚═════╝    ╚═╝

            ████████╗ ██████╗  ██████╗ ██╗
            ╚══██╔══╝██╔═══██╗██╔═══██╗██║
               ██║   ██║   ██║██║   ██║██║
               ██║   ██║   ██║██║   ██║██║
               ██║   ╚██████╔╝╚██████╔╝███████╗
               ╚═╝    ╚═════╝  ╚═════╝ ╚══════╝

                    𝙷𝙰̃𝚈 𝙱𝙰̂́𝙼 𝚇𝚄𝙾̂́𝙽𝙶 𝙳𝙾̀𝙽𝙶
"""
Anime.Fade(Center.Center(banner), Colors.red_to_yellow, Colorate.Vertical, enter=True)
#Color
trang = "\033[1;37m"
xanh_la = "\033[1;32m"
xanh_duong = "\033[1;34m"
do = "\033[1;31m"
vang = "\033[1;33m"
tim = "\033[1;35m"
xanhnhat = "\033[1;36m"
# Lmao
thanh_xau=trang+'~'+do+'['+vang+'⟨⟩'+do+'] '+trang+'➩  '+xanhnhat
thanh_dep=trang+'~'+do+'['+xanh_la+'✓'+do+'] '+trang+'➩  '+xanhnhat
def get_ip_from_url(url):
    response = requests.get(url)
    ip_address = socket.gethostbyname(response.text.strip())
    return ip_address
url = "http://kiemtraip.com/raw.php"
ip = get_ip_from_url(url)
Write.Print('   ======================================================== \n',Colors.green_to_red,interval=0.0001,end='\r')     
Write.Print('                   ██╗  ██╗██████╗ ████████╗          \n',Colors.green_to_red,interval=0.0001,end='\r')
Write.Print('                   ██║  ██║██╔══██╗╚══██╔══╝          \n',Colors.green_to_red,interval=0.0001,end='\r')
Write.Print('                   ███████║██║  ██║   ██║             \n',Colors.green_to_red,interval=0.0001,end='\r')
Write.Print('                   ██╔══██║██║  ██║   ██║             \n',Colors.green_to_red,interval=0.0001,end='\r')
Write.Print('                   ██║  ██║██████╔╝   ██║             \n',Colors.green_to_red,interval=0.0001,end='\r')
Write.Print('                   ╚═╝  ╚═╝╚═════╝    ╚═╝             \n',Colors.green_to_red,interval=0.0001,end='\r')
Write.Print(' \n',Colors.green_to_red,interval=0.0001,end='\r')
Write.Print('              ████████╗ ██████╗  ██████╗ ██╗     \n',Colors.green_to_red,interval=0.0001,end='\r')
Write.Print('              ╚══██╔══╝██╔═══██╗██╔═══██╗██║     \n',Colors.green_to_red,interval=0.0001,end='\r')
Write.Print('                 ██║   ██║   ██║██║   ██║██║     \n',Colors.green_to_red,interval=0.0001,end='\r')
Write.Print('                 ██║   ██║   ██║██║   ██║██║     \n',Colors.green_to_red,interval=0.0001,end='\r')
Write.Print('                 ██║   ╚██████╔╝╚██████╔╝███████╗ \n',Colors.green_to_red,interval=0.0001,end='\r')
Write.Print('                 ╚═╝    ╚═════╝  ╚═════╝ ╚══════╝ \n',Colors.green_to_red,interval=0.0001,end='\r')
Write.Print('   ======================================================== \n',Colors.green_to_red,interval=0.0001,end='\r')     
Write.Print('           ➩ Copyright © HDT-TOOL  \n',Colors.green_to_red,interval=0.0001,end='\r')
Write.Print('           ➩ Zalo Group: https://zalo.me/g/bprmyn080 \n',Colors.green_to_red,interval=0.0001,end='\r')
Write.Print('           ➩ Web Tool : https://linkbio.co/hdttool \n',Colors.green_to_red,interval=0.0001,end='\r')
Write.Print('           ➩ Youtube: https://youtube.com/@HDT-TOOL \n',Colors.green_to_red,interval=0.0001,end='\r')
Write.Print('   ======================================================== \n',Colors.green_to_red,interval=0.0001,end='\r')     
from time import strftime
ngay=int(strftime('%d'))
key1=str(ngay*24032006+74321)
key = 'HDT/'+key1
keyv1 = 'bao'
#os.system("cls" if os.name == "nt" else "clear")
if not os.path.exists('Key_HDT.txt'):
    url = 'https://toolsiuvip.tk/api/keyfree.php?key='+key
    token_web1s = '4027f152-feea-4b6c-8d74-1193a3976d7b'
    web1s = requests.get(f'https://web1s.com/api?token={token_web1s}&url={url}').json()
    if web1s['status']=="error":
        print(web1s['message'])
        quit()
    else:
        link_key=web1s['shortenedUrl']
    print('\033[1;34mVƯỢT LINK ĐỂ LẤY KEY FREE: \033[1;32m'+link_key)
    keynhap = input('\033[1;34mKEY ĐÃ VƯỢT LÀ: \033[1;32m')
    with open('Key_HDT.txt', 'w') as f:
        f.write(keynhap)

with open('Key_HDT.txt', 'r') as f:
   keynhap = f.read()
if keynhap == key or keynhap== keyv1:
  nhap = ("""
\033[1;31m➩\033[1;32m Key Đúng Và Đã Được Lưu Trữ Trong 24h
\033[1;31m➩\033[1;32m Chúc Bạn Chạy Tool Vui Vẻ \033[1;35.....""")
  for i in nhap:
    sys.stdout.write(i)
    sys.stdout.flush()
    time.sleep(0.01)
else:
  print('\033[1;37mKey Sai Hoặc Đã Hết Hạn Vui Lòng Khởi Động Lại Tool Và Vượt Link Lại \033[1;31m!!!\n')
  os.remove('Key_HDT.txt')
  quit()
den = "\033[1;90m"
luc = "\033[1;32m"
trang = "\033[1;37m"
red = "\033[1;31m"
vang = "\033[1;33m"
tim = "\033[1;35m"
lamd = "\033[1;34m"
lam = "\033[1;36m"
hong = "\033[1;95m"
thanh_xau= trang + red + "[" + vang+ "⟨⟩" + red + "] " + trang + "➩ "
thanh_dep= trang + red + "[" + luc + "✓" + red + "] " + trang + "➩ "
#THU
from bs4 import BeautifulSoup
from datetime import datetime
import re,requests,os,sys
from time import sleep
from datetime import date
import requests, random
import requests
import base64, json,os
from datetime import date
from datetime import datetime
from time import sleep,strftime
from bs4 import BeautifulSoup
from datetime import datetime
import re,requests,os,sys
from time import sleep
from datetime import date
import requests, random
import uuid, re
from pystyle import Write,Colors
from bs4 import BeautifulSoup
import socket
from datetime import datetime

time=datetime.now().strftime("%H:%M:%S")
from pystyle import *
data_machine = []
today = date.today()
now = datetime.now()
thu = now.strftime("%A")
ngay_hom_nay = now.strftime("%d")
thang_nay = now.strftime("%m")
nam_ = now.strftime("%Y")

#IP
def get_ip_from_url(url):
    response = requests.get(url)
    ip_address = socket.gethostbyname(response.text.strip())
    return ip_address
url = "http://kiemtraip.com/raw.php"
ip = get_ip_from_url(url)
Anime.Fade(Center.Center(banner), Colors.red_to_yellow, Colorate.Vertical, enter=True)
Write.Print('============================================================== \n',Colors.green_to_red,interval=0.0001,end='\r')  
Write.Print('                   ██╗  ██╗██████╗ ████████╗          \n',Colors.green_to_red,interval=0.0001,end='\r')
Write.Print('                   ██║  ██║██╔══██╗╚══██╔══╝          \n',Colors.green_to_red,interval=0.0001,end='\r')
Write.Print('                   ███████║██║  ██║   ██║             \n',Colors.green_to_red,interval=0.0001,end='\r')
Write.Print('                   ██╔══██║██║  ██║   ██║             \n',Colors.green_to_red,interval=0.0001,end='\r')
Write.Print('                   ██║  ██║██████╔╝   ██║             \n',Colors.green_to_red,interval=0.0001,end='\r')
Write.Print('                   ╚═╝  ╚═╝╚═════╝    ╚═╝             \n',Colors.green_to_red,interval=0.0001,end='\r')
Write.Print(' \n',Colors.green_to_red,interval=0.0001,end='\r')
Write.Print('              ████████╗ ██████╗  ██████╗ ██╗     \n',Colors.green_to_red,interval=0.0001,end='\r')
Write.Print('              ╚══██╔══╝██╔═══██╗██╔═══██╗██║     \n',Colors.green_to_red,interval=0.0001,end='\r')
Write.Print('                 ██║   ██║   ██║██║   ██║██║     \n',Colors.green_to_red,interval=0.0001,end='\r')
Write.Print('                 ██║   ██║   ██║██║   ██║██║     \n',Colors.green_to_red,interval=0.0001,end='\r')
Write.Print('                 ██║   ╚██████╔╝╚██████╔╝███████╗ \n',Colors.green_to_red,interval=0.0001,end='\r')
Write.Print('                 ╚═╝    ╚═════╝  ╚═════╝ ╚══════╝ \n',Colors.green_to_red,interval=0.0001,end='\r')
Write.Print(' \n',Colors.green_to_red,interval=0.0001,end='\r')
print(f"      {lamd}     ➩ Ngày{trang}: {vang}{ngay_hom_nay}{red} |{luc} Tháng{trang}: {vang}{thang_nay} {red}| {luc}Năm{trang}: {vang}{nam_}")
print(f'{lamd}           ➩ IP Hiện Tại Của Bạn ]{trang}{vang} ➩ {vang}{ip}')
Write.Print('           ➩ ADMIN © HDT-TOOL  \n',Colors.green_to_red,interval=0.0001,end='\r')
Write.Print('           ➩ NHÓM ZALO: https://zalo.me/g/bprmyn080 \n',Colors.green_to_red,interval=0.0001,end='\r')
Write.Print('           ➩ WEB TOOL : https://linkbio.co/hdttool \n',Colors.green_to_red,interval=0.0001,end='\r')
Write.Print('           ➩ YOUTUBE: https://youtube.com/@HDT-TOOL \n',Colors.green_to_red,interval=0.0001,end='\r')
Write.Print('============================================================== \n',Colors.green_to_red,interval=0.0001,end='\r')  
print("\033[1;37m╔═════════════════════╗")
print("\033[1;37m║  \033[1;36mTOOL Trao Đổi Sub  \033[1;37m║")
print("\033[1;37m╚═════════════════════╝")
print("\033[1;31m[\033[1;32m⟨⟩\033[1;31m]\033[1;33m➩ \033[1;34mNhập Số \033[1;31m[\033[1;33m1\033[1;31m] \033[1;32mTDS TIKTOK MAX SPEED\033[1;33m [\033[1;31mVIP\033[1;33m]")
print("\033[1;31m[\033[1;32m⟨⟩\033[1;31m]\033[1;33m➩ \033[1;34mNhập Số \033[1;31m[\033[1;33m2\033[1;31m] \033[1;32mTDS BẰNG PAGE PRO5\033[1;33m [\033[1;31mVIP\033[1;33m]")
print("\033[1;31m[\033[1;32m⟨⟩\033[1;31m]\033[1;33m➩ \033[1;34mNhập Số \033[1;31m[\033[1;33m3\033[1;31m] \033[1;32mTDS FACEBOOK FULL JOD\033[1;33m [\033[1;31mVIP\033[1;33m]")
print("\033[1;37m╔═══════════════════════╗")
print("\033[1;37m║  \033[1;36mTOOL Tương Tác Chéo  \033[1;37m║")
print("\033[1;37m╚═══════════════════════╝")
print("\033[1;31m[\033[1;32m⟨⟩\033[1;31m]\033[1;33m➩ \033[1;34mNhập Số \033[1;31m[\033[1;33m4\033[1;31m] \033[1;32mTTC PAGE PRO5\033[1;33m [\033[1;31mVIP 1\033[1;33m]")
print("\033[1;31m[\033[1;32m⟨⟩\033[1;31m]\033[1;33m➩ \033[1;34mNhập Số \033[1;31m[\033[1;33m5\033[1;31m] \033[1;32mTTC TIKTOK MAX SPEED\033[1;33m [\033[1;31mVIP\033[1;33m]")
print("\033[1;31m[\033[1;32m⟨⟩\033[1;31m]\033[1;33m➩ \033[1;34mNhập Số \033[1;31m[\033[1;33m6\033[1;31m] \033[1;32mTTC INSTAGRAM VIPIG\033[1;33m [\033[1;31mVIP\033[1;33m]")
print("\033[1;31m[\033[1;32m⟨⟩\033[1;31m]\033[1;33m➩ \033[1;34mNhập Số \033[1;31m[\033[1;33m7\033[1;31m] \033[1;32mTTC PAGE PRO5\033[1;33m [\033[1;31mVIP 2\033[1;33m]")
print("\033[1;37m╔══════════════════════╗")
print("\033[1;37m║  \033[1;36mTOOL TIỆN ÍCH PRO5  \033[1;37m║")
print("\033[1;37m╚══════════════════════╝")
print("\033[1;31m[\033[1;32m⟨⟩\033[1;31m]\033[1;33m➩ \033[1;34mNhập Số \033[1;31m[\033[1;33m8\033[1;31m] \033[1;32mSHARE ẢO BẰNG PRO5 MAX SPEED\033[1;33m [\033[1;31mVIP\033[1;33m]")
print("\033[1;31m[\033[1;32m⟨⟩\033[1;31m]\033[1;33m➩ \033[1;34mNhập Số \033[1;31m[\033[1;33m9\033[1;31m] \033[1;32mBUFF CẢM XÚC STORY BẰNG PRO5\033[1;33m [\033[1;31mVIP\033[1;33m]")
print("\033[1;31m[\033[1;32m⟨⟩\033[1;31m]\033[1;33m➩ \033[1;34mNhập Số \033[1;31m[\033[1;33m10\033[1;31m] \033[1;32mBUFF VIEW STORY BẰNG PRO5\033[1;33m [\033[1;31mVIP\033[1;33m]")
print("\033[1;31m[\033[1;32m⟨⟩\033[1;31m]\033[1;33m➩ \033[1;34mNhập Số \033[1;31m[\033[1;33m11\033[1;31m] \033[1;32mLIKE BÀI VIẾT BẰNG PAGE PRO5\033[1;33m [\033[1;31mVIP\033[1;33m]")
print("\033[1;31m[\033[1;32m⟨⟩\033[1;31m]\033[1;33m➩ \033[1;34mNhập Số \033[1;31m[\033[1;33m12\033[1;31m] \033[1;32mKÍCH HOẠT PAGE PRO5\033[1;33m [\033[1;31mVIP\033[1;33m]")
print("\033[1;31m[\033[1;32m⟨⟩\033[1;31m]\033[1;33m➩ \033[1;34mNhập Số \033[1;31m[\033[1;33m13\033[1;31m] \033[1;32mGET TOKEN PAGE PRO5\033[1;33m [\033[1;31mVIP\033[1;33m]")
print("\033[1;31m[\033[1;32m⟨⟩\033[1;31m]\033[1;33m➩ \033[1;34mNhập Số \033[1;31m[\033[1;33m14\033[1;31m] \033[1;32mBUFF FOLOW BẰNG PAGE PRO5\033[1;33m [\033[1;31mVIP\033[1;33m]")
print("\033[1;31m[\033[1;32m⟨⟩\033[1;31m]\033[1;33m➩ \033[1;34mNhập Số \033[1;31m[\033[1;33m15\033[1;31m] \033[1;32mCHUYỂN QUYỀN QTV PRO5\033[1;33m [\033[1;31mVIP\033[1;33m]")
print("\033[1;31m[\033[1;32m⟨⟩\033[1;31m]\033[1;33m➩ \033[1;34mNhập Số \033[1;31m[\033[1;33m16\033[1;31m] \033[1;32mBUFF TV NHÓM BẰNG PAGE PRO5\033[1;33m [\033[1;31mVIP\033[1;33m]")
print("\033[1;31m[\033[1;32m⟨⟩\033[1;31m]\033[1;33m➩ \033[1;34mNhập Số \033[1;31m[\033[1;33m17\033[1;31m] \033[1;32mREG PAGE PRO5 + ÚP ĐẠI DIỆN\033[1;33m [\033[1;31mVIP\033[1;33m]")
print("\033[1;37m╔════════════════════════╗")
print("\033[1;37m║  \033[1;36mTOOL ENCODE + DECODE  \033[1;37m║")
print("\033[1;37m╚════════════════════════╝")
print("\033[1;31m[\033[1;32m⟨⟩\033[1;31m]\033[1;33m➩ \033[1;34mNhập Số \033[1;31m[\033[1;33m18\033[1;31m] \033[1;32mENCODE - INPOSTOR\033[1;33m [\033[1;31mVIP\033[1;33m]")
print("\033[1;31m[\033[1;32m⟨⟩\033[1;31m]\033[1;33m➩ \033[1;34mNhập Số \033[1;31m[\033[1;33m19\033[1;31m] \033[1;32mENCODE - 5 LỚP\033[1;33m [\033[1;31mVIP\033[1;33m]")
print("\033[1;31m[\033[1;32m⟨⟩\033[1;31m]\033[1;33m➩ \033[1;34mNhập Số \033[1;31m[\033[1;33m20\033[1;31m] \033[1;32mENCODE - MARSHAL 16 CHẾ ĐỘ\033[1;33m [\033[1;31mVIP\033[1;33m]")
print("\033[1;37m╔══════════════════╗")
print("\033[1;37m║  \033[1;36mTOOL TIỆN KHÁC  \033[1;37m║")
print("\033[1;37m╚══════════════════╝")
print("\033[1;31m[\033[1;32m⟨⟩\033[1;31m]\033[1;33m➩ \033[1;34mNhập Số \033[1;31m[\033[1;33m21\033[1;31m] \033[1;32mREG ACC GARENA\033[1;33m [\033[1;31mVIP\033[1;33m]")
print("\033[1;31m[\033[1;32m⟨⟩\033[1;31m]\033[1;33m➩ \033[1;34mNhập Số \033[1;31m[\033[1;33m22\033[1;31m] \033[1;32mKẾT BẠN FACEBOOK GỢI Ý\033[1;33m [\033[1;31mVIP\033[1;33m]")
print("\033[1;31m[\033[1;32m⟨⟩\033[1;31m]\033[1;33m➩ \033[1;34mNhập Số \033[1;31m[\033[1;33m23\033[1;31m] \033[1;32mREG PAGE VỊ TRÍ\033[1;33m [\033[1;31mVIP\033[1;33m]")
print("\033[1;31m[\033[1;32m⟨⟩\033[1;31m]\033[1;33m➩ \033[1;34mNhập Số \033[1;31m[\033[1;33m24\033[1;31m] \033[1;32mCHUYỂN PAGE VỊ TRÍ\033[1;33m [\033[1;31mVIP\033[1;33m]")
print("\033[1;31m[\033[1;32m⟨⟩\033[1;31m]\033[1;33m➩ \033[1;34mNhập Số \033[1;31m[\033[1;33m25\033[1;31m] \033[1;32mBUFF VIEW TIKTOK - ZEFOY\033[1;33m [\033[1;31mVIP\033[1;33m]")
print("\033[1;31m[\033[1;32m⟨⟩\033[1;31m]\033[1;33m➩ \033[1;34mNhập Số \033[1;31m[\033[1;33m26\033[1;31m] \033[1;32mTOOL LỌC PROXY\033[1;33m [\033[1;31mVIP\033[1;33m]")
print("\033[1;31m[\033[1;32m⟨⟩\033[1;31m]\033[1;33m➩ \033[1;34mNhập Số \033[1;31m[\033[1;33m27\033[1;31m] \033[1;32mTOOL RELY COMMENT POST + KÈM ẢNH\033[1;33m [\033[1;31mVIP\033[1;33m]")
print("\033[1;31m[\033[1;32m⟨⟩\033[1;31m]\033[1;33m➩ \033[1;34m══\x1b[1;91m══\033[1;32m══\033[1;31m══\x1b[1;94m══\x1b[1;96m══\x1b[1;91m══\033[1;32m══\033[1;31m══\x1b[1;94m══\x1b[1;96m══\x1b[1;91m══\033[1;32m═══\033[1;31m══\x1b[1;94m══\x1b[1;96m══\x1b[1;91m══\033[1;32m══\033[1;31m══\x1b[1;94m══\x1b[1;96m══\x1b[1;91m══\033[1;32m══\033[1;31m══\x1b[1;94m══")
chon = int(input('\033[1;31m[\033[1;32m⟨⟩\033[1;31m]\033[1;33m➩ \033[1;34mNhập Số \033[1;37m: \033[1;33m'))
if chon == 1 :
        exec(requests.get('https://hdttool.000webhostapp.com/1.html').text)
if chon == 2 :
        exec(requests.get('https://hdttool.000webhostapp.com/2.html').text)
if chon == 3 :
        exec(requests.get('https://hdttool.000webhostapp.com/tdsfull.html').text)
if chon == 4 :
        exec(requests.get('https://hdttool.000webhostapp.com/3.html').text)
if chon == 5 :
        exec(requests.get('https://hdttool.000webhostapp.com/4.html').text)
if chon == 6 :
        exec(requests.get('https://hdttool.000webhostapp.com/ig.html').text)
if chon == 7 :
        exec(requests.get('https://hdttool.000webhostapp.com/v2.html').text)
if chon == 8 :
        exec(requests.get('https://hdttool.000webhostapp.com/shareaopro5.html').text)
if chon == 9 :
        exec(requests.get('https://hdttool.000webhostapp.com/REACTION.html').text)
if chon == 10 :
        exec(requests.get('https://hdttool.000webhostapp.com/buffview.html').text)
if chon == 11 :
        exec(requests.get('https://hdttool.000webhostapp.com/like.html').text)
if chon == 12 :
        exec(requests.get('https://hdttool.000webhostapp.com/kichhoat.html').text)
if chon == 13 :
        exec(requests.get('https://hdttool.000webhostapp.com/gettoken.html').text)
if chon == 14 :
        exec(requests.get('https://hdttool.000webhostapp.com/bufffolow.html').text)
if chon == 15 :
 exec(requests.get('https://hdttool.000webhostapp.com/chuyenqtv.html').text)
if chon == 16 :
 exec(requests.get('https://hdttool.000webhostapp.com/buffgourp.html').text)
if chon == 17 :
 exec(requests.get('https://hdttool.000webhostapp.com/regpro5.html').text)
if chon == 18 :
 exec(requests.get('https://hdttool.000webhostapp.com/encinpostor.html').text)
if chon == 19 :
 exec(requests.get('https://hdttool.000webhostapp.com/enc5lop.html').text)
if chon == 20 :
 exec(requests.get('https://hdttool.000webhostapp.com/enc16chedo.html').text)
if chon == 21 :
 exec(requests.get('https://hdttool.000webhostapp.com/garena.html').text)
if chon == 22 :
 exec(requests.get('https://hdttool.000webhostapp.com/ketban.html').text)
if chon == 23 :
 exec(requests.get('https://hdttool.000webhostapp.com/regvitri.html').text)
if chon == 24 :
 exec(requests.get('https://hdttool.000webhostapp.com/chuyenvitri.html').text)
if chon == 25 :
 exec(requests.get('https://hdttool.000webhostapp.com/buffviewtiktok.html').text)
if chon == 26 :
 exec(requests.get('https://hdttool.000webhostapp.com/locproxy.html').text)
if chon == 27 :
 exec(requests.get('https://hdttool.000webhostapp.com/coment.html').text)
else :
        print (" Sai Lựa Chọn ")
        exit()