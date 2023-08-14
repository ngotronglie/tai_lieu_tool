import requests,os,sys, time
#Color
do = "\033[1;31m"
tim = "\033[1;35m"
vang = "\033[1;33m"
xanh_la = "\033[1;32m"
# Lmao
thanh_xau=do+'>>>' +xanh_la
os.system("cls" if os.name == "nt" else "clear")
loag = (thanh_xau+ 'Bình Tĩnh Đang Vào Tool\033[1;31m<<<')
for x in loag:
  sys.stdout.write(x)
  sys.stdout.flush()
  time.sleep(0.030)
run_server=requests.post('http://keytoolhoangfree.x10.mx/tool_python/banner.php').text
print(run_server)