d = "\033[1;31m"
l = "\033[1;32m"
v = "\033[1;33m"
t = "\033[1;37m"
tim = "\033[1;35m"
x = "\033[1;36m"
thanh = f'\033[1;35m {t}=> '
hongthanh = f'{d}[{t}</>{d}] {t}=>'
den = "\033[1;90m"
lamd = "\033[1;34m"
logo = f"{t}[{d}=.={t}]"
import json #line:1:import json
import os ,time #line:2:import os,time
import cloudscraper #line:3:import cloudscraper
import requests #line:4:import requests
import socket #line:5:import socket
import subprocess #line:6:import subprocess
from time import strftime #line:7:from time import strftime
from time import sleep #line:8:from time import sleep
from datetime import datetime ,timedelta #line:9:from datetime import datetime, timedelta
from bs4 import BeautifulSoup #line:10:from bs4 import BeautifulSoup
import time #line:11:import time
from colorama import Fore ,init #line:12:from colorama import Fore, init
import sys #line:13:import sys
import base64 #line:14:import base64
import subprocess #line:15:import subprocess
from pystyle import Colors ,Colorate #line:16:from pystyle import Colors, Colorate
from rich .console import Console #line:17:from rich.console import Console
from rich .panel import Panel #line:18:from rich.panel import Panel
from rich .console import Console #line:19:from rich.console import Console
from rich .text import Text #line:20:from rich.text import Text
def kiem_tra_mang ():#line:21:def kiem_tra_mang():
    try :#line:22:try:
        socket .create_connection (("8.8.8.8",53 ),timeout =3 )#line:23:socket.create_connection(("8.8.8.8", 53), timeout=3)
    except OSError :#line:24:except OSError:
        print ("Mạng không ổn định hoặc bị mất kết nối. Vui lòng kiểm tra lại mạng.")#line:25:print("Mạng không ổn định hoặc bị mất kết nối. Vui lòng kiểm tra lại mạng.")
kiem_tra_mang ()#line:26:kiem_tra_mang()
scraper =cloudscraper .create_scraper ()#line:27:scraper = cloudscraper.create_scraper()
def banner():
    os.system('cls' if os.name=='nt' else 'clear')
    tool = "GOLIKE TIKTOK"
    print(f'''
            
{tim}███╗░░░███╗██╗░░░░░░█████╗░███╗░░██╗░██████╗░
{t}████╗░████║██║░░░░░██╔══██╗████╗░██║██╔════╝░
{tim}██╔████╔██║██║░░░░░██║░░██║██╔██╗██║██║░░██╗░
{t}██║╚██╔╝██║██║░░░░░██║░░██║██║╚████║██║░░╚██╗
{tim}██║░╚═╝░██║███████╗╚█████╔╝██║░╚███║╚██████╔╝
{t}╚═╝░░░░░╚═╝╚══════╝░╚════╝░╚═╝░░╚══╝░╚═════╝░
{t}Tool by: {l}Nguyễn Mạnh Long            {t}Phiên Bản: {l}1.0                   
{d}══════════════════════════════════════════════════════
{logo} {t}Tool{d} : {l}{tool}
{logo} {t}Ngày{d} : {x}{datetime.now().strftime('%d/%m/%Y %H:%M:%S')}
{logo} {t}Phiên Bản{d} :{l} Python 3.12
{logo} {t}Chất Lượng Xây Dựng Niềm Tin
{d}══════════════════════════════════════════════════════''')#line:43:os.system('cls' if os.name== 'nt' else 'clear')
banner()#line:44:print(banner)
print ("\033[1;35m╔═════════════════════════════════╗")#line:45:print("\033[1;35m╔═════════════════════════════════╗")
print ("\033[1;35m║       \033[1;33m  LOGIN GOLIKE            \033[1;35m║")#line:46:print("\033[1;35m║       \033[1;33m  LOGIN GOLIKE        \033[1;35m║")
print ("\033[1;35m╚═════════════════════════════════╝")#line:47:print("\033[1;35m╚═════════════════════════════════╝")
try :#line:49:try:
  Authorization =open ("Authorization.txt","x")#line:50:Authorization = open("Authorization.txt","x")
except :#line:51:except:
  pass #line:52:pass
Authorization =open ("Authorization.txt","r")#line:53:Authorization = open("Authorization.txt","r")
t =open ("token.txt","r")#line:54:t = open("token.txt","r")
author =Authorization .read ()#line:56:author = Authorization.read()
token =t .read ()#line:57:token = t.read()
if author =="":#line:58:if author == "":
  author =input ("\033[1;32mNHẬP AUTHORIZATION : \033[1;33m")#line:59:author = input("\033[1;32mNHẬP AUTHORIZATION : \033[1;33m")
  token =input ("\033[1;32mNHẬP T : \033[1;33m")#line:60:token = input("\033[1;32mNHẬP T : \033[1;33m")
  Authorization =open ("Authorization.txt","w")#line:61:Authorization = open("Authorization.txt","w")
  t =open ("token.txt","w")#line:62:t = open("token.txt","w")
  Authorization .write (author )#line:63:Authorization.write(author)
  t .write (token )#line:64:t.write(token)
