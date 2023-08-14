#Deobfuscate by HuyAnh
#Zalo:0905491417
#huyanhnong.21

import requests,os
from time import sleep
class NguyenDucPhatCutePhoMaiQue:
    def getinfotk(self, cookie):
        requests_get_info =  requests.get('https://ndptoolvip-api.tk/api/gettokeneaabw.php?cookie='+cookie).json()
        if requests_get_info['status'] == 'success':
            return requests_get_info
        else:
            return False
    def get_id_cmt(self, idpost, token):
        requests_get = requests.get(f'https://graph.facebook.com/{idpost}/comments?&access_token='+token).json()
        return requests_get
    def rely_comment(self, id_post, mess, img, cookie, token, dem, namechucmt):
        # Code Tool By: NguyenDucPhat.Copyright
        data = {"access_token": token,"message": mess,"attachment_url": img}
        rq_rely = requests.post(f'https://graph.facebook.com/{id_post}/comments', headers={'cookie': cookie},data=data).json()
        if 'id' in rq_rely:
            ID_OK = rq_rely['id']
            print(f'| {dem} | RELY COMMENT THÀNH CÔNG => {ID_OK} => [TK CMT: {namechucmt}]')
        else:
            print(f'| {dem} | RELY COMMENT ERROR => [TK CMT: {namechucmt}]')
def ndp_delay_tool(p):
    while(p>1):
         p=p-1
         print(f'[HDT-TOOL][|][LO......][{p}]','     ',end='\r');sleep(1/6)
         print(f'[HDT-TOOL][/][LOA.....][{p}]','     ',end='\r');sleep(1/6)
         print(f'[HDT-TOOL][-][LOAD....][{p}]','     ',end='\r');sleep(1/6)
         print(f'[HDT-TOOL][+][LOADI...][{p}]','     ',end='\r');sleep(1/6)
         print(f'[HDT-TOOL][\][LOADIN..][{p}]','     ',end='\r');sleep(1/6)
         print(f'[HDT-TOOL][|][LOADING.][{p}]','     ',end='\r');sleep(1/6)
def banner():
    os.system("cls" if os.name == "nt" else "clear")
    banner = '''
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
                  
   \033[1;30m➩ \033[1;33mTOOL \033[1;32mRELY\033[1;31m COMMENT\033[1;34m POST\033[1;35m KÈM\033[1;36m ẢNH
   \033[1;30m➩ \033[1;33mTẠO FILE ➩ \033[1;37mnoidung.txt \033[1;32mTRƯỚC KHI CHẠY TOOL NÀY
\033[1;32m==============================================================
    '''
    print(banner)
banner()
dem=0
while True:
    cookie_fb = input('Vui Lòng Nhập Cookie Tài Khoản Rely Comment: ')
    dpkuti = NguyenDucPhatCutePhoMaiQue()
    checktk = dpkuti.getinfotk(cookie_fb)
    if checktk != False:
        name_fb = checktk['name']
        uid_fb = checktk['id']
        token = checktk['access_token']
        print('─'*50)
        print(f'UID FB: {uid_fb} | NANE FB: {name_fb}')
        print('─'*50)
        if not os.path.exists('noidung.txt'):
            print('Thiếu File noidung.txt Rồi Bro!!')
        else:
            with open('noidung.txt', 'r', encoding='utf-8') as f:
                noidung = f.read()
        if noidung == '':   
            print('Thiếu Dữ Liệu Truyền Vào!!')
        else:
            idpost = input('Vui Lòng Nhập UID Bài Viết: ')
            print('─'*50)
            img = input('Vui Lòng Nhập Link Ảnh: ')
            print('─'*50)
            delay = int(input('Vui Lòng Nhập Delay Rely Comment: '))
            print('─'*50)
            dcmhmm = dpkuti.get_id_cmt(idpost, token)
            for dl in dcmhmm['data']:
                dem=dem+1
                idchucmt = dl['from']['id']
                namechucmt = dl['from']['name']
                id_cmt = dl['id']
                dpkuti.rely_comment(id_cmt, noidung, img, cookie_fb, token, dem, namechucmt)
                ndp_delay_tool(delay)
            input('Done Rely Comment => [ENTER ĐỂ EXIT]')
            exit()
    else:
        print('Cookie Đã Die Or Out Vui Lòng Kiểm Tra Lại!!')
        continue  