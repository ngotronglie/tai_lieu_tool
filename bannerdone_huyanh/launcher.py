from time import strftime
import os
import sys
import requests
import json
from time import sleep
from datetime import datetime, timedelta
import base64
import requests
import os
import time
# màu
xnhac = "\033[1;36m"
do = "\033[1;31m"
luc = "\033[1;32m"
vang = "\033[1;33m"
xduong = "\033[1;34m"
tim = '\033[1;39m'
hong = "\033[1;35m"
trang = "\033[1;37m"
whiteb = "\033[1;37m"
red = "\033[0;31m"
redb = "\033[1;31m"
end = '\033[0m'
os.system("cls" if os.name == "nt" else "clear")

# đánh dấu bản quyền
ndp_tool = "\033[1;31m[\033[1;37m=.=\033[1;31m] \033[1;37m=>  "
thanh = "\033[1;37m- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -"

ip = requests.get("https://api.ipgeolocation.io/getip").json()
def banner():
    banner = f"""

\033[1;97m= = = = = = = = = = = = = = = = = = = = = = = = = = = = = 
\033[1;39m┌────────────────────── \033[2;32mNguyễn Minh Hoàng + Phan Hưng  \033[1;39m────────────────────┐
\033[1;32m║   \033[1;39mPYTHON VERSION\033[0;37m     :\033[0;33m   2.5                                 \033[1;32m║
\033[1;32m║   \033[1;39mZALO\033[1;33m ADMIN         \033[1;37m:  0706670417\033[1;31m + \033[1;37m0827827016              \033[1;32m║
          ║   \033[1;39mbox zalo hỗ trợ\033[1;33m \033[1;37m:  https://zalo.me/g/yleaqz769
          ║   \033[1;39mmới update tool shareaopro5 max speed
\033[1;39m└──────────────────────────────────────────────────────────────┘
\033[1;97m= = = = = = = = = = = = = = = = = = = = = = = = = = = = = 
\033[1;31m────────────────────────────────────────────────────────────
"""

    for X in banner:
        sys.stdout.write(X)
        sys.stdout.flush()
        sleep(0.00125)
banner()
ngay=int(strftime('%d'))
key1=str(ngay*5868756+74356421)
key = 'hoangtool'+key1
if not os.path.exists('key_hoangtool.txt'):
    url = 'http://keytoolhoangfree.x10.mx/key.html?key='+key
    token_web1s = '27d5d10f-ef8d-4d88-9364-4ede0ebfd784'
    web1s = requests.get(f'https://web1s.com/api?token={token_web1s}&url={url}').json()
    if web1s['status']=="error": 
        print(web1s['message'])
        quit()
    else:
        link_key=web1s['shortenedUrl']
    print ("\033[1;33mTool Free Nên Sẽ Đổi Key Mỗi Ngày\033[1;33m")
    print ("\033[1;35m ============================================  ")
    print('\033[1;36mVượt Link Để Lấy Key Free: \033[1;37m'+link_key)
    keynhap = input('\033[1;34mKey Đã Vượt Là: \033[1;33m')
    with open('key_hoangtool.txt', 'w') as f:
        f.write(keynhap)
    
with open('key_hoangtool.txt', 'r') as f:
   keynhap = f.read()
   
if keynhap == key:
  nhap = ("""\033[1;36m>\033[1;31m>\033[1;37m> \033[1;32mKey Đúng Và Đã Được Lưu 
\033[1;31m➩\033[1;32m Chúc Bạn Chạy Tool Vui Vẻ \033[1;35.....""")
  for i in nhap:
    sys.stdout.write(i)
    sys.stdout.flush()
    time.sleep(0.02)
else:
  print('\033[1;37mKey Sai Hoặc Đã Hết Hạn Vui Lòng Khởi Động Lại Tool Và Vượt Link Lại \033[1;31m!!!\n')
  os.remove('key_hoangtool.txt')
  quit()
os.system("cls" if os.name == "nt" else "clear")
banner()
print("\033[1;35m╔════════════════════════════════════════════════════════╗")
print(f"\033[1;34m║ \033[1;33mip của bạn là: {ip['ip']}  \033[1;35m║")
print("\033[1;34m╚════════════════════════════════════════════════════════╝")
print("\033[1;31m────────────────────────────────────────────────────────────")
print("\033[1;37m╔═════════════════════╗")
print("\033[1;37m║  \033[1;33mTool Trao Đổi Sub  \033[1;37m║")
print("\033[1;37m╚═════════════════════╝")
print("\033[1;31m[\033[1;37m=.=\033[1;31m] \033[1;37m=> \033[1;32mNhập Số \033[1;31m[\033[1;33m1\033[1;31m] \033[1;32mTool TDS FB FULL JOD ")       
print("\033[1;31m[\033[1;37m=.=\033[1;31m] \033[1;37m=> \033[1;32mNhập Số \033[1;31m[\033[1;33m2\033[1;31m] \033[1;32mTool TDS FB VIP")

