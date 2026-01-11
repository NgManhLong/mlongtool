import os
import sys
import time
import json
import random
import requests
from datetime import datetime
# thư viện
import json
import os
import sys
import time
import requests
from bs4 import BeautifulSoup
from pystyle import Write, Colors, Colorate
from datetime import datetime
import cloudscraper
import socket
import subprocess
from time import strftime
from time import sleep
from datetime import datetime, timedelta
from bs4 import BeautifulSoup
from colorama import Fore, init
import subprocess
from rich.console import Console
from rich.panel import Panel
from rich.console import Console
from rich.text import Text
import requests, re, os, json, base64, uuid, random, sys
from time import sleep
from datetime import datetime
from pystyle import Colors, Colorate
from bs4 import BeautifulSoup
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

# --- CẤU HÌNH MÀU SẮC ---
class Color:
    RESET = "\033[0m"
    BLACK = "\033[0;30m"
    RED = "\033[1;31m"
    GREEN = "\033[1;32m"
    YELLOW = "\033[1;33m"
    BLUE = "\033[1;34m"
    PURPLE = "\033[1;35m"
    CYAN = "\033[1;36m"
    WHITE = "\033[1;37m"

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
    
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def delay_wait(seconds, message="Chờ"):
    for i in range(seconds, -1, -1):
        time_str = datetime.now().strftime("%H:%M:%S")
        print(f'{Color.YELLOW}[{time_str}] {Color.CYAN}{message} {Color.RED}| {Color.WHITE}{i}s {Color.RED}|', end='\r')
        time.sleep(1)
    print(' ' * 60, end='\r') # Xóa dòng đếm ngược

# --- XỬ LÝ TRAODOISUB ---
class Traodoisub:
    def __init__(self, token):
        self.token = token
        self.base_url = "https://traodoisub.com/api/"

    def get_info(self):
        try:
            res = requests.get(f'{self.base_url}?fields=profile&access_token={self.token}').json()
            if 'success' in res:
                return res['data']
            return None
        except:
            return None

    def set_running_acc(self, id_instagram):
        try:
            res = requests.get(f'{self.base_url}?fields=instagram_run&id={id_instagram}&access_token={self.token}').json()
            return 'success' in res
        except:
            return False

    def get_jobs(self, job_type):
        # job_type: 'instagram_follow' hoặc 'instagram_like'
        try:
            res = requests.get(f'{self.base_url}?fields={job_type}&access_token={self.token}').json()
            return res.get('data', [])
        except:
            return []

    def cache_job(self, job_type_cache, job_id):
        # job_type_cache: 'INS_FOLLOW_CACHE' hoặc 'INS_LIKE_CACHE'
        try:
            res = requests.get(f'{self.base_url}coin/?type={job_type_cache}&id={job_id}&access_token={self.token}').json()
            return res
        except:
            return {}

# --- XỬ LÝ INSTAGRAM ---
class InstagramAPI:
    def __init__(self, cookie, user_agent=None, proxy=None):
        self.cookie = cookie
        self.proxy = proxy
        self.user_agent = user_agent if user_agent else 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36'
        try:
            self.csrftoken = cookie.split('csrftoken=')[1].split(';')[0]
            self.ds_user_id = cookie.split('ds_user_id=')[1].split(';')[0]
        except:
            self.csrftoken = ""
            self.ds_user_id = ""

    def _get_proxies(self):
        if self.proxy:
            return {'http': f'http://{self.proxy}', 'https': f'http://{self.proxy}'}
        return None

    def get_username(self):
        headers = {
            'authority': 'www.instagram.com',
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
            'cookie': self.cookie,
            'user-agent': self.user_agent
        }
        try:
            res = requests.get('https://www.instagram.com/', headers=headers, proxies=self._get_proxies(), timeout=10).text
            if 'class="no-js' in res:
                return "DIE"
            # Parse username đơn giản (có thể cần regex nếu IG đổi giao diện)
            if 'username' in res:
                return res.split('username')[1].split('"')[2].split("\\")[0]
            return "UNKNOWN"
        except:
            return "ERROR"

    def follow(self, user_id):
        url = f'https://i.instagram.com/api/v1/web/friendships/{user_id}/follow/'
        headers = {
            'authority': 'i.instagram.com',
            'accept': '*/*',
            'content-type': 'application/x-www-form-urlencoded',
            'cookie': self.cookie,
            'origin': 'https://www.instagram.com',
            'referer': 'https://www.instagram.com/',
            'user-agent': self.user_agent,
            'x-csrftoken': self.csrftoken,
            'x-ig-app-id': '936619743392459',
            'x-instagram-ajax': '1006309104',
        }
        try:
            res = requests.post(url, headers=headers, proxies=self._get_proxies(), timeout=15).json()
            return res.get('status') == 'ok'
        except:
            return False

    def like(self, media_id, link_post):
        url = f'https://www.instagram.com/web/likes/{media_id}/like/'
        headers = {
            'authority': 'www.instagram.com',
            'accept': '*/*',
            'content-type': 'application/x-www-form-urlencoded',
            'cookie': self.cookie,
            'origin': 'https://www.instagram.com',
            'referer': link_post,
            'user-agent': self.user_agent,
            'x-csrftoken': self.csrftoken,
            'x-asbd-id': '198387',
        }
        try:
            res = requests.post(url, headers=headers, proxies=self._get_proxies(), timeout=15).text
            return '"status":"ok"' in res
        except:
            return False

