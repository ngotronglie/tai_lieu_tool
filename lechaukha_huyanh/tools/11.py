#deobfuscator by HuyAnh
#Zalo:0905491417
#huyanhnong.21
import requests, sys, os
from pystyle import Add, Center, Anime, Colors, Colorate, Write, System
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
                    TOOL GEN PROXY [LIVE 80%]
════════════════════════════════════════════════════════════════""")
 for X in banner:
  sys.stdout.write(X)
  sys.stdout.flush() 
def gen():
  banner()
  print(Colorate.Diagonal(Colors.green_to_white, "\n1.http"))
  print(Colorate.Diagonal(Colors.green_to_white, "2.socks4"))
  print(Colorate.Diagonal(Colors.green_to_white, "3.socks5"))
  print(Colorate.Diagonal(Colors.green_to_white, "════════════════════════════════════════════════════════════════"))
  loai = input(Colorate.Diagonal(Colors.green_to_white, "Nhập Loại Proxy Muốn Gen: "))
  so = input(Colorate.Diagonal(Colors.green_to_white, "Nhập Số Lượn: "))
  luu = input(Colorate.Diagonal(Colors.green_to_white, "File Save Proxy: "))
  params = {
      'request': 'displayproxies',
      'protocol': loai,
      'timeout': so,
      'country': 'all',
      'ssl': 'all',
      'anonymity': 'all',
  }
  
  response = requests.get('https://api.proxyscrape.com/v2/', params=params).text
  print(response)
  open(luu,'a').write(response)
gen()