else :#line:65:else:
  print (f"\033[1;32m       Nhấn Enter để vào TOOL")#line:66:print(f"\033[1;32m       Nhấn Enter để vào TOOL")
  print (f"\033[38;2;0;220;255m               HOẶC ")#line:67:print(f"\033[38;2;0;220;255m               HOẶC ")
  select =input (f"\033[1;32mNhập AUTHORIZATION {Fore.RED}(tại đây) \033[1;32mđể vào acc khác: \033[1;33m")#line:68:select = input(f"\033[1;32mNhập AUTHORIZATION {Fore.RED}(tại đây) \033[1;32mđể vào acc khác: \033[1;33m")
  kiem_tra_mang ()#line:69:kiem_tra_mang()
  if select !="":#line:70:if select != "":
    author =select #line:71:author = select
    token =input ("\033[1;32mNhập T (Token) : \033[1;33m")#line:72:token = input("\033[1;32mNhập T (Token) : \033[1;33m")
    Authorization =open ("Authorization.txt","w")#line:73:Authorization = open("Authorization.txt","w")
    t =open ("token.txt","w")#line:74:t = open("token.txt","w")
    Authorization .write (author )#line:75:Authorization.write(author)
    t .write (token )#line:76:t.write(token)
Authorization .close ()#line:77:Authorization.close()
t .close ()#line:78:t.close()
os .system ('cls'if os .name =='nt'else 'clear')#line:79:os.system('cls' if os.name== 'nt' else 'clear')
print (banner )#line:80:print(banner)
print ("\033[1;35m╔═════════════════════════════════╗")#line:81:print("\033[1;35m╔═════════════════════════════════╗")
print ("\033[1;35m║   \033[1;33m   LIST ACC TIKTOK       \033[1;35m║")#line:82:print("\033[1;35m║   \033[1;33m   LIST ACC TIKTOK       \033[1;35m║")
print ("\033[1;35m╚═════════════════════════════════╝")#line:83:print("\033[1;35m╚═════════════════════════════════╝")
headers ={'Accept':'application/json, text/plain, */*','Content-Type':'application/json;charset=utf-8','Authorization':author ,'t':token ,'User-Agent':'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36','Referer':'https://app.golike.net/account/manager/tiktok',}#line:91:}
scraper =cloudscraper .create_scraper ()#line:92:scraper = cloudscraper.create_scraper()
def chonacc ():#line:93:def chonacc():
    O0O0O0OOOOO00O0OO ={}#line:94:json_data = {}
    OO0O000OOO00OOO0O =scraper .get ('https://gateway.golike.net/api/tiktok-account',headers =headers ,json =O0O0O0OOOOO00O0OO ).json ()#line:99:).json()
    return OO0O000OOO00OOO0O #line:100:return response
def nhannv (O00OOOO0O000OOOO0 ):#line:101:def nhannv(account_id):
    try :#line:102:try:
        O000OOO000OO000O0 ={'account_id':O00OOOO0O000OOOO0 ,'data':'null',}#line:106:}
        O00000OOO0OOO0O00 =scraper .get ('https://gateway.golike.net/api/advertising/publishers/tiktok/jobs',headers =headers ,params =O000OOO000OO000O0 ,json ={})#line:112:)
        return O00000OOO0OOO0O00 .json ()#line:113:return response.json()
    except Exception as OO000OO0OOO0OOO0O :#line:114:except Exception as e:
        print ()#line:115:print()
        return {}#line:116:return {}
def hoanthanh (OOO000O00OO0OO00O ,O00OO00OO0OOO00O0 ):#line:117:def hoanthanh(ads_id, account_id):
    try :#line:118:try:
        OOOOO0O000OOOO0O0 ={'ads_id':OOO000O00OO0OO00O ,'account_id':O00OO00OO0OOO00O0 ,'async':True ,'data':None ,}#line:124:}
        O0O00O00O0O0OO0OO =scraper .post ('https://gateway.golike.net/api/advertising/publishers/tiktok/complete-jobs',headers =headers ,json =OOOOO0O000OOOO0O0 ,timeout =6 )#line:130:)
        return O0O00O00O0O0OO0OO .json ()#line:131:return response.json()
    except Exception as OO0OO000OO0O0O0OO :#line:132:except Exception as e:
        print ()#line:133:print()
        return {}#line:134:return {}
