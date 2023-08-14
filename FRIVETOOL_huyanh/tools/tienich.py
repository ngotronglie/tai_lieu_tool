'''Deobfuscator by HuyAnh
Zalo: 0905491417
fb: huyanhnong.21



'''
den = "\033[1;90m"
luc = "\033[1;32m"
trang = "\033[1;37m"
red = "\033[1;31m"
vang = "\033[1;33m"
tim = "\033[1;35m"
lamd = "\033[1;34m"
lam = "\033[1;36m"
hong = "\033[1;95m"
thanh_xau= red+"[" + vang+ "⟨⟩" + red + "] " + trang + "➩ "
thanh_dep= red+"[" + luc + "✓" + red + "] " + trang + "➩ "
#thư viện
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
import socket
from pystyle import Write,Colors
key_pass1 = 'FRIVE-TOOL'
key_pass2 = 'FRIVE-TOOL'
#TIME
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
def is_connected():
    try:
        import socket
        socket.create_connection(("1.1.1.1", 53))
        return True
    except OSError:
        pass
    return False
def get_ip_from_url(url):
    response = requests.get(url)
    ip_address = socket.gethostbyname(response.text.strip())
    return ip_address
url = "http://kiemtraip.com/raw.php"
ip = get_ip_from_url(url)
os.system("cls" if os.name == "nt" else "clear")
Write.Print(f'             ███████╗██████╗ ██╗██╗   ██╗███████╗\n',Colors.cyan_to_green,interval=0.0001)
Write.Print(f'             ██╔════╝██╔══██╗██║██║   ██║██╔════╝\n',Colors.cyan_to_green,interval=0.0001)
Write.Print(f'             █████╗  ██████╔╝██║██║   ██║█████╗  \n',Colors.cyan_to_green,interval=0.0001)
Write.Print(f'             ██╔══╝  ██╔══██╗██║╚██╗ ██╔╝██╔══╝  \n',Colors.cyan_to_green,interval=0.0001)
Write.Print(f'             ██║     ██║  ██║██║ ╚████╔╝ ███████╗\n',Colors.cyan_to_green,interval=0.0001)
Write.Print(f'             ╚═╝     ╚═╝  ╚═╝╚═╝  ╚═══╝  ╚══════╝\n',Colors.cyan_to_green,interval=0.0001)
print(f' {vang}          Copyright © FRIVE-Tool 2023 {red}|{vang} Version 2.0{trang}')
print(f"      {luc}           Ngày{trang}:{vang}{ngay_hom_nay}{red} |{luc} Tháng{trang}:{vang}{thang_nay} {red}| {luc}Năm{trang}:{vang}{nam_}\n")
print(f"{thanh_xau}{luc} Zalo group{trang}:{vang} https://zalo.me/g/cdcazh320")
print(f"{thanh_xau}{luc} Email{trang}:{vang} fivetool.official@gmail.com")
print(f"{thanh_xau}{luc} Youtube{trang}:{vang} https://www.youtube.com/@TOOLFRIVE{trang}")
print(f'{thanh_xau}{luc} IP hiện tại của bạn là{trang}:{vang} {ip}\n')
print(f"{red}┌─────┬────────────────────────────────────┬─────────┬─────────┐")
print(f"{red}│{vang} STT {red}│    {vang}         MENU TOOL        {red}      │ {vang}STATUS {red} │{vang} VERSION {red}│")
print(f"{red}├─────┼────────────────────────────────────┼─────────┼─────────┤")
print(f"{red}│{vang}  1 {red} │{lam} GET ID FACEBOOK {red}                   │{luc} ONLINE {red} │ {lam} [1.0] {red} │")
print(f"{red}├─────┼────────────────────────────────────┼─────────┼─────────┤")
print(f"{red}│ {vang} 2 {red} │{lam} SPAM SMS & CALL           {red}         │{luc} ONLINE {red} │ {lam} [1.0] {red} │")
print(f"{red}├─────┼────────────────────────────────────┼─────────┼─────────┤")
print(f"{red}│ {vang} 3 {red} │{lam} GET TOKEN PRO5            {red}         │{luc} ONLINE {red} │ {lam} [1.0] {red} │")
print(f"{red}├─────┼────────────────────────────────────┼─────────┼─────────┤")
print(f"{red}│ {vang} 4 {red} │{lam} ADD FRIENDS               {red}         │{luc} ONLINE  {red}│ {lam} [1.0]  {red}│")
print(f"{red}├─────┼────────────────────────────────────┼─────────┼─────────┤")
print(f"{red}│{vang}  5 {red} │{lam} GET TOKEN                 {red}         │{luc} ONLINE {red} │ {lam} [1.0] {red} │")
print(f"{red}├─────┼────────────────────────────────────┼─────────┼─────────┤")
print(f"{red}│ {vang} 6 {red} │{lam} GET COOKIE PRO5           {red}         │{luc} ONLINE {red} │ {lam} [1.0] {red} │")
print(f"{red}├─────┼────────────────────────────────────┼─────────┼─────────┤")
print(f"{red}│ {vang} 7 {red} │{lam} ENC PYTHON                {red}         │{luc} ONLINE {red} │ {lam} [1.0] {red} │")
print(f"{red}├─────┼────────────────────────────────────┼─────────┼─────────┤")
print(f"{red}│ {vang} 8 {red} │{lam} VIEW TIK TOK              {red}         │{luc} ONLINE {red} │ {lam} [1.0] {red} │")
print(f"{red}├─────┼────────────────────────────────────┼─────────┼─────────┤")
print(f"{red}│ {vang} 9 {red} │{lam} SPAM MESS                  {red}        │{luc} ONLINE {red} │ {lam} [1.0] {red} │")
print(f"{red}├─────┼────────────────────────────────────┼─────────┼─────────┤")
print(f"{red}│ {vang} 10 {red}│{lam} QUAY LẠI                  {red}         │{tim}   =.=   {red}│ {lam}  NEXT {red} │")
print(f"{red}└─────┴────────────────────────────────────┴─────────┴─────────┘\n")
chon = input(f"{thanh_dep}{luc}Nhập Lựa Chọn{trang}: ")
os.system("cls" if os.name == "nt" else "clear")
try:
        if chon == '1':
                run = requests.get(f'https://raw.githubusercontent.com/FRIVE-TOOL/FRIVE-TOOL/main/getid.py').text
        elif chon == '2':
                run = requests.get(f'https://raw.githubusercontent.com/FRIVE-TOOL/FRIVE-TOOL/main/spamsmscall.py').text
        elif chon == '3':
                run = requests.get(f'https://raw.githubusercontent.com/FRIVE-TOOL/FRIVE-TOOL/main/gettokenpr5.py').text
        elif chon == '4':
                run = requests.get(f'https://raw.githubusercontent.com/FRIVE-TOOL/FRIVE-TOOL/main/addfen.py').text
        elif chon == '5':
                run = requests.get(f'https://raw.githubusercontent.com/FRIVE-TOOL/FRIVE-TOOL/main/gettoken.py').text
        elif chon == '6':
                run = requests.get(f'https://raw.githubusercontent.com/FRIVE-TOOL/FRIVE-TOOL/main/getcookie.py').text
        elif chon == '7':
                run = requests.get(f'https://raw.githubusercontent.com/FRIVE-TOOL/FRIVE-TOOL/main/enc_dec.py').text
        elif chon == '8':
                run = requests.get(f'https://raw.githubusercontent.com/FRIVE-TOOL/FRIVE-TOOL/main/zyfoy_new.py').text
        elif chon == '9':
                run = requests.get(f'https://raw.githubusercontent.com/FRIVE-TOOL/FRIVE-TOOL/main/spammess.py').text
        elif chon == '10':
                run = requests.get(f'https://raw.githubusercontent.com/FRIVE-TOOL/FRIVE-TOOL/main/gop_key.py').text
        else:
                run = print(f'{lam}Lựa Chọn Không Xác Định{trang}')
except:
        if not is_connected():
                print(f'{lam}Hãy Kiểm Tra Kết Nối Mạng !!! {trang}')
        else:
                print(f'{lam}Sever Gặp Lỗi Hãy Liên Hệ Admin !!! {trang}')
        exit()
exec(run)