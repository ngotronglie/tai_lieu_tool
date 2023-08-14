'''
Deobfuscator by HuyAnh
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
purple = "\e[35m"
hong = "\033[1;95m"
# Đánh dấu bản quyền
thanh_xau= red + "[" + vang+ "⟨⟩" + red + "] " + trang + "➩ "+luc
thanh_dep= red + "[" + luc + "✓" + red + "] " + trang + "➩ "+luc
##### Cài Thư Viện #####
from bs4 import BeautifulSoup
from sys import platform
import re,requests,os,sys
from time import sleep 
import requests, random
import base64, json
from time import sleep,strftime
import uuid
from pystyle import Write,Colors
from datetime import datetime
import datetime
from pystyle import Colors, Colorate
import socket
key_pass = 'FRIVE-TOOL'

def clear ():
    if platform[0:3] == 'lin':
        os.system("clear")
    else:
	    os.system("cls")
            
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

def frive(so):
	a= "────"*so
	for i in range(len(a)):
		sys.stdout.write(a[i])
		sys.stdout.flush()
		sleep(0.003)
	print()
            
def checkkey(key):
    try:
        key_phi = requests.get(f'https://keysieuvip.link/api_key/check.php?key={key}').json()
        if key_phi["status"] == "success":
            return key_phi["name"], key_phi["end"]
        else:
            return [key_phi["msg"]]
    except:
        return False
    
def banner():
      clear()
      t=(f'   {Colorate.Horizontal(Colors.green_to_cyan,   "         ███████╗██████╗ ██╗██╗   ██╗███████╗")} ')
      t_1=(f'   {Colorate.Horizontal(Colors.green_to_cyan, "         ██╔════╝██╔══██╗██║██║   ██║██╔════╝")} ')
      t_2=(f'   {Colorate.Horizontal(Colors.green_to_cyan, "         █████╗  ██████╔╝██║██║   ██║█████╗")}')
      t_3=(f'   {Colorate.Horizontal(Colors.green_to_cyan, "         ██╔══╝  ██╔══██╗██║╚██╗ ██╔╝██╔══╝  ")}')
      t_4=(f'   {Colorate.Horizontal(Colors.green_to_cyan, "         ██║     ██║  ██║██║ ╚████╔╝ ███████╗")}')
      t_5=(f'   {Colorate.Horizontal(Colors.green_to_cyan, "         ╚═╝     ╚═╝  ╚═╝╚═╝  ╚═══╝  ╚══════╝")}')
      t_6=(f'           {Colorate.Horizontal(Colors.green_to_blue, "CopyRight: © FRIVE | Tool Version: 2.0")}\n')
    
      print(t)
      print(t_1)
      print(t_2)
      print(t_3)
      print(t_4)
      print(t_5)
      print(t_6)

clear()
banner()

print(f"{red}┌─────┬────────────────────────────────────┬─────────┬─────────┐")
print(f"{red}│ {vang}STT {red}│             {vang}MENU TOOL              {red}│ {vang}STATUS  {red}│ {vang}VERSION {red}│")
print(f"{red}├─────┼────────────────────────────────────┼─────────┼─────────┤")
print(f"{red}│  {vang}1  {red}│ {lam}TRAODOISUB                         {red}│ {luc}ONLINE  {red}│  {lam}[1.0]  {red}│")
print(f"{red}├─────┼────────────────────────────────────┼─────────┼─────────┤")
print(f"{red}│  {vang}2  {red}│ {lam}TUONGTACCHEO                       {red}│ {luc}ONLINE  {red}│  {lam}[1.0]  {red}│")
print(f"{red}├─────┼────────────────────────────────────┼─────────┼─────────┤")
print(f"{red}│  {vang}3  {red}│ {lam}TIỆN ÍCH                           {red}│ {luc}ONLINE  {red}│  {lam}[1.0]  {red}│")
print(f"{red}├─────┼────────────────────────────────────┼─────────┼─────────┤")
print(f"{red}│  {vang}4  {red}│ {lam}PAGE PROFILE                       {red}│ {luc}ONLINE  {red}│  {lam}[1.0]  {red}│")
print(f"{red}├─────┼────────────────────────────────────┼─────────┼─────────┤")
print(f"{red}│  {vang}5  {red}│ {lam}GOLIKE PE                          {red}│ {luc}ONLINE  {red}│  {lam}[1.0]  {red}│")
print(f"{red}├─────┼────────────────────────────────────┼─────────┼─────────┤")
print(f"{red}│  {vang}6  {red}│ {lam}THOÁT TOOL                         {red}│   {tim}=.=   {red}│   {lam}NEXT  {red}│")
print(f"{red}└─────┴────────────────────────────────────┴─────────┴─────────┘\n")

chon = input(f'{thanh_xau}{luc}NHẬP SỐ{trang}: {vang}')
clear()
try:
	if chon == '1':
		run = requests.get(f'https://raw.githubusercontent.com/FRIVE-TOOL/FRIVE-TOOL/main/tds.py').text
	elif chon == '2':
		run = requests.get(f'https://raw.githubusercontent.com/FRIVE-TOOL/FRIVE-TOOL/main/ttc.py').text
	elif chon == '3':
		run = requests.get(f'https://raw.githubusercontent.com/FRIVE-TOOL/FRIVE-TOOL/main/tienich.py').text
	elif chon == '4':
		run = requests.get(f'https://raw.githubusercontent.com/FRIVE-TOOL/FRIVE-TOOL/main/profile.py').text
	elif chon == '5':
		run = requests.get(f'https://raw.githubusercontent.com/FRIVE-TOOL/FRIVE-TOOL/main/golikepe.py').text
	elif chon == '6':
		run = requests.get(f'https://raw.githubusercontent.com/FRIVE-TOOL/FRIVE-TOOL/main/exit.py').text

	else:
		run = f"{lam}Lựa Chọn Không Xác Định{trang}"
except:
	if not is_connected():
		print(f'{lam}Hãy Kiểm Tra Kết Nối Mạng !!! {trang}')
	else:
		print (f'{lam}Sever Gặp Lỗi Hãy Liên Hệ Admin !!! {trang}')
	exit()
print(run)