def baoloi (O0OOO0OOO000OOOO0 ,OOO0O0O00OO00OO00 ,OOO0O0000OOOOOO0O ,OO00000O0O00OO00O ):#line:135:def baoloi(ads_id, object_id, account_id, loai):
    try :#line:136:try:
        O000OOO0OOO000OOO ={'description':'Tôi đã làm Job này rồi','users_advertising_id':O0OOO0OOO000OOOO0 ,'type':'ads','provider':'tiktok','fb_id':OOO0O0000OOOOOO0O ,'error_type':6 ,}#line:144:}
        scraper .post ('https://gateway.golike.net/api/report/send',headers =headers ,json =O000OOO0OOO000OOO )#line:145:scraper.post('https://gateway.golike.net/api/report/send', headers=headers, json=json_data1)
        O0OOO00000O00O0OO ={'ads_id':O0OOO0OOO000OOOO0 ,'object_id':OOO0O0O00OO00OO00 ,'account_id':OOO0O0000OOOOOO0O ,'type':OO00000O0O00OO00O ,}#line:151:}
        scraper .post ('https://gateway.golike.net/api/advertising/publishers/tiktok/skip-jobs',headers =headers ,json =O0OOO00000O00O0OO ,)#line:156:)
    except Exception as O00O0O000000O0000 :#line:157:except Exception as e:
        print ()#line:158:print()
chontktiktok =chonacc ()#line:160:chontktiktok = chonacc()
def dsacc ():#line:161:def dsacc():
  if chontktiktok .get ("status")!=200 :#line:162:if chontktiktok.get("status") != 200:
    print ("\033[1;31mAuthorization hoăc T sai   ")#line:163:print("\033[1;31mAuthorization hoăc T sai   ")
    quit ()#line:164:quit()
  for O0O0O0O00000O0000 in range (len (chontktiktok ["data"])):#line:165:for i in range(len(chontktiktok["data"])):
    print (f'\033[1;36m[{O0O0O0O00000O0000+1}]\033[1;93m {chontktiktok["data"][O0O0O0O00000O0000]["nickname"]} \033[1;97m|\033[1;31m\033[1;32m Hoạt Động')#line:166:print(f'\033[1;36m[{i+1}]\033[1;93m {chontktiktok["data"][i]["nickname"]} \033[1;97m|\033[1;31m\033[1;32m Hoạt Động')
dsacc ()#line:167:dsacc()
print (f"{Fore.MAGENTA}═══════════════════════════════════")#line:168:print(f"{Fore.MAGENTA}═══════════════════════════════════")
while True :#line:169:while True:
  try :#line:170:try:
    luachon =int (input ("\033[1;32mChọn tài khoản TIKTOK: \033[1;33m"))#line:171:luachon = int(input("\033[1;32mChọn tài khoản TIKTOK: \033[1;33m"))
    while luachon >len ((chontktiktok )["data"]):#line:172:while luachon > len((chontktiktok)["data"]):
      luachon =int (input ("\033[1;32mAcc Này Không Có Trong Danh Sách , Nhập Lại : \033[1;33m"))#line:173:luachon = int(input("\033[1;32mAcc Này Không Có Trong Danh Sách , Nhập Lại : \033[1;33m"))
    account_id =chontktiktok ["data"][luachon -1 ]["id"]#line:174:account_id = chontktiktok["data"][luachon - 1]["id"]
    break #line:175:break
  except :#line:176:except:
    print ("\033[1;31mSai Định Dạng   ")#line:177:print("\033[1;31mSai Định Dạng   ")
while True :#line:178:while True:
  try :#line:179:try:
    delay =int (input (f"\033[1;32mDelay: \033[1;33m"))#line:180:delay = int(input(f"\033[1;32mDelay: \033[1;33m"))
    break #line:181:break
  except :#line:182:except:
    print ("\033[1;31mSai Định Dạng  ")#line:183:print("\033[1;31mSai Định Dạng  ")
while True :#line:184:while True:
  try :#line:185:try:
    doiacc =int (input (f"\033[1;32mThất bại bao nhiêu lần thì đổi acc: \033[1;33m"))#line:186:doiacc = int(input(f"\033[1;32mThất bại bao nhiêu lần thì đổi acc: \033[1;33m"))
    break #line:187:break
  except :#line:188:except:
    print ("\033[1;31mNhập Vào 1 Số  ")#line:189:print("\033[1;31mNhập Vào 1 Số  ")
