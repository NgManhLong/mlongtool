import requests
import os
import sys
import time
from time import sleep
from datetime import datetime
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


# wed làm banner

# https://patorjk.com/software/taag/
# https://www.ascii-art-generator.org/

# banner


    

# --- CẤU HÌNH MÀU SẮC ---
class Color:
    R = "\033[1;31m"    # Red
    G = "\033[1;32m"    # Green
    Y = "\033[1;33m"    # Yellow
    C = "\033[1;36m"    # Cyan
    W = "\033[1;37m"    # White
    RESET = "\033[0m"

def banner():
    os.system('cls' if os.name=='nt' else 'clear')
    tool = ""
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
{d}══════════════════════════════════════════════════════''')

class FacebookIDFinder:
    def __init__(self):
        self.api_url = 'https://id.traodoisub.com/api.php'
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36',
            'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
            'Accept': 'application/json, text/javascript, */*; q=0.01',
            'Referer': 'https://id.traodoisub.com/',
            'X-Requested-With': 'XMLHttpRequest',
            'Origin': 'https://id.traodoisub.com'
        }

    def get_id(self, link):
        data = {'link': link}
        try:
            print(f"{Color.Y}➤ Đang xử lý...", end='\r')
            response = requests.post(self.api_url, headers=self.headers, data=data, timeout=10)
            
            if response.status_code == 200:
                try:
                    json_data = response.json()
                    if 'id' in json_data:
                        return json_data['id']
                    elif 'error' in json_data:
                        return f"Error: {json_data['error']}"
                    else:
                        return "Không tìm thấy ID"
                except requests.exceptions.JSONDecodeError:
                    return "API trả về dữ liệu lỗi (Không phải JSON)"
            else:
                return f"Lỗi Server: {response.status_code}"
        except requests.exceptions.RequestException as e:
            return f"Lỗi kết nối: {e}"

    def run(self):
        banner()
        while True:
            print(f"{Color.C}────────────────────────────────────────────────────────────")
            link = input(f"{Color.G}Nhập Link Facebook (Enter để thoát): {Color.W}").strip()
            
            if not link:
                print(f"{Color.R}Đã thoát tool.")
                break

            uid = self.get_id(link)
            
            if "Error" in uid or "Lỗi" in uid or "Không" in uid:
                 print(f"{Color.R}➤ {uid}")
            else:
                 print(f"{Color.G}➤ ID CỦA BẠN LÀ: {Color.Y}{uid}")

if __name__ == "__main__":
    try:
        tool = FacebookIDFinder()
        tool.run()
    except KeyboardInterrupt:
        print(f"\n{Color.R}Dừng tool thành công!")