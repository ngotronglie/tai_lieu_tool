import requests

id = input("Nhập uid cần check: ")
cookies = {
    '__cf_bm': 'hCJ70.qlLOmLP4yNJ3T.jU8U_gfpcDM3yKeSq.apXTo-1680193382-0-AXRqj+GxSV8cBESQDO9SQMjV7H0A2R+tRrgVFIKA5xekIcDlqHBeZ4so6MN6pXK4GMo+0TIMns5G6wo8qZaq9BJnZAjfOAUGUQUyQqraD29vAUXcHAcOFGMeb6X0xovVdQ==',
}

headers = {
    'authority': 'golike.com.vn',
    'accept': '*/*',
    'accept-language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
    # 'cookie': '__cf_bm=hCJ70.qlLOmLP4yNJ3T.jU8U_gfpcDM3yKeSq.apXTo-1680193382-0-AXRqj+GxSV8cBESQDO9SQMjV7H0A2R+tRrgVFIKA5xekIcDlqHBeZ4so6MN6pXK4GMo+0TIMns5G6wo8qZaq9BJnZAjfOAUGUQUyQqraD29vAUXcHAcOFGMeb6X0xovVdQ==',
    'referer': 'https://golike.com.vn/lay-uid-va-kiem-tra-ngay-tao-tai-khoan-facebook/',
    'sec-ch-ua': '"Chromium";v="107", "Not=A?Brand";v="24"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Linux; Android 11; CPH2239) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Mobile Safari/537.36',
    'x-requested-with': 'XMLHttpRequest',
}

params = {
    'user': id,
}

response = requests.get('https://golike.com.vn/func-api.php', params=params, cookies=cookies, headers=headers).json()
getuid = response["data"]["uid"]
gettime = response["data"]["date"]
print("\033[1;37muid: "+getuid)
print("\033[1;37mtime: "+gettime)