print ("\033[1;35m╔═════════════════════════════════╗")#line:190:print("\033[1;35m╔═════════════════════════════════╗")
print ("\033[1;35m║     \033[1;33m  CHỌN LOẠI NHIỆM VỤ        \033[1;35m║")#line:191:print("\033[1;35m║     \033[1;33m  CHỌN LOẠI NHIỆM VỤ        \033[1;35m║")
print ("\033[1;35m╚═════════════════════════════════╝")#line:192:print("\033[1;35m╚═════════════════════════════════╝")
print ("\033[1;36m[1] \033[1;32mFollow")#line:193:print("\033[1;36m[1] \033[1;32mFollow")
print ("\033[1;36m[2] \033[1;32mLike")#line:194:print("\033[1;36m[2] \033[1;32mLike")
print ("\033[1;36m[3] \033[1;32mCả hai (\033[1;33mFollow và Like\033[1;32m)")#line:195:print("\033[1;36m[3] \033[1;32mCả hai (\033[1;33mFollow và Like\033[1;32m)")
while True :#line:196:while True:
    try :#line:197:try:
        loai_nhiem_vu =int (input ("\033[1;32mChọn loại nhiệm vụ: \033[1;33m"))#line:198:loai_nhiem_vu = int(input("\033[1;32mChọn loại nhiệm vụ: \033[1;33m"))
        if loai_nhiem_vu in [1 ,2 ,3 ]:#line:199:if loai_nhiem_vu in [1, 2, 3]:
            break #line:200:break
        else :#line:201:else:
            print ("\033[1;31mVui lòng chọn số từ 1 đến 3!")#line:202:print("\033[1;31mVui lòng chọn số từ 1 đến 3!")
    except :#line:203:except:
        print ("\033[1;31mSai định dạng! Vui lòng nhập số.")#line:204:print("\033[1;31mSai định dạng! Vui lòng nhập số.")
