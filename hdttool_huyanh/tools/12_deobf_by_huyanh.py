#Deobfuscate by HuyAnh
#Zalo:0905491417
#huyanhnong.21

import requests, re, os
from time import sleep
# Count 
dem=0
# =========================== [ CLASS + FUNCTION TOOL ] ===========================
class NguyenDucPhat_Activated_Page:
    def banner(self):
        os.system("cls" if os.name == "nt" else "clear")
        banner = '''
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
\033[1;31m[\033[1;32m⟨⟩\033[1;31m]\033[1;33m ➩\033[1;32m [  𝚃𝙾𝙾𝙻 𝙺𝙸́𝙲𝙷 𝙷𝙾𝙰̣𝚃 𝙿𝙰𝙶𝙴 𝙿𝚁𝙾𝟻 𝚅𝙸𝙿 𝙿𝚁𝙾 - 𝚅𝙴𝚁𝚂𝙸𝙾𝙽 𝟷.0  ]
\033[1;31m[\033[1;32m⟨⟩\033[1;31m]\033[1;33m ➩ \033[1;32m══\x1b[1;91m══\033[1;32m══\033[1;31m══\x1b[1;94m══\x1b[1;96m══\x1b[1;91m══\033[1;32m══\033[1;31m══\x1b[1;94m══\x1b[1;96m══\x1b[1;91m══\033[1;32m═══\033[1;31m══\x1b[1;94m══\x1b[1;96m══\x1b[1;91m══\033[1;32m══\033[1;31m══\x1b[1;94m══\x1b[1;96m══\x1b[1;91m══\033[1;32m══\033[1;31m══\x1b[1;94m══
'''
        print(banner)
    def ndp_delay_tool(self, p):
        while(p>1):
            p=p-1
            print(f'[𖥕 HDT - TOOL 𖥕][|][LO......][{p}]','     ',end='\r');sleep(1/6)
            print(f'[𖥕 HDT - TOOL 𖥕][/][LOA.....][{p}]','     ',end='\r');sleep(1/6)
            print(f'[𖥕 HDT - TOOL 𖥕][-][LOAD....][{p}]','     ',end='\r');sleep(1/6)
            print(f'[𖥕 HDT - TOOL 𖥕][+][LOADI...][{p}]','     ',end='\r');sleep(1/6)
            print(f'[𖥕 HDT - TOOL 𖥕][\][LOADIN..][{p}]','     ',end='\r');sleep(1/6)
            print(f'[𖥕 HDT - TOOL 𖥕][|][LOADING.][{p}]','     ',end='\r');sleep(1/6)
    def GetThongTinFacebook(self, cookie: str):
        headers_get = {'authority': 'www.facebook.com','accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','accept-language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5','sec-ch-prefers-color-scheme': 'light','sec-ch-ua': '"Not?A_Brand";v="8", "Chromium";v="108", "Google Chrome";v="108"','sec-ch-ua-mobile': '?0','sec-ch-ua-platform': '"Windows"','sec-fetch-dest': 'document','sec-fetch-mode': 'navigate','sec-fetch-site': 'none','sec-fetch-user': '?1','upgrade-insecure-requests': '1','user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36','viewport-width': '1184','cookie': cookie}
        try:
            # print("Đang Check Live Cookie...", end="\r")
            url_profile = requests.get('https://www.facebook.com/me', headers = headers_get).url
            get_dulieu_profile = requests.get(url = url_profile, headers = headers_get).text
        except:
            return {'status': 'error', 'message':'Get Dữ Liệu Thất Bại Vui Lòng Kiểm Tra Lại!!'}
        try:
            uid_get = cookie.split('c_user=')[1].split(';')[0]
            name_get = get_dulieu_profile.split('<h1 class="x1heor9g x1qlqyl8 x1pd3egz x1a2a7pz">')[1].split('</h1>')[0]
            fb_dtsg_get = get_dulieu_profile.split('{"name":"fb_dtsg","value":"')[1].split('"},')[0]
            jazoest_get = get_dulieu_profile.split('{"name":"jazoest","value":"')[1].split('"},')[0]
            lsd = get_dulieu_profile.split('["LSD",[],{"token":"')[1].split('"},')[0]
            return {'status':'success', 'name': name_get, 'id': uid_get, 'fb_dtsg': fb_dtsg_get, 'jazoest': jazoest_get, 'lsd': lsd}
        except:
            try:
                uid_get = cookie.split('c_user=')[1].split(';')[0]
                name_get = get_dulieu_profile.split('<h1 class="x1heor9g x1qlqyl8 x1pd3egz x1a2a7pz">')[1].split('</h1>')[0]
                fb_dtsg_get = get_dulieu_profile.split(',"f":"')[1].split('","l":null}')[0]
                jazoest_get = get_dulieu_profile.split('&jazoest=')[1].split('","e":"')[0]
                lsd = get_dulieu_profile.split('["LSD",[],{"token":"')[1].split('"},')[0]
                return {'status':'success', 'name': name_get, 'id': uid_get, 'fb_dtsg': fb_dtsg_get, 'jazoest': jazoest_get, 'lsd': lsd}
            except:
                return {'status': 'error', 'message':'Get Dữ Liệu Thất Bại Vui Lòng Kiểm Tra Lại!!'}
    def GetPageDie(self, cookie: str):
        # Nhận Code Thuê Theo Yêu Cầu Zalo: 0396735565 - NguyenDucPhat
        headers_getpage = {'authority': 'www.facebook.com','accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7','accept-language': 'vi,fr-FR;q=0.9,fr;q=0.8,en-US;q=0.7,en;q=0.6','cache-control': 'max-age=0','sec-ch-prefers-color-scheme': 'light','sec-ch-ua': '"Google Chrome";v="113", "Chromium";v="113", "Not-A.Brand";v="24"','sec-ch-ua-full-version-list': '"Google Chrome";v="113.0.5672.174", "Chromium";v="113.0.5672.174", "Not-A.Brand";v="24.0.0.0"','sec-ch-ua-mobile': '?0','sec-ch-ua-platform': '"Windows"','sec-ch-ua-platform-version': '"10.0.0"','sec-fetch-dest': 'document','sec-fetch-mode': 'navigate','sec-fetch-site': 'same-origin','sec-fetch-user': '?1','upgrade-insecure-requests': '1','user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36','viewport-width': '1585','cookie': cookie}
        try:
            get_data = requests.get('https://www.facebook.com/pages/?category=your_pages&ref=bookmarks', headers=headers_getpage).text
            data = re.findall('","uri_token":".*?","profilePic40"',get_data)
            if data == []:
                return {'status': 'error', 'message':'Không Tìm Thấy Page Die Nào!!'}
            else:
                return {'status': 'success', 'data': data, 'count': len(data)}
        except:
            return {'status': 'error', 'message':'Get Page Die Thấy Bại. Vui Lòng Kiểm Tra Lại Tài Khoản'}
    def Activated_Page(self, cookie: str, fb_dtsg: str, jazoest: str, lsd: str, uid_page_die):
        global dem
        
        headers_activated = {'authority': 'www.facebook.com','accept': '*/*','accept-language': 'vi,fr-FR;q=0.9,fr;q=0.8,en-US;q=0.7,en;q=0.6','content-type': 'application/x-www-form-urlencoded','origin': 'https://www.facebook.com','referer': 'https://www.facebook.com/pages/?category=your_pages&ref=bookmarks','sec-ch-prefers-color-scheme': 'light','sec-ch-ua': '"Google Chrome";v="113", "Chromium";v="113", "Not-A.Brand";v="24"','sec-ch-ua-full-version-list': '"Google Chrome";v="113.0.5672.174", "Chromium";v="113.0.5672.174", "Not-A.Brand";v="24.0.0.0"','sec-ch-ua-mobile': '?0','sec-ch-ua-platform': '"Windows"','sec-ch-ua-platform-version': '"10.0.0"','sec-fetch-dest': 'empty','sec-fetch-mode': 'cors','sec-fetch-site': 'same-origin','user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36','viewport-width': '1585','x-asbd-id': '129477','x-fb-friendly-name': 'ReactivateProfileMutation','x-fb-lsd': lsd,'cookie': cookie}
        data_activated = {'fb_dtsg': fb_dtsg,'jazoest': jazoest,'lsd': lsd,'__spin_r': '1007848011','__spin_b': 'trunk','__spin_t': '1689490220','fb_api_caller_class': 'RelayModern','fb_api_req_friendly_name': 'ReactivateProfileMutation','variables': '{"profile_id":"'+uid_page_die+'","delegate_page_id":null}','server_timestamps': 'true','doc_id': '6365256943526229'}
        Json_Activated_Page = requests.post('https://www.facebook.com/api/graphql/', headers=headers_activated, data=data_activated).json()
        try:
            dem+=1
            print(f'[𖥕 HDT - TOOL 𖥕] | {dem} | 𝙰𝙲𝚃𝙸𝚅𝙰𝚃𝙴𝙳_𝙿𝙰𝙶𝙴_𝚂𝚄𝙲𝙲𝙴𝚂𝚂 | 𝚃𝚊̀𝚒 𝙺𝚑𝚘𝚊̉𝚗: '+Json_Activated_Page['data']['reactivate_profile']['name']+'] | 𝚄𝙸𝙳 𝙵𝙱: '+Json_Activated_Page['data']['reactivate_profile']['id']+']')
        except:
            print(f'[𖥕 HDT - TOOL 𖥕] | {dem} | 𝙰𝙲𝚃𝙸𝚅𝙰𝚃𝙴𝙳_𝙿𝙰𝙶𝙴_𝙴𝚁𝚁𝙾𝚁 | [𝚄𝙸𝙳_𝙿𝙰𝙶𝙴: {uid_page_die}]')
