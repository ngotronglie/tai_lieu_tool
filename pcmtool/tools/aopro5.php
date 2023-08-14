 #BẢN QUYỀN CỦA NGUYỄN ĐỨC PHÁT
import requests,random,threading,os,sys,time
from time import strftime
list_token = []
def banner():
    os.system("cls" if os.name == "nt" else "clear")
#Giao Diện ///////////
    banner = '''

  \033[1;36m_______    ____     ____    _      
 |__   __|  / __ \   / __ \  | |     
    | |    | |  | | | |  | | | |     
    | |    | |  | | | |  | | | |     
    | |    | |__| | | |__| | | |____ 
    |_|     \____/   \____/  |______|

       \033[1;33mTOOL SHARE ẢO PRO5 MAX SPEED
\033[1;35m============================================
    '''
    #print(banner)
    for i in banner:
      sys.stdout.write(i)
      sys.stdout.flush()
      time.sleep(0.00130)
class PCM:
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
            print(f'\033[1;93m[\033[1;34mUID SHARE: {idshare}\033[1;93m] \033[1;93m| \033[1;32mTHÀNH CÔNG ')
 #BẢN QUYỀN CỦA NĐP
        else:
            print('\033[1;31mBỊ BOLCK RỒI ĐỢI 24H SAU VÀO CHẠY TIẾP')

banner()
while True:
    cookie = input('\033[1;37m\033[1;3mNHẬP COOKIE FACEBOOK CHỨA PAGE: \033[1;35m')
    dpcute = PCM()
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
        print('\033[1;31mCookie Die Mẹ Rồi Nhập Cl!!')
        continue
id_post = input('\033[1;37mUID BÀI VIẾT BẰNG SỐ CHỨ ĐỪNG NHẬP NGUYÊN CÁI LINK BÀI VIẾT VÀO NHA GET UID RỒI NHẬP VÀO: \033[1;35m')
print('─'*50)
luong = int(input('\033[1;37mNHẬP LUỒNG (CÓ BAO NHIU PAGE THÌ NHẬP BẤY NHIU): \033[1;35m'))
print('─'*50)
getpage = dpcute.getpage(token)
if getpage != False:
    print(f'Đã Tìm Thấy | {len(getpage)} | Page', end='\r')
    for getdl in getpage:
        tokenpagegett = getdl['access_token']
        list_token.append(tokenpagegett)
else:
    print('\033[1;31mKhông Tìm Thấy Page Nào!!')
while True:
    for tokenpage in list_token:
        t = threading.Thread(target=dpcute.run_share,args=(tokenpage, id_post))
        t.start()
        while threading.active_count() > luong:
            t.join()
            