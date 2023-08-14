import requests,os,sys, time
#Color
trang = "\033[1;37m"
xanh_la = "\033[1;32m"
xanh_duong = "\033[1;34m"
do = "\033[1;31m"
vang = "\033[1;33m"
tim = "\033[1;35m"
xanhnhat = "\033[1;36m"
# Lmao
thanh_xau=trang+'~'+do+'['+vang+'⟨⟩'+do+'] '+trang+'➩  '+xanhnhat
thanh_dep=trang+'~'+do+'['+xanh_la+'✓'+do+'] '+trang+'➩  '+xanhnhat

def banner():
        os.system("cls" if os.name == "nt" else "clear")
        banner = '''
       \033[1;31;48m########   ######  ##     ##
       \033[1;36;48m##     ## ##    ## ###   ###
       \033[1;37;48m##     ## ##       #### ####
       \033[1;34;48m########  ##       ## ### ##
       \033[1;32;48m##        ##       ##     ##
       \033[1;33;48m##        ##    ## ##     ##
       \033[1;35;48m##         ######  ##     ##


\033[1;35m= = = = = = = = = = = = = = = = = = = = = = = = = = = = =
\033[1;39m┌────────────────── TOOL GỘP 16 CHẾ ĐỘ ──────────────────┐
\033[1;32m║   \033[1;39mAMIN               :  \033[1;32mCHÍ MUM   \033[1;31m+   \033[1;32mVĂN LINH         \033[1;32m║
\033[1;32m║   \033[1;39mZALO               :  zalo.me/84834617174            \033[1;32m║
\033[1;32m║   \033[1;37mWEBSITE            :      SUBRE62.COM                \033[1;32m║
\033[1;32m║   \033[1;37mWEBSITE            :      SUBVIPS1.CLICK             \033[1;32m║
\033[1;32m║   \033[1;39mPYTHON VERSION     :      3.2                        \033[1;32m║
\033[1;39m└────────────────────────────────────────────────────────┘
\033[1;35m= = = = = = = = = = = = = = = = = = = = = = = = = = = = =
\033[1;37m──────────────────────────────────────────────────────────
 \033[1;31m➩  \033[1;37mTHÔNG BÁO
 \033[1;31m* \033[1;37mVừa Update Tds Bằng Pro5 Đa Luồng Full Job
 \033[1;31m* \033[1;37mVừa Update Tự Động Lưu Trữ Key 24h
\033[1;37m───────────────────────────────────────────────────────────
        '''
        for i in banner:
          sys.stdout.write(i)
          sys.stdout.flush()
          time.sleep(0.00130)
banner()
from time import strftime
ngay=int(strftime('%d'))
key1=str(ngay*24032006+74321)
key = 'PCMTOOL'+key1
#os.system("cls" if os.name == "nt" else "clear")
if not os.path.exists('keypcmtool.txt'):
    url = 'http://keyfree24h.ddns.net/key.html?key='+key
    token_web1s = '22d4da6a-1cf8-42ac-8b40-2099478b3373'
    web1s = requests.get(f'https://web1s.com/api?token={token_web1s}&url={url}').json()
    if web1s['status']=="error":
        print(web1s['message'])
        quit()
    else:
        link_key=web1s['shortenedUrl']
    print ("\033[1;33mTool Free Nên Sẽ Đổi Key Mỗi Ngày\033[1;33m")
    print ("\033[1;35m ============================================  ")
    print('\033[1;36mVượt Link Để Lấy Key Free: \033[1;37m'+link_key)
    keynhap = input('\033[1;34mKey Đã Vượt Là: \033[1;33m')
    with open('keypcmtool.txt', 'w') as f:
        f.write(keynhap)

with open('keypcmtool.txt', 'r') as f:
   keynhap = f.read()

if keynhap == key:
  nhap = ('\033[1;36m>\033[1;31m>\033[1;37m> \033[1;32mKey Đúng Và Đã Được Lưu Trữ Trong 24h \033[1;31m➩\033[1;32m Chúc Bạn Chạy Tool Vui Vẻ \033[1;36m<\033[1;31m<\033[1;37m<\033[1;35.....')
  for i in nhap:
    sys.stdout.write(i)
    sys.stdout.flush()
    time.sleep(0.03)
else:
  print('\033[1;37mKey Sai Hoặc Đã Hết Hạn Vui Lòng Khởi Động Lại Tool Và Vượt Link Lại \033[1;31m!!!\n')
  os.remove('keypcmtool.txt')
  quit()
