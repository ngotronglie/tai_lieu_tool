#deobfuscator by HuyAnh
#Zalo:0905491417
#huyanhnong.21
import requests,random,os,sys
from pystyle import Add, Center, Anime, Colors, Colorate, Write, System
from threading import Thread
def clear():
    if os.name=='nt':os.system('cls')
    else:os.system('clear')
clear()
def banner():
 banner = Colorate.Diagonal(Colors.green_to_white, f"""
╔══════════════════════════════════════════════════════════════╗
║                                                              ║
║ ██╗  ██╗██╗  ██╗ █████╗  ████████╗ ██████╗  ██████╗ ██╗      ║
║ ██║ ██╔╝██║  ██║██╔══██╗ ╚══██╔══╝██╔═══██╗██╔═══██╗██║      ║
║ █████╔╝ ███████║███████║    ██║   ██║   ██║██║   ██║██║      ║
║ ██╔═██╗ ██╔══██║██╔══██║    ██║   ██║   ██║██║   ██║██║      ║
║ ██║  ██╗██║  ██║██║  ██║    ██║   ╚██████╔╝╚██████╔╝███████╗ ║
║ ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝    ╚═╝    ╚═════╝  ╚═════╝ ╚══════╝ ║
║══════════════════════════════════════════════════════════════║
║    Youtube -> Le Kha                                         ║
║    Telegram -> @lechaukhasupport                             ║
║    Zalo Support -> 0912119945                                ║
║    Facebook Support -> www.facebook.com/lechaukha.suppot     ║
║══════════════════════════════════════════════════════════════║
║      Mọi Hướng Dẫn Bạn Cần Đều Nằm Ở Trên Kênh Youtube       ║
║        Le Kha, Vui Lòng Xem Kỹ Hướng Dẫn Và Sử Dụng.         ║
╚══════════════════════════════════════════════════════════════╝
                    GEN MAIL SPEED VIP PRO
════════════════════════════════════════════════════════════════\n------------Nẽu Gen Mail Bị Đứng Thì Hãy Fake IP USA------------\n════════════════════════════════════════════════════════════════\n""")
 for X in banner:
  sys.stdout.write(X)
  sys.stdout.flush() 

headers={'user-agent':'Mozilla/5.0 (Linux; Android 11; Joy 4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.40 Mobile Safari/537.36'}
nuoc=['af_ZA', 'ge', 'ar', 'id_ID', 'az', 'it', 'cz', 'ja', 'de', 'ko', 'de_AT', 'lv', 'de_CH', 'nb_NO', 'el', 'en', 'nl', 'en_AU', 'nl_BE', 'pl', 'pt_BR', 'en_CA', 'pt_PT', 'en_GB', 'ro', 'en_IE', 'ru', 'sk', 'en_US', 'sv', 'en_ZA', 'tr', 'es', 'uk', 'es_MX', 'vi', 'fa', 'zh_CN', 'fr', 'zh_TW', 'fr_CA', 'zu_ZA', 'fr_CH']
banner()
duoi=input(Colorate.Diagonal(Colors.green_to_white, "\nĐuôi Mail [EX-@hotmail.com]: "))
HaHa=input(Colorate.Diagonal(Colors.green_to_white, "File Save Mail: "))
luong=int(input(Colorate.Diagonal(Colors.green_to_white, "Thead: ")))
def daomail():
    while True:
        try:
            luu=''
            data={
    'number':'1000',
    'culture':random.choice(nuoc),
    '__RequestVerificationToken':'CfDJ8Fud5pe4-RhHmVzQ3TlWMhkmfRE2OznEA7IgRl6PRzPhGcDnx897Ql8DiCoJV2DDV7Moa0O8qEL-iV99WqW3coPB_St7QfiiaZUX9cO8zrlbVBUWXjoAhIw8EauhBy9QymoepO_KDiK2JuavbMkVvEA',
    'X-Requested-With':'XMLHttpRequest'
            }
            trave=requests.post('https://randommer.io/random-email-address',headers=headers,data=data).json()
            for RT in trave:
                loz=RT.split('@')[0]
                if len(loz)<5:break
                loz+=f'{duoi}\n'
                luu+=loz
                print(loz,end='')
            open(HaHa,'a+').write(luu)
        except:pass
for WHIST in range(luong):
    Thread(target=daomail).start()