# --- HÀM MAIN ---
def main():
    clear_screen()
    banner()

    # 1. Cấu hình User Agent
    user_agents = []
    if os.path.exists('ua.txt'):
        with open('ua.txt', 'r') as f:
            user_agents = [line.strip() for line in f.readlines() if line.strip()]
    
    # 2. Login TDS
    token_tds = ""
    if os.path.exists("configtds.txt"):
        with open("configtds.txt", "r") as f:
            token_tds = f.read().strip()
    
    if token_tds:
        print(f'{Color.YELLOW}[?] Nhập [1] Giữ Token cũ | [2] Nhập Token mới: ', end='')
        choice = input(f'{Color.RED}')
        if choice == '2':
            token_tds = input(f'{Color.CYAN}Nhập Token TDS: {Color.RED}').strip()
            with open("configtds.txt", "w") as f: f.write(token_tds)
    else:
        token_tds = input(f'{Color.CYAN}Nhập Token TDS: {Color.RED}').strip()
        with open("configtds.txt", "w") as f: f.write(token_tds)

    tds = Traodoisub(token_tds)
    info = tds.get_info()
    if info:
        print(f'{Color.GREEN}➤ Login thành công: {Color.YELLOW}{info["user"]} {Color.GREEN}| Xu: {Color.YELLOW}{info["xu"]}')
    else:
        print(f'{Color.RED}Token lỗi! Vui lòng kiểm tra lại.')
        sys.exit()

    # 3. Nhập danh sách tài khoản
    list_cookies = []
    print(f'\n{Color.CYAN}1. Nhập cookie thủ công')
    print(f'{Color.CYAN}2. Nhập từ file')
    choice_input = input(f'{Color.YELLOW}Chọn: {Color.RED}')
    
    if choice_input == '1':
        while True:
            ck = input(f'{Color.CYAN}Nhập Cookie (Enter để dừng): {Color.WHITE}')
            if not ck: break
            list_cookies.append(ck)
    elif choice_input == '2':
        filename = input(f'{Color.CYAN}Tên file cookie: {Color.WHITE}')
        try:
            with open(filename, 'r') as f:
                list_cookies = [line.strip() for line in f.readlines() if line.strip()]
        except:
            print(f'{Color.RED}Không tìm thấy file!')
            sys.exit()

    # 4. Cấu hình nhiệm vụ
    do_follow = input(f'{Color.CYAN}Làm Follow? (y/n): {Color.WHITE}').lower() == 'y'
    if do_follow:
        count_follow = int(input(f'{Color.CYAN}Số lượng Follow/Acc: {Color.WHITE}'))
        delay_follow = int(input(f'{Color.CYAN}Delay Follow: {Color.WHITE}'))
    
    do_like = input(f'{Color.CYAN}Làm Like? (y/n): {Color.WHITE}').lower() == 'y'
    if do_like:
        count_like = int(input(f'{Color.CYAN}Số lượng Like/Acc: {Color.WHITE}'))
        delay_like = int(input(f'{Color.CYAN}Delay Like: {Color.WHITE}'))

    change_acc_delay = int(input(f'{Color.CYAN}Thời gian nghỉ chuyển Acc: {Color.WHITE}'))

    # 5. Cấu hình Proxy
    list_proxies = []
    use_proxy = input(f'{Color.CYAN}Dùng Proxy? (y/n): {Color.WHITE}').lower() == 'y'
    if use_proxy:
        proxy_file = input(f'{Color.CYAN}Tên file Proxy: {Color.WHITE}')
        try:
            with open(proxy_file, 'r') as f:
                list_proxies = [line.strip() for line in f.readlines() if line.strip()]
        except:
            print(f'{Color.RED}Không tìm thấy file Proxy!')

    # --- VÒNG LẶP CHÍNH ---
    while True: # Vòng lặp vĩnh cửu (hết list acc thì quay lại từ đầu)
        if not list_cookies:
            print(f'{Color.RED}Hết cookie để chạy!')
            break

        for i, cookie in enumerate(list_cookies):
            current_proxy = random.choice(list_proxies) if list_proxies else None
            current_ua = random.choice(user_agents) if user_agents else None
            
            ig = InstagramAPI(cookie, current_ua, current_proxy)
            
            # Check Live/Die và lấy username
            print(f'{Color.BLUE}➤ Đang check account {i+1}...', end='\r')
            username = ig.get_username()
            
            if username == "DIE":
                print(f'{Color.RED}Account {i+1} Cookie Die -> Bỏ qua.')
                continue
            elif username == "ERROR":
                print(f'{Color.RED}Account {i+1} Lỗi kết nối -> Bỏ qua.')
                continue

            # Cấu hình vào TDS
            if tds.set_running_acc(ig.ds_user_id):
                print(f'{Color.GREEN}Account: {Color.YELLOW}{username} {Color.GREEN}--> Cấu hình TDS thành công!')
            else:
                print(f'{Color.RED}Account: {username} --> Cấu hình thất bại! (Có thể chưa thêm vào TDS)')
                continue

            # --- NHIỆM VỤ FOLLOW ---
            if do_follow:
                done_follow = 0
                while done_follow < count_follow:
                    jobs = tds.get_jobs('instagram_follow')
                    if not jobs:
                        print(f'{Color.RED}Hết job Follow tạm thời...')
                        break
                    
                    for job in jobs:
                        job_id = job['id']
                        target_id = job_id.split('_')[0]
                        
                        time_now = datetime.now().strftime("%H:%M:%S")
                        print(f'{Color.YELLOW}[FOLLOW] {Color.WHITE}{target_id} {Color.BLUE}--> ', end='')
                        
                        if ig.follow(target_id):
                            print(f'{Color.GREEN}OK', end='')
                            
                            # Nhận xu
                            res_coin = tds.cache_job('INS_FOLLOW_CACHE', job_id)
                            msg = res_coin.get('data', {}).get('msg', 'Pending...')
                            pending = res_coin.get('data', {}).get('pending', 0)
                            print(f' {Color.CYAN}| {msg} | Pending: {pending}')
                            
                            done_follow += 1
                            delay_wait(delay_follow, "Nghỉ Follow")
                        else:
                            print(f'{Color.RED}FAIL')
                            delay_wait(5, "Lỗi thao tác")

                        if done_follow >= count_follow:
                            break
            
            # --- NHIỆM VỤ LIKE ---
            if do_like:
                done_like = 0
                while done_like < count_like:
                    jobs = tds.get_jobs('instagram_like')
                    if not jobs:
                        print(f'{Color.RED}Hết job Like tạm thời...')
                        break

                    for job in jobs:
                        job_id = job['id']
                        target_id = job_id.split('_')[0]
                        link_post = job['link']

                        time_now = datetime.now().strftime("%H:%M:%S")
                        print(f'{Color.YELLOW}[LIKE] {Color.WHITE}{target_id} {Color.BLUE}--> ', end='')

                        if ig.like(target_id, link_post):
                            print(f'{Color.GREEN}OK', end='')

                            # Nhận xu
                            res_coin = tds.cache_job('INS_LIKE_CACHE', job_id)
                            msg = res_coin.get('data', {}).get('msg', 'Pending...')
                            pending = res_coin.get('data', {}).get('pending', 0)
                            print(f' {Color.CYAN}| {msg} | Pending: {pending}')

                            done_like += 1
                            delay_wait(delay_like, "Nghỉ Like")
                        else:
                            print(f'{Color.RED}FAIL')
                            delay_wait(5, "Lỗi thao tác")
                        
                        if done_like >= count_like:
                            break

            # Chuyển acc
            print(f'{Color.PURPLE}Hoàn thành acc {username}.')
            delay_wait(change_acc_delay, "Chuyển tài khoản tiếp theo")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print(f'\n{Color.RED}Đã dừng tool bởi người dùng!')
        sys.exit()