banner()
print(f"""
{tim}┏━━━━━━━━━━━━━━━━━━━━━━━┓
{tim}┃   {vang}Tool Trao Đổi Sub   {do}┃
{do}┗━━━━━━━━━━━━━━━━━━━━━━━┛ """)
print('\033[1;37m>>> '+do+'['+vang+'1'+do+'] '+xanhnhat+'Tool TDS Cookie Fb '+do+'['+vang+'Đa Cookie'+do+']')
print('\033[1;37m>>> '+do+'['+vang+'1.1'+do+'] '+xanhnhat+'Tool TDS Pro5 Đa Luồng Full Job '+do+'['+vang+'New Update'+do+']')
print(do+'─'*50)
print(f"""
{tim}┏━━━━━━━━━━━━━━━━━━━━━━━┓
{tim}┃  {vang}Tool Tương Tác Chéo  {do}┃
{do}┗━━━━━━━━━━━━━━━━━━━━━━━┛ """)
print('\033[1;37m>>> '+do+'['+vang+'2'+do+'] '+xanhnhat+'Tool Tương Tác Chéo Pro5 '+do+'['+vang+'Bảo Trì'+do+']')
print(do+'─'*50)
print(f"""{tim}┏━━━━━━━━━━━━━━━━━━━┓
{tim}┃   {vang}Tool Facbook   {do} ┃
{do}┗━━━━━━━━━━━━━━━━━━━┛ """)
print('\033[1;37m>>> '+do+'['+vang+'3'+do+'] '+xanhnhat+'Tool Reg Pro5 + Úp Avt '+do+'['+vang+'Đa Luồng'+do+']')
print('\033[1;37m>>> '+do+'['+vang+'4'+do+'] '+xanhnhat+'Tool Kích Hoạt Page Pro5 Bị Ẩn '+do+'['+vang+'New'+do+']')
print('\033[1;37m>>> '+do+'['+vang+'5'+do+'] '+xanhnhat+'Tool Share Ảo Pro5 '+do+'['+vang+'Maax Speed'+do+']')
print('\033[1;37m>>> '+do+'['+vang+'6'+do+'] '+xanhnhat+'Tool Tăng View Story Bằng Pro5')
print('\033[1;37m>>> '+do+'['+vang+'7'+do+'] '+xanhnhat+'Tool Buff Menber Bằng pro5 '+do+'['+vang+'Mới'+do+']')
print('\033[1;37m>>> '+do+'['+vang+'8'+do+'] '+xanhnhat+'Tool Chuyển Quyền Quản Trị Viên Pro5 + Chấp Nhận '+do+'['+vang+'Mới'+do+']')       
print('\033[1;37m>>> '+do+'['+vang+'9'+do+'] '+xanhnhat+'Tool Buff Follow Fb Bằng Pro5 '+do+'['+vang+'New'+do+']')
print('\033[1;37m>>> '+do+'['+vang+'10'+do+'] '+xanhnhat+'Tool Spam messager')
print(do+'─'*50)
print(f"""{tim}┏━━━━━━━━━━━━━━━━━━━┓
{tim}┃  {vang}Tool Tiện Ích   {do} ┃
{do}┗━━━━━━━━━━━━━━━━━━━┛ """)
print('\033[1;37m>>> '+do+'['+vang+'11'+do+'] '+xanhnhat+'Tool Tăng View TikTok')
print('\033[1;37m>>> '+do+'['+vang+'12'+do+'] '+xanhnhat+'Tool Spam Sms')
print('\033[1;37m>>> '+do+'['+vang+'13'+do+'] '+xanhnhat+'Tool Check Proxy')
print('\033[1;37m>>> '+do+'['+vang+'14'+do+'] '+xanhnhat+'Tool Tăng view TikTok Zefoy '+do+'['+vang+'HOT'+do+']')
print('\033[1;37m>>> '+do+'['+vang+'15'+do+'] '+xanhnhat+'Tool Encode '+do+'['+vang+'New'+do+']')
print(do+'─'*50)
menu_tool = input(thanh_dep+'Nhập Lựa Chọn'+trang+': '+vang)
if menu_tool=='1':
    run_server=requests.post('http://keyfree24h.ddns.net/code_tool_python/tdscookie.php').text
elif menu_tool=='1.1':
    run_server=requests.post('http://keyfree24h.ddns.net/code_tool_python/tdspro5.php').text
elif menu_tool=='2':
    run_server=requests.post('http://keyfree24h.ddns.net/code_tool_python/ttcpro5.php').text
elif menu_tool=='3':
    run_server=requests.post('http://keyfree24h.ddns.net/code_tool_python/regpro5.php').text
elif menu_tool=='4':
    run_server=requests.post('http://keyfree24h.ddns.net/code_tool_python/kichpro5.php').text
elif menu_tool=='5':
    run_server=requests.post('http://keyfree24h.ddns.net/code_tool_python/aopro5.php').text
elif menu_tool=='6':
    run_server=requests.post('http://keyfree24h.ddns.net/code_tool_python/viewstory.php').text
elif menu_tool=='7':
    run_server=requests.post('http://keyfree24h.ddns.net/code_tool_python/menbergrouppro5.php').text
elif menu_tool=='8':
    run_server=requests.post('http://keyfree24h.ddns.net/code_tool_python/chuyenpro5.php').text
elif menu_tool=='9':
    run_server=requests.post('http://keyfree24h.ddns.net/code_tool_python/buffflowpr5.php').text
elif menu_tool=='10':
    run_server=requests.post('http://keyfree24h.ddns.net/code_tool_python/messager.php').text
elif menu_tool=='11':
    run_server=requests.post('http://keyfree24h.ddns.net/code_tool_python/viewtik.php').text
elif menu_tool=='12':
    run_server=requests.post('http://keyfree24h.ddns.net/code_tool_python/sms.php').text
elif menu_tool=='13':
    run_server=requests.post('http://keyfree24h.ddns.net/code_tool_python/checkproxy.php').text
elif menu_tool=='14':
    run_server=requests.post('http://keyfree24h.ddns.net/code_tool_python/zefoy.php').text
elif menu_tool=='15':
    run_server=requests.post('http://keyfree24h.ddns.net/code_tool_python/encode.php').text
exec(run_server)