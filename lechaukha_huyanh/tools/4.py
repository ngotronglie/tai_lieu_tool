#deobfuscator by HuyAnh
#Zalo:0905491417
#huyanhnong.21
import os, sys
try:
  from faker import Faker
  from requests import session
  from colorama import Fore, Style
  import requests, random, re
  from pystyle import Add, Center, Anime, Colors, Colorate, Write, System
  from random import randint
except:
  os.system("pip install faker")
  os.system("pip install requests")
  os.system("pip install colorama")
  from faker import Faker
  from requests import session
  from pystyle import Add, Center, Anime, Colors, Colorate, Write, System
  from colorama import Fore, Style
  import requests, random, re
  from random import randint
os.system("clear")

def checkhotmail():
  s = session()
  n_hotmail = 0
  print(Colorate.Diagonal(Colors.green_to_white, '     ╔══════════════════════════════════════════════════════════════╗'))
  print(Colorate.Diagonal(Colors.green_to_white, '     ║                                                              ║'))
  print(Colorate.Diagonal(Colors.green_to_white, '     ║ ██╗  ██╗██╗  ██╗ █████╗  ████████╗ ██████╗  ██████╗ ██╗      ║'))
  print(Colorate.Diagonal(Colors.green_to_white, '     ║ ██║ ██╔╝██║  ██║██╔══██╗ ╚══██╔══╝██╔═══██╗██╔═══██╗██║      ║'))
  print(Colorate.Diagonal(Colors.green_to_white, '     ║ █████╔╝ ███████║███████║    ██║   ██║   ██║██║   ██║██║      ║'))
  print(Colorate.Diagonal(Colors.green_to_white, '     ║ ██╔═██╗ ██╔══██║██╔══██║    ██║   ██║   ██║██║   ██║██║      ║'))
  print(Colorate.Diagonal(Colors.green_to_white, '     ║ ██║  ██╗██║  ██║██║  ██║    ██║   ╚██████╔╝╚██████╔╝███████╗ ║'))
  print(Colorate.Diagonal(Colors.green_to_white, '     ║ ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝    ╚═╝    ╚═════╝  ╚═════╝ ╚══════╝ ║'))
  print(Colorate.Diagonal(Colors.green_to_white, '     ║══════════════════════════════════════════════════════════════║'))
  print(Colorate.Diagonal(Colors.green_to_white, '     ║    Youtube -> Le Kha                                         ║'))
  print(Colorate.Diagonal(Colors.green_to_white, '     ║    Telegram -> @lechaukhasupport                             ║'))
  print(Colorate.Diagonal(Colors.green_to_white, '     ║    Zalo Support -> 0912119945                                ║'))
  print(Colorate.Diagonal(Colors.green_to_white, '     ║    Facebook Support -> www.facebook.com/lechaukha.suppot     ║'))
  print(Colorate.Diagonal(Colors.green_to_white, '     ║══════════════════════════════════════════════════════════════║'))
  print(Colorate.Diagonal(Colors.green_to_white, '     ║      Mọi Hướng Dẫn Bạn Cần Đều Nằm Ở Trên Kênh Youtube       ║'))
  print(Colorate.Diagonal(Colors.green_to_white, '     ║        Le Kha, Vui Lòng Xem Kỹ Hướng Dẫn Và Sử Dụng.         ║'))
  print(Colorate.Diagonal(Colors.green_to_white, '     ╚══════════════════════════════════════════════════════════════╝'))
  print(Colorate.Diagonal(Colors.green_to_white, '                      TOOL LỌC HOTMAIL.COM LIVE/DIE VIP'))
  print(Colorate.Diagonal(Colors.green_to_white, '════════════════════════════════════════════════════════════════════════'))
  hotmail = open(input(Colorate.Diagonal(Colors.green_to_white, "File Mail: "))).readlines()
  hotmail_die = input(Colorate.Diagonal(Colors.green_to_white, "File Save Mail: "))
  os.system('clear')
  for line_hotmail in hotmail:
    n_hotmail += 1
    HotMail = line_hotmail.strip("\n")
    name_hotmail = HotMail[0:HotMail.index("@")]
    DL = s.get("https://signup.live.com/signup?username="+name_hotmail+"@hotmail.com&lic=1")
    kq = re.search("isAvailable",DL.text)
    if kq == None:
      print ("[" + str(n_hotmail) + "] Live -> " + name_hotmail + "@hotmail.com")
    else:
      print ("[" + str(n_hotmail) + "] Die -> " + name_hotmail + "@hotmail.com")
      open(hotmail_die,"a").write(name_hotmail + "@hotmail.com" + "\n")
  process_menu()
def process_menu():
  print(Colorate.Diagonal(Colors.green_to_white, '     ╔══════════════════════════════════════════════════════════════╗'))
  print(Colorate.Diagonal(Colors.green_to_white, '     ║                                                              ║'))
  print(Colorate.Diagonal(Colors.green_to_white, '     ║ ██╗  ██╗██╗  ██╗ █████╗  ████████╗ ██████╗  ██████╗ ██╗      ║'))
  print(Colorate.Diagonal(Colors.green_to_white, '     ║ ██║ ██╔╝██║  ██║██╔══██╗ ╚══██╔══╝██╔═══██╗██╔═══██╗██║      ║'))
  print(Colorate.Diagonal(Colors.green_to_white, '     ║ █████╔╝ ███████║███████║    ██║   ██║   ██║██║   ██║██║      ║'))
  print(Colorate.Diagonal(Colors.green_to_white, '     ║ ██╔═██╗ ██╔══██║██╔══██║    ██║   ██║   ██║██║   ██║██║      ║'))
  print(Colorate.Diagonal(Colors.green_to_white, '     ║ ██║  ██╗██║  ██║██║  ██║    ██║   ╚██████╔╝╚██████╔╝███████╗ ║'))
  print(Colorate.Diagonal(Colors.green_to_white, '     ║ ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝    ╚═╝    ╚═════╝  ╚═════╝ ╚══════╝ ║'))
  print(Colorate.Diagonal(Colors.green_to_white, '     ║══════════════════════════════════════════════════════════════║'))
  print(Colorate.Diagonal(Colors.green_to_white, '     ║    Youtube -> Le Kha                                         ║'))
  print(Colorate.Diagonal(Colors.green_to_white, '     ║    Telegram -> @lechaukhasupport                             ║'))
  print(Colorate.Diagonal(Colors.green_to_white, '     ║    Zalo Support -> 0912119945                                ║'))
  print(Colorate.Diagonal(Colors.green_to_white, '     ║    Facebook Support -> www.facebook.com/lechaukha.suppot     ║'))
  print(Colorate.Diagonal(Colors.green_to_white, '     ║══════════════════════════════════════════════════════════════║'))
  print(Colorate.Diagonal(Colors.green_to_white, '     ║      Mọi Hướng Dẫn Bạn Cần Đều Nằm Ở Trên Kênh Youtube       ║'))
  print(Colorate.Diagonal(Colors.green_to_white, '     ║        Le Kha, Vui Lòng Xem Kỹ Hướng Dẫn Và Sử Dụng.         ║'))
  print(Colorate.Diagonal(Colors.green_to_white, '     ╚══════════════════════════════════════════════════════════════╝'))
  print(Colorate.Diagonal(Colors.green_to_white, '                      TOOL LỌC HOT.COM LIVE/DIE VIP'))
  print(Colorate.Diagonal(Colors.green_to_white, '════════════════════════════════════════════════════════════════════════'))
  os.system('clear')
  checkhotmail()
  quit()
  if choice_user != '1':
    process_menu()
  if choice_user == '1':
    process_menu()
process_menu()