# =========================== [ START TOOL ] ===========================         
NgDucPhat_Tool = NguyenDucPhat_Activated_Page()
NgDucPhat_Tool.banner()
while True:
    cookie = input('𝚅𝚄𝙸 𝙻𝙾̀𝙽𝙶 𝙽𝙷𝙰̣̂𝙿 𝙲𝙾𝙾𝙺𝙸𝙴 𝙵𝙰𝙲𝙴𝙱𝙾𝙾𝙺: ')
    if cookie != '':
        break
    continue
# Setting Config
NgDucPhat_Tool.banner()
delay = int(input('𝚅𝚄𝙸 𝙻𝙾̀𝙽𝙶 𝙽𝙷𝙰̣̂𝙿 𝙳𝙴𝙻𝙰𝚈 𝙺𝙸́𝙲𝙷 𝙷𝙾𝙰̣𝚃 𝚃𝚁𝙰𝙽𝙶: '))
Check_Live_Account = NgDucPhat_Tool.GetThongTinFacebook(cookie)
if Check_Live_Account['status'] != 'error':
    name = Check_Live_Account['name']
    uid = Check_Live_Account['id']
    fb_dtsg = Check_Live_Account['fb_dtsg']
    jazoest = Check_Live_Account['jazoest']
    lsd = Check_Live_Account['lsd']
    print('─'*50)
    print('𝚃𝚊̀𝚒 𝙺𝚑𝚘𝚊̉𝚗: {0} | 𝚄𝙸𝙳 𝙵𝙱: {1}'.format(name,uid))
    print('─'*50)
    Check_Count_Page = NgDucPhat_Tool.GetPageDie(cookie)
    print('Đã Tìm Thấy: '+str(Check_Count_Page['count'])+'𝙿𝙰𝙶𝙴 𝙿𝚁𝙾𝟻 𝙲𝙰̂̀𝙽 𝙺𝙸́𝙲𝙷 𝙷𝙾𝙰̣𝚃', end='\r')
    for data_trang in Check_Count_Page['data']:
        uid_page_die = data_trang.replace('","uri_token":"','').replace('","profilePic40"','')
        NgDucPhat_Tool.Activated_Page(cookie, fb_dtsg, jazoest, lsd, uid_page_die)
        NgDucPhat_Tool.ndp_delay_tool(delay)
else:
    print(Check_Live_Account['message'])