x_like ,y_like ,x_follow ,y_follow =None ,None ,None ,None #line:205:x_like, y_like, x_follow, y_follow = None, None, None, None
print ("\033[1;35m╔═════════════════════════════════╗")#line:206:print("\033[1;35m╔═════════════════════════════════╗")
print ("\033[1;35m║       \033[1;33m  ADB Tự Ðộng             \033[1;35m║")#line:207:print("\033[1;35m║       \033[1;33m  ADB Tự Ðộng             \033[1;35m║")
print ("\033[1;35m╚═════════════════════════════════╝")#line:208:print("\033[1;35m╚═════════════════════════════════╝")
print (f"\033[1;36m[1] yes")#line:209:print(f"\033[1;36m[1] yes")
print (f"\033[1;36m[2] no")#line:210:print(f"\033[1;36m[2] no")
adbyn =input (f"\033[1;32mNhập lựa chọn: \033[1;33m")#line:211:adbyn = input(f"\033[1;32mNhập lựa chọn: \033[1;33m")
if adbyn =="1":#line:212:if adbyn == "1":
    def setup_adb ():#line:213:def setup_adb():
      O0O000OO0000OOOO0 ="adb_config.txt"#line:214:config_file = "adb_config.txt"
      O0O00O0O00OOO000O ="toa_do_tim.txt"#line:215:like_coords_file = "toa_do_tim.txt"
      O0OO0O0O0O000O000 ="toa_do_follow.txt"#line:216:follow_coords_file = "toa_do_follow.txt"
      print (f"{Fore.MAGENTA}═══════════════════════════════════")#line:218:print(f"{Fore.MAGENTA}═══════════════════════════════════")
      O0OOO0OO0O00OO000 =input ("\033[1;32mNhập IP của thiết bị ví dụ (192.168.1.2): \033[1;33m")#line:221:ip = input("\033[1;32mNhập IP của thiết bị ví dụ (192.168.1.2): \033[1;33m")
      OO0O00OOOOO00OO00 =input ("\033[1;32mNhập port của thiết bị ví dụ (39327): \033[1;33m")#line:222:adb_port = input("\033[1;32mNhập port của thiết bị ví dụ (39327): \033[1;33m")
      OOOOO00OOO0O0000O ,OO000OO0OOOOO0O0O ,OOOO00O0OOO0OO000 ,OOOOO0OO0OO00000O =None ,None ,None ,None #line:224:x_like, y_like, x_follow, y_follow = None, None, None, None
      if os .path .exists (O0O00O0O00OOO000O ):#line:225:if os.path.exists(like_coords_file):
           with open (O0O00O0O00OOO000O ,"r")as O00OO0OOOO00O0O00 :#line:226:with open(like_coords_file, "r") as f:
              O0O00O00000OOOOO0 =O00OO0OOOO00O0O00 .read ().split ("|")#line:227:coords = f.read().split("|")
              if len (O0O00O00000OOOOO0 )==2 :#line:228:if len(coords) == 2:
                   OOOOO00OOO0O0000O ,OO000OO0OOOOO0O0O =O0O00O00000OOOOO0 #line:229:x_like, y_like = coords
                   print (f"\033[1;32mĐã tìm thấy tọa độ nút tim: X={OOOOO00OOO0O0000O}, Y={OO000OO0OOOOO0O0O}")#line:230:print(f"\033[1;32mĐã tìm thấy tọa độ nút tim: X={x_like}, Y={y_like}")
      if os .path .exists (O0OO0O0O0O000O000 ):#line:231:if os.path.exists(follow_coords_file):
          with open (O0OO0O0O0O000O000 ,"r")as O00OO0OOOO00O0O00 :#line:232:with open(follow_coords_file, "r") as f:
               O0O00O00000OOOOO0 =O00OO0OOOO00O0O00 .read ().split ("|")#line:233:coords = f.read().split("|")
               if len (O0O00O00000OOOOO0 )==2 :#line:234:if len(coords) == 2:
                   OOOO00O0OOO0OO000 ,OOOOO0OO0OO00000O =O0O00O00000OOOOO0 #line:235:x_follow, y_follow = coords
                   print (f"\033[1;32mĐã tìm thấy tọa độ nút follow: X={OOOO00O0OOO0OO000}, Y={OOOOO0OO0OO00000O}")#line:236:print(f"\033[1;32mĐã tìm thấy tọa độ nút follow: X={x_follow}, Y={y_follow}")
      if not os .path .exists (O0O000OO0000OOOO0 ):#line:237:if not os.path.exists(config_file):
           print ("\033[1;36mLần đầu chạy, nhập mã ghép nối (6 SỐ) và port ghép nối.\033[0m")#line:238:print("\033[1;36mLần đầu chạy, nhập mã ghép nối (6 SỐ) và port ghép nối.\033[0m")
           O000O00OO0O0O0O0O =input ("\033[1;32mNhập mã ghép nối 6 số ví dụ (322763): \033[1;33m")#line:239:pair_code = input("\033[1;32mNhập mã ghép nối 6 số ví dụ (322763): \033[1;33m")
           OO00O0000O00OOOOO =input ("\033[1;32mNhập port ghép nối ví dụ (44832): \033[1;33m")#line:240:pair_port = input("\033[1;32mNhập port ghép nối ví dụ (44832): \033[1;33m")
           with open (O0O000OO0000OOOO0 ,"w")as O00OO0OOOO00O0O00 :#line:241:with open(config_file, "w") as f:
               O00OO0OOOO00O0O00 .write (f"{O000O00OO0O0O0O0O}|{OO00O0000O00OOOOO}")#line:242:f.write(f"{pair_code}|{pair_port}")
      else :#line:243:else:
          with open (O0O000OO0000OOOO0 ,"r")as O00OO0OOOO00O0O00 :#line:244:with open(config_file, "r") as f:
               O000O00OO0O0O0O0O ,OO00O0000O00OOOOO =[OOOO00000O00OOO00 .strip ()for OOOO00000O00OOO00 in O00OO0OOOO00O0O00 .read ().split ("|")]#line:245:pair_code, pair_port = [s.strip() for s in f.read().split("|")]
      print ("\n\033[1;36m  Đang ghép nối với thiết bị\033[0m")#line:246:print("\n\033[1;36m  Đang ghép nối với thiết bị\033[0m")
      os .system (f"adb pair {O0OOO0OO0O00OO000}:{OO00O0000O00OOOOO} {O000O00OO0O0O0O0O}")#line:247:os.system(f"adb pair {ip}:{pair_port} {pair_code}")
      time .sleep (2 )#line:248:time.sleep(2)
      print ("\033[1;36m  Đang kết nối ADB\033[0m")#line:249:print("\033[1;36m  Đang kết nối ADB\033[0m")
      os .system (f"adb connect {O0OOO0OO0O00OO000}:{OO0O00OOOOO00OO00}")#line:250:os.system(f"adb connect {ip}:{adb_port}")
      time .sleep (2 )#line:251:time.sleep(2)
      O0OO0OO0O0O000O0O =os .popen ("adb devices").read ()#line:252:devices = os.popen("adb devices").read()
      if O0OOO0OO0O00OO000 not in O0OO0OO0O0O000O0O :#line:253:if ip not in devices:
        print (f"{Fore.RED} Kết nối thất bại{Fore.WHITE}")#line:254:print(f"{Fore.RED} Kết nối thất bại{Fore.WHITE}")
        exit ()#line:255:exit()
      print ("\033[1;35m╔═════════════════════════════════╗")#line:257:print("\033[1;35m╔═════════════════════════════════╗")
      print ("\033[1;35m║     \033[1;33m  NHẬP TỌA ĐỘ NÚT         \033[1;35m║")#line:258:print("\033[1;35m║     \033[1;33m  NHẬP TỌA ĐỘ NÚT         \033[1;35m║")
      print ("\033[1;35m╚═════════════════════════════════╝")#line:259:print("\033[1;35m╚═════════════════════════════════╝")
      if loai_nhiem_vu in [1 ,3 ]and (OOOO00O0OOO0OO000 is None or OOOOO0OO0OO00000O is None ):#line:260:if loai_nhiem_vu in [1, 3] and (x_follow is None or y_follow is None):
           OOOO00O0OOO0OO000 =input ("\033[1;32mNhập tọa độ X của nút follow: \033[1;33m")#line:261:x_follow = input("\033[1;32mNhập tọa độ X của nút follow: \033[1;33m")
           OOOOO0OO0OO00000O =input ("\033[1;32mNhập tọa độ Y của nút follow: \033[1;33m")#line:262:y_follow = input("\033[1;32mNhập tọa độ Y của nút follow: \033[1;33m")
           with open (O0OO0O0O0O000O000 ,"w")as O00OO0OOOO00O0O00 :#line:263:with open(follow_coords_file, "w") as f:
               O00OO0OOOO00O0O00 .write (f"{OOOO00O0OOO0OO000}|{OOOOO0OO0OO00000O}")#line:264:f.write(f"{x_follow}|{y_follow}")
      if loai_nhiem_vu in [2 ,3 ]and (OOOOO00OOO0O0000O is None or OO000OO0OOOOO0O0O is None ):#line:265:if loai_nhiem_vu in [2, 3] and (x_like is None or y_like is None):
           OOOOO00OOO0O0000O =input ("\033[1;32mNhập tọa độ X của nút tim: \033[1;33m")#line:266:x_like = input("\033[1;32mNhập tọa độ X của nút tim: \033[1;33m")
           OO000OO0OOOOO0O0O =input ("\033[1;32mNhập tọa độ Y của nút tim: \033[1;33m")#line:267:y_like = input("\033[1;32mNhập tọa độ Y của nút tim: \033[1;33m")
           with open (O0O00O0O00OOO000O ,"w")as O00OO0OOOO00O0O00 :#line:268:with open(like_coords_file, "w") as f:
              O00OO0OOOO00O0O00 .write (f"{OOOOO00OOO0O0000O}|{OO000OO0OOOOO0O0O}")#line:269:f.write(f"{x_like}|{y_like}")
      return OOOOO00OOO0O0000O ,OO000OO0OOOOO0O0O ,OOOO00O0OOO0OO000 ,OOOOO0OO0OO00000O #line:270:return x_like, y_like, x_follow, y_follow
    x_like ,y_like ,x_follow ,y_follow =setup_adb ()#line:272:x_like, y_like, x_follow, y_follow = setup_adb()