print("\033[1;31m[\033[1;37m=.=\033[1;31m] \033[1;37m=> \033[1;32mNhập Số \033[1;31m[\033[1;33m3\033[1;31m] \033[1;32mTool TDS Pro5 [chưa fix] ")   
print("\033[1;31m[\033[1;37m=.=\033[1;31m] \033[1;37m=> \033[1;32mNhập Số \033[1;31m[\033[1;33m4\033[1;31m] \033[1;32mTool TDS IG \033[1;31m[\033[1;33mV1\033[1;31m] ")

print("\033[1;31m[\033[1;37m=.=\033[1;31m] \033[1;37m=> \033[1;32mNhập Số \033[1;31m[\033[1;33m5\033[1;31m] \033[1;32mTool TDS TikTok & TDS TIKTOK NOW ")

print("\033[1;31m────────────────────────────────────────────────────────────")
print("\033[1;37m╔═══════════════════════╗")
print("\033[1;37m║  \033[1;33mTool Tương Tác Chéo  \033[1;37m║")
print("\033[1;37m╚═══════════════════════╝")
print("\033[1;31m[\033[1;37m=.=\033[1;31m] \033[1;37m=> \033[1;32mNhập Số \033[1;31m[\033[1;33m6\033[1;31m] \033[1;32mTool TTC TikTok [chưa fix] ") 
print("\033[1;31m[\033[1;37m=.=\033[1;31m] \033[1;37m=> \033[1;32mNhập Số \033[1;31m[\033[1;33m7\033[1;31m] \033[1;32mTool TTC Pro5 ")

print("\033[1;31m────────────────────────────────────────────────────────────")
print("\033[1;37m╔═════════════════════╗")
print("\033[1;37m║  \033[1;33mTool Tiện Ích      \033[1;37m║")
print("\033[1;37m╚═════════════════════╝")
print("\033[1;31m[\033[1;37m=.=\033[1;31m] \033[1;37m=> \033[1;32mNhập Số \033[1;31m[\033[1;33m8\033[1;31m] \033[1;32mTool Đào Mail ")
print("\033[1;31m[\033[1;37m=.=\033[1;31m] \033[1;37m=> \033[1;32mNhập Số \033[1;31m[\033[1;33m9\033[1;31m] \033[1;32mTool Tạo Thẻ Thanh Toán ")    
print("\033[1;31m[\033[1;37m=.=\033[1;31m] \033[1;37m=> \033[1;32mNhập Số \033[1;31m[\033[1;33m10\033[1;31m] \033[1;32mTool Check Valid")
print("\033[1;31m[\033[1;37m=.=\033[1;31m] \033[1;37m=> \033[1;32mNhập Số \033[1;31m[\033[1;33m11\033[1;31m] \033[1;32mTool Check Ngày Tạo Acc FB") 
print("\033[1;31m[\033[1;37m=.=\033[1;31m] \033[1;37m=> \033[1;32mNhập Số \033[1;31m[\033[1;33m12\033[1;31m] \033[1;32mTool Spam-sms [lỏ chưa fix] ")

print("\033[1;31m────────────────────────────────────────────────────────────")
print("\033[1;37m╔═════════════════════╗")
print("\033[1;37m║  \033[1;33mTool PROFILE       \033[1;37m║")
print("\033[1;37m╚═════════════════════╝")
print("\033[1;31m[\033[1;37m=.=\033[1;31m] \033[1;37m=> \033[1;32mNhập Số \033[1;31m[\033[1;33m13\033[1;31m] \033[1;32msharefb bằng pro5 [đã sài được] ")
print("\033[1;31m[\033[1;37m=.=\033[1;31m] \033[1;37m=> \033[1;32mNhập Số \033[1;31m[\033[1;33m14\033[1;31m] \033[1;32mTool Reg Page Pro5 \033[1;31m[\033[1;33mV2\033[1;31m]")
print("\033[1;31m[\033[1;37m=.=\033[1;31m] \033[1;37m=> \033[1;32mNhập Số \033[1;31m[\033[1;33m15\033[1;31m] \033[1;32mTOOL TĂNG SHARE AO BẰNG TOKEN")
print("\033[1;31m[\033[1;37m=.=\033[1;31m] \033[1;37m=> \033[1;32mNhập Số \033[1;31m[\033[1;33m16\033[1;31m] \033[1;32mTool Buff View Story Max Speed Pro5 [mới update] ")
print("\033[1;31m[\033[1;37m=.=\033[1;31m] \033[1;37m=> \033[1;32mNhập Số \033[1;31m[\033[1;33m17\033[1;31m] \033[1;32mtool spam sms\033[1;31m[\033[1;33mV5\033[1;31m] ")

