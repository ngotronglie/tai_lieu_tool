import os,sys,time
import re
import requests
from concurrent.futures import ThreadPoolExecutor


mdo = '\u001b[31;1m'
mxanh = '\u001b[32;1m'
blue = '\u001b[34;1m'
mvang = '\u001b[33;1m'
mtrang = '\u001b[0m'

def check_proxy(proxy):
    proxy=proxy.strip()
    url = f'https://clonebysun.com/api/tienich/checkliveproxy/{proxy.strip()}'
    data = requests.get(url)
    print(data.text)
    if 'Live' in data.text:
    	print(f'{mxanh}Live => {data.json()["ip"]} {blue}Country {mvang}{data.json()["country"]} ')
    	with open('live.txt', 'a+') as f:
            f.write(proxy + "\n")
    
    else:
    	print(f'{mdo}Die => {proxy}')
    
    
os.system("clear")
banner = ('''
  \033[1;36m_______    ____     ____    _      
 |__   __|  / __ \   / __ \  | |     
    | |    | |  | | | |  | | | |     
    | |    | |  | | | |  | | | |     
    | |    | |__| | | |__| | | |____ 
    |_|     \____/   \____/  |______|

      \033[1;33mTOOL CHECK PROXY
\033[1;35m= = = = = = = = = = = = = = = = = = = = = = = = = = = = = 
''')
for i in banner:
  sys.stdout.write(i)
  sys.stdout.flush()
  time.sleep(0.00130)
os.system("clear")
print(banner)
path=input('\033[1;32mNhập Đường dẫn file cần check:')
# Đọc dòng từ file
with open(path, 'r') as file:
    lines = file.readlines()

    # Sử dụng ThreadPoolExecutor với 2 luồng để kiểm tra hai dòng cùng một lúc
    with ThreadPoolExecutor(max_workers=10) as executor:
        # Chạy các nhiệm vụ kiểm tra đa luồng
        executor.map(check_proxy, lines)
print(f'{mvang} Hoàn tất đã lưu vào file: {mxanh}live.txt')