elif adbyn =="2":#line:273:elif adbyn == "2":
    pass #line:274:pass
dem =0 #line:276:dem = 0
tong =0 #line:277:tong = 0
checkdoiacc =0 #line:278:checkdoiacc = 0
dsaccloi =[]#line:279:dsaccloi = []
accloi =""#line:280:accloi = ""
os .system ('cls'if os .name =='nt'else 'clear')#line:281:os.system('cls' if os.name== 'nt' else 'clear')
print (banner )#line:282:print(banner)
print ("\033[1;37m════════════════════════════════════════════════════════════")#line:283:print("\033[1;37m════════════════════════════════════════════════════════════")
print ("\033[1;31m| \033[1;36mSTT \033[1;37m| \033[1;33mThời gian \033[1;37m| \033[1;32mStatus \033[1;37m| \033[1;31mType job \033[1;37m| \033[1;32mID Acc \033[1;37m| \033[1;32mXu \033[1;37m| \033[1;33mTổng       ")#line:284:print("\033[1;31m| \033[1;36mSTT \033[1;37m| \033[1;33mThời gian \033[1;37m| \033[1;32mStatus \033[1;37m| \033[1;31mType job \033[1;37m| \033[1;32mID Acc \033[1;37m| \033[1;32mXu \033[1;37m| \033[1;33mTổng       ")
print ("\033[1;37m════════════════════════════════════════════════════════════")#line:285:print("\033[1;37m════════════════════════════════════════════════════════════")
while True :#line:286:while True:
    if checkdoiacc ==doiacc :#line:287:if checkdoiacc == doiacc:
        dsaccloi .append (chontktiktok ["data"][luachon -1 ]["nickname"])#line:288:dsaccloi.append(chontktiktok["data"][luachon - 1]["nickname"])
        print (f"{Fore.WHITE}════════════════════════════════════════════════════")#line:289:print(f"{Fore.WHITE}════════════════════════════════════════════════════")
        print (f"\033[1;31m  Acc Tiktok {dsaccloi} gặp vấn đề ")#line:290:print(f"\033[1;31m  Acc Tiktok {dsaccloi} gặp vấn đề ")
        print (f"{Fore.WHITE}════════════════════════════════════════════════════")#line:291:print(f"{Fore.WHITE}════════════════════════════════════════════════════")
        dsacc ()#line:292:dsacc()
        while True :#line:293:while True:
            try :#line:294:try:
                print (f"{Fore.WHITE}════════════════════════════════════════════════════")#line:295:print(f"{Fore.WHITE}════════════════════════════════════════════════════")
                luachon =int (input ("\033[1;32mChọn tài khoản mới: \033[1;33m"))#line:296:luachon = int(input("\033[1;32mChọn tài khoản mới: \033[1;33m"))
                while luachon >len ((chontktiktok )["data"]):#line:297:while luachon > len((chontktiktok)["data"]):
                    luachon =int (input ("\033[1;31mAcc Này Không Có Trong Danh Sách, Hãy Nhập Lại : \033[1;33m"))#line:298:luachon = int(input("\033[1;31mAcc Này Không Có Trong Danh Sách, Hãy Nhập Lại : \033[1;33m"))
                account_id =chontktiktok ["data"][luachon -1 ]["id"]#line:299:account_id = chontktiktok["data"][luachon - 1]["id"]
                checkdoiacc =0 #line:300:checkdoiacc = 0
                os .system ('cls'if os .name =='nt'else 'clear')#line:301:os.system('cls' if os.name== 'nt' else 'clear')
                for h in banner :#line:302:for h in banner:
                    print (h ,end ="")#line:303:print(h,end = "")
                break #line:304:break
            except :#line:305:except:
                print ("\033[1;31mSai Định Dạng !!!")#line:306:print("\033[1;31mSai Định Dạng !!!")
    print ('\033[1;35mĐang Tìm Nhiệm Vụ',end ="\r")#line:307:print('\033[1;35mĐang Tìm Nhiệm Vụ', end="\r")
    max_retries =3 #line:308:max_retries = 3
    retry_count =0 #line:309:retry_count = 0
    nhanjob =None #line:310:nhanjob = None
    while retry_count <max_retries :#line:311:while retry_count < max_retries:
        try :#line:312:try:
            nhanjob =nhannv (account_id )#line:313:nhanjob = nhannv(account_id)
            if nhanjob and nhanjob .get ("status")==200 and nhanjob ["data"].get ("link")and nhanjob ["data"].get ("object_id"):#line:314:if nhanjob and nhanjob.get("status") == 200 and nhanjob["data"].get("link") and nhanjob["data"].get("object_id"):
                break #line:315:break
            else :#line:316:else:
                retry_count +=1 #line:317:retry_count += 1
                time .sleep (2 )#line:318:time.sleep(2)
        except Exception as e :#line:319:except Exception as e:
            retry_count +=1 #line:320:retry_count += 1
            time .sleep (1 )#line:321:time.sleep(1)
    if not nhanjob or retry_count >=max_retries :#line:322:if not nhanjob or retry_count >= max_retries:
        continue #line:323:continue
    ads_id =nhanjob ["data"]["id"]#line:324:ads_id = nhanjob["data"]["id"]
    link =nhanjob ["data"]["link"]#line:325:link = nhanjob["data"]["link"]
    object_id =nhanjob ["data"]["object_id"]#line:326:object_id = nhanjob["data"]["object_id"]
    job_type =nhanjob ["data"]["type"]#line:327:job_type = nhanjob["data"]["type"]
    if (loai_nhiem_vu ==1 and job_type !="follow")or (loai_nhiem_vu ==2 and job_type !="like")or (job_type not in ["follow","like"]):#line:331:(job_type not in ["follow", "like"]):
        baoloi (ads_id ,object_id ,account_id ,job_type )#line:332:baoloi(ads_id, object_id, account_id, job_type)
        continue #line:333:continue
    try :#line:335:try:
        if adbyn =="1":#line:336:if adbyn == "1":
            os .system (f'adb shell am start -a android.intent.action.VIEW -d "{link}" > /dev/null 2>&1')#line:337:os.system(f'adb shell am start -a android.intent.action.VIEW -d "{link}" > /dev/null 2>&1')
        else :#line:338:else:
            subprocess .run (["termux-open-url",link ])#line:340:subprocess.run(["termux-open-url", link])
        for remaining in range (3 ,0 ,-1 ):#line:341:for remaining in range(3, 0, -1):
            time .sleep (1 )#line:342:time.sleep(1)
        print ("\r"+" "*30 +"\r",end ="")#line:343:print("\r" + " " * 30 + "\r", end="")
    except Exception as e :#line:344:except Exception as e:
        baoloi (ads_id ,object_id ,account_id ,job_type )#line:345:baoloi(ads_id, object_id, account_id, job_type)
        continue #line:346:continue
    if job_type =="like"and adbyn =="1"and x_like and y_like :#line:348:if job_type == "like" and adbyn == "1" and x_like and y_like:
        os .system (f"adb shell input tap {x_like} {y_like}")#line:349:os.system(f"adb shell input tap {x_like} {y_like}")
    elif job_type =="follow"and adbyn =="1"and x_follow and y_follow :#line:350:elif job_type == "follow" and adbyn == "1" and x_follow and y_follow:
        os .system (f"adb shell input tap {x_follow} {y_follow}")#line:351:os.system(f"adb shell input tap {x_follow} {y_follow}")
    for remaining_time in range (delay ,-1 ,-1 ):#line:353:for remaining_time in range(delay, -1, -1):
        color ="\033[1;36m"if remaining_time %2 ==0 else "\033[1;33m"#line:354:color = "\033[1;36m" if remaining_time % 2 == 0 else "\033[1;33m"
        print (f"\r{color}Time | ○.O | {remaining_time}s           ",end ="")#line:355:print(f"\r{color}time | ○.O | {remaining_time}s           ", end="")
        time .sleep (1 )#line:356:time.sleep(1)
    print ("\r                          \r",end ="")#line:357:print("\r                          \r", end="")
    print ("\033[1;35mĐang Buss    ",end ="\r")#line:358:print("\033[1;35mĐang Buss    ",end = "\r")
    max_attempts =2 #line:360:max_attempts = 2
    attempts =0 #line:361:attempts = 0
    nhantien =None #line:362:nhantien = None
    while attempts <max_attempts :#line:363:while attempts < max_attempts:
        try :#line:364:try:
            nhantien =hoanthanh (ads_id ,account_id )#line:365:nhantien = hoanthanh(ads_id, account_id)
            if nhantien and nhantien .get ("status")==200 :#line:366:if nhantien and nhantien.get("status") == 200:
                break #line:367:break
        except :#line:368:except:
            pass #line:369:pass
        attempts +=1 #line:370:attempts += 1
    if nhantien and nhantien .get ("status")==200 :#line:371:if nhantien and nhantien.get("status") == 200:
        dem +=1 #line:372:dem += 1
        tien =nhantien ["data"]["prices"]#line:373:tien = nhantien["data"]["prices"]
        tong +=tien #line:374:tong += tien
        local_time =time .localtime ()#line:375:local_time = time.localtime()
        hour =local_time .tm_hour #line:376:hour = local_time.tm_hour
        minute =local_time .tm_min #line:377:minute = local_time.tm_min
        second =local_time .tm_sec #line:378:second = local_time.tm_sec
        h =hour #line:379:h = hour
        m =minute #line:380:m = minute
        s =second #line:381:s = second
        if hour <10 :#line:382:if hour < 10:
            h ="0"+str (hour )#line:383:h = "0" + str(hour)
        if minute <10 :#line:384:if minute < 10:
            m ="0"+str (minute )#line:385:m = "0" + str(minute)
        if second <10 :#line:386:if second < 10:
            s ="0"+str (second )#line:387:s = "0" + str(second)
        chuoi =(f"\033[1;31m| \033[1;36m{dem}" f" \033[1;37m| \033[1;33m{h}:{m}:{s}" f" \033[1;37m| \033[1;32msuccess" f" \033[1;37m| \033[1;31m{job_type}" f" \033[1;37m| \033[1;32mẨn ID" f" \033[1;37m| \033[1;32m+{tien}" f" \033[1;37m| \033[1;33m{tong}")#line:394:f" \033[1;37m| \033[1;33m{tong}")
        print ("                                                    ",end ="\r")#line:395:print("                                                    ", end="\r")
        print (chuoi )#line:396:print(chuoi)
        time .sleep (0.7 )#line:397:time.sleep(0.7)
        checkdoiacc =0 #line:398:checkdoiacc = 0
    else :#line:399:else:
        try :#line:400:try:
            baoloi (ads_id ,object_id ,account_id ,nhanjob ["data"]["type"])#line:401:baoloi(ads_id, object_id, account_id, nhanjob["data"]["type"])
            print ("                                              ",end ="\r")#line:402:print("                                              ", end="\r")
            print ("\033[1;31mBỏ qua nhiệm vụ ",end ="\r")#line:403:print("\033[1;31mBỏ qua nhiệm vụ ", end="\r")
            sleep (1 )#line:404:sleep(1)
            checkdoiacc +=1 #line:405:checkdoiacc += 1
        except :#line:406:except:
            pass #line:407:pass