print("\033[1;31m────────────────────────────────────────────────────────────")
print("\033[1;37m╔═════════════════════╗")
print("\033[1;37m║  \033[1;33mTool mới cập nhật  \033[1;37m║")
print("\033[1;37m╚═════════════════════╝")
print("\033[1;31m[\033[1;37m=.=\033[1;31m] \033[1;37m=> \033[1;32mNhập Số \033[1;31m[\033[1;33m18\033[1;31m] \033[1;32mtool lọc proxy\033[1;31m『\033[1;33mNEW\033[1;31m』 ")
print("\033[1;31m[\033[1;37m=.=\033[1;31m] \033[1;37m=> \033[1;32mNhập Số \033[1;31m[\033[1;33m19\033[1;31m] \033[1;32mtool buff view tiktok\033[1;31m『\033[1;33mNEW\033[1;31m』 ")
print("\033[1;31m[\033[1;37m=.=\033[1;31m] \033[1;37m=> \033[1;32mNhập Số \033[1;31m[\033[1;33m00\033[1;31m] \033[1;32mThoát Tool")
print("\033[1;31m────────────────────────────────────────────────────────────")

chon = int(input('\033[1;31m[\033[1;37m=.=\033[1;31m] \033[1;37m=> \033[1;32mNhập Số \033[1;37m: \033[1;33m'))
#tool tds
if chon == 1 :
    exec(requests.get('http://keytoolhoangfree.x10.mx/tool_python/tdsfulljob1.php').text) 
if chon == 2:
    exec(requests.get('http://keytoolhoangfree.x10.mx/tool_python/tdsfbvip2.php').text)
if chon == 3 :
    exec(requests.get('http://keytoolhoangfree.x10.mx/tool_python/tdspr53.php').text) 
if chon == 4 :
    exec(requests.get('http://keytoolhoangfree.x10.mx/tool_python/tdsin4.php').text) 
elif chon == 5 : 
 exec(requests.get('http://keytoolhoangfree.x10.mx/tool_python/tdstiktok5.php').text) 
 #tool ttc
if chon == 6 :
    exec(requests.get('http://keytoolhoangfree.x10.mx/tool_python/ttctiktok6.php').text)
if chon == 7 :
    exec(requests.get('http://keytoolhoangfree.x10.mx/tool_python/ttcpro57.php').text)
#tool công cụ 
elif chon == 8 :
 exec(requests.get('http://keytoolhoangfree.x10.mx/tool_python/daomail8.php').text)
elif chon == 9 :
 exec(requests.get('http://keytoolhoangfree.x10.mx/tool_python/taottt9.php').text)
if chon == 10 :
    exec(requests.get('http://keytoolhoangfree.x10.mx/tool_python/checkvalid10.php').text)
if chon == 11 :
    exec(requests.get('http://keytoolhoangfree.x10.mx/tool_python/checkntaoaccfb11.php').text)
if chon == 12 :
    exec(requests.get('http://keytoolhoangfree.x10.mx/tool_python/spamsms12.php').text)
if chon == 13 :
    exec(requests.get('http://keytoolhoangfree.x10.mx/tool_python/sharefb13.php').text)
if chon == 14 :
    exec(requests.get('http://keytoolhoangfree.x10.mx/tool_python/regpro514.php').text)
if chon == 15 :
    exec(requests.get('http://keytoolhoangfree.x10.mx/tool_python/shareaotoken15.php').text)
if chon == 16 :
    exec(requests.get('http://keytoolhoangfree.x10.mx/tool_python/viewstory16.php').text)
if chon == 17 :
    exec(requests.get('http://keytoolhoangfree.x10.mx/tool_python/spamsms17.php').text)
if chon == 18 :
    exec(requests.get('http://keytoolhoangfree.x10.mx/tool_python/locproxy18.php').text)
if chon == 19 :
    exec(requests.get('http://keytoolhoangfree.x10.mx/tool_python/viewtik19.php').text)
if chon == 00 :
    exec(requests.get('http://keytoolhoangfree.x10.mx/tool_python/thoattool00.php').text)
else :
     exit()