import os
import sys
import time
import json
import requests
import random
from datetime import datetime

# --- CẤU HÌNH MÀU SẮC ---
class Color:
    R = "\033[1;31m"    # Đỏ
    G = "\033[1;32m"    # Xanh lá
    Y = "\033[1;33m"    # Vàng
    B = "\033[1;34m"    # Xanh dương
    P = "\033[1;35m"    # Tím
    C = "\033[1;36m"    # Xanh lơ
    W = "\033[1;37m"    # Trắng
    D = "\033[1;90m"    # Xám/Đen
    RESET = "\033[0m"

# --- HÀM HỖ TRỢ GIAO DIỆN ---
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def banner():
    clear_screen()
    time_now = datetime.now().strftime('%d/%m/%Y %H:%M:%S')
    print(f'''{Color.P}
███╗░░░███╗██╗░░░░░░█████╗░███╗░░██╗░██████╗░
{Color.W}████╗░████║██║░░░░░██╔══██╗████╗░██║██╔════╝░
{Color.P}██╔████╔██║██║░░░░░██║░░██║██╔██╗██║██║░░██╗░
{Color.W}██║╚██╔╝██║██║░░░░░██║░░██║██║╚████║██║░░╚██╗
{Color.P}██║░╚═╝░██║███████╗╚█████╔╝██║░╚███║╚██████╔╝
{Color.W}╚═╝░░░░░╚═╝╚══════╝░╚════╝░╚═╝░░╚══╝░╚═════╝░
{Color.D}══════════════════════════════════════════════════════
{Color.R}[{Color.W}=.={Color.R}] {Color.W}Tool    : {Color.G}TraoDoiSub TikTok
{Color.R}[{Color.W}=.={Color.R}] {Color.W}Ngày    : {Color.C}{time_now}
{Color.R}[{Color.W}=.={Color.R}] {Color.W}Admin   : {Color.Y}Nguyễn Mạnh Long
{Color.R}[{Color.W}=.={Color.R}] {Color.W}Chất Lượng Xây Dựng Niềm Tin
{Color.D}══════════════════════════════════════════════════════{Color.RESET}''')

def delay(seconds, message="Vui lòng chờ"):
    for i in range(seconds, 0, -1):
        print(f'{Color.Y}[Wait] {Color.C}{message}... {Color.R}| {Color.W}{i}s {Color.R}|', end='\r')
        time.sleep(1)
    print(' ' * 70, end='\r') # Xóa dòng delay sau khi chạy xong

def open_link(link):
    # Hỗ trợ mở link trên cả Termux và Windows
    try:
        if sys.platform.startswith('linux'):
            if 'termux' in os.environ.get('PREFIX', ''):
                os.system(f'xdg-open "{link}" > /dev/null 2>&1')
            else:
                os.system(f'xdg-open "{link}"')
        else:
            os.system(f'start "" "{link}"')
    except:
        pass

# --- API TRAODOISUB ---
class TraoDoiSub:
    def __init__(self, token):
        self.token = token
        self.base_url = "https://traodoisub.com/api/"
        self.session = requests.Session()
        # Thêm Header để giống trình duyệt thật
        self.session.headers.update({
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36'
        })

    def get_profile(self):
        try:
            res = self.session.get(f'{self.base_url}?fields=profile&access_token={self.token}').json()
            return res.get('data')
        except Exception as e:
            return None

    def configure_tiktok(self, user_tiktok):
        try:
            res = self.session.get(f'{self.base_url}?fields=tiktok_run&id={user_tiktok}&access_token={self.token}').json()
            return res.get('data')
        except:
            return None

    def get_jobs(self, job_type):
        try:
            res = self.session.get(f'{self.base_url}?fields={job_type}&access_token={self.token}').json()
            return res
        except:
            return []

    def cache_job(self, cache_type, job_id):
        try:
            res = self.session.get(f'{self.base_url}coin/?type={cache_type}&id={job_id}&access_token={self.token}').json()
            return 'cache' in res
        except:
            return False

    def claim_coin(self, claim_type, claim_api):
        try:
            res = self.session.get(f'{self.base_url}coin/?type={claim_type}&id={claim_api}&access_token={self.token}').json()
            return res.get('data') if 'data' in res else res
        except:
            return None

# --- CHƯƠNG TRÌNH CHÍNH ---
def main():
    banner()
    
    # --- ĐĂNG NHẬP ---
    token = ""
    if os.path.exists('configtds.txt'):
        with open('configtds.txt', 'r') as f:
            token = f.read().strip()
    
    api = None
    
    # Kiểm tra token cũ
    if token:
        api = TraoDoiSub(token)
        profile = api.get_profile()
        if profile:
            print(f"{Color.G}User: {Color.Y}{profile['user']} {Color.G}| Xu: {Color.Y}{profile['xu']}")
            print(f"{Color.D}--------------------------------------------------")
            print(f"{Color.C}[1] {Color.W}Tiếp tục chạy tài khoản này")
            print(f"{Color.C}[2] {Color.W}Đăng nhập tài khoản mới")
            choice = input(f"{Color.Y}Lựa chọn: {Color.W}")
            if choice == '2':
                token = ""
        else:
            print(f"{Color.R}Token cũ lỗi hoặc hết hạn!")
            token = ""

    # Nhập token mới nếu chưa có
    while not token:
        token = input(f"{Color.G}Nhập Access_Token TDS: {Color.W}").strip()
        api = TraoDoiSub(token)
        profile = api.get_profile()
        if profile:
            with open('configtds.txt', 'w') as f:
                f.write(token)
            print(f"{Color.G}Đăng nhập thành công: {Color.Y}{profile['user']}")
            break
        else:
            print(f"{Color.R}Token sai! Vui lòng nhập lại.")
            token = ""

    total_xu = int(profile['xu'])
    
    # --- CẤU HÌNH USER CHẠY ---
    print(f"{Color.D}══════════════════════════════════════════════════════")
    while True:
        tiktok_id = input(f"{Color.C}Nhập ID TikTok để chạy (VD: user123): {Color.W}").strip()
        if not tiktok_id: continue
        
        cfg = api.configure_tiktok(tiktok_id)
        if cfg:
            print(f"{Color.G}Cấu hình thành công ID: {Color.Y}{cfg['uniqueID']}")
            break
        else:
            print(f"{Color.R}Cấu hình thất bại! Kiểm tra lại ID hoặc user chưa thêm vào TDS.")

    # --- CHỌN CHẾ ĐỘ ---
    print(f"{Color.D}══════════════════════════════════════════════════════")
    print(f"{Color.C}[1] {Color.W}Auto Like TikTok")
    print(f"{Color.C}[2] {Color.W}Auto Follow TikTok")
    
    while True:
        mode = input(f"{Color.Y}Chọn chế độ (1/2): {Color.W}").strip()
        if mode in ['1', '2']: break

    while True:
        try:
            delay_time = int(input(f"{Color.C}Nhập Delay (giây): {Color.W}"))
            max_job = int(input(f"{Color.C}Làm bao nhiêu job thì nhận xu (8-20): {Color.W}"))
            break
        except ValueError:
            print(f"{Color.R}Vui lòng nhập số!")

    # Thiết lập biến dựa trên chế độ
    if mode == '1':
        job_type = 'tiktok_like'
        cache_type = 'TIKTOK_LIKE_CACHE'
        claim_api = 'TIKTOK_LIKE_API'
        claim_code = 'TIKTOK_LIKE'
        log_text = 'LIKE'
    else:
        job_type = 'tiktok_follow'
        cache_type = 'TIKTOK_FOLLOW_CACHE'
        claim_api = 'TIKTOK_FOLLOW_API'
        claim_code = 'TIKTOK_FOLLOW'
        log_text = 'FOLLOW'

    # --- VÒNG LẶP CHẠY JOB ---
    banner()
    print(f"{Color.P}Đang chạy user: {Color.W}{tiktok_id} {Color.P}| Mode: {Color.W}{log_text}")
    print(f"{Color.D}══════════════════════════════════════════════════════")
    
    job_count_session = 0

    while True:
        # Lấy danh sách nhiệm vụ
        jobs_data = api.get_jobs(job_type)

        # Xử lý lỗi trả về
        if isinstance(jobs_data, dict) and 'error' in jobs_data:
            err_msg = jobs_data['error']
            
            if 'countdown' in jobs_data:
                wait_sec = int(jobs_data['countdown'])
                delay(wait_sec, "Thao tác quá nhanh")
                continue
            
            print(f"{Color.R}Thông báo TDS: {err_msg}")
            
            if 'NHẬN TẤT CẢ' in str(err_msg).upper():
                 api.claim_coin(claim_api, claim_code)
                 delay(5, "Đang nhận xu tồn đọng")
                 continue
                 
            delay(10, "Đang thử lại")
            continue

        # Kiểm tra nếu có job
        if isinstance(jobs_data, list) and len(jobs_data) > 0:
            print(f"{Color.G}Tìm thấy {len(jobs_data)} nhiệm vụ...", end='\r')
            
            for job in jobs_data:
                job_id = job['id']
                link = job['link']
                
                # Mở link
                open_link(link)
                
                # Gửi cache (xác nhận đã làm)
                if api.cache_job(cache_type, job_id):
                    job_count_session += 1
                    time_curr = datetime.now().strftime('%H:%M:%S')
                    print(f"{Color.Y}[{job_count_session}] {Color.R}| {Color.C}{time_curr} {Color.R}| {Color.P}{log_text} {Color.R}| {Color.W}{job_id}")
                    
                    delay(delay_time, "Đang chờ")
                    
                    # Logic nhận xu
                    if job_count_session % max_job == 0:
                        res_claim = api.claim_coin(claim_api, claim_code)
                        if res_claim and 'xu_them' in res_claim:
                            xu_them = res_claim['xu_them']
                            total_xu += int(xu_them)
                            msg = res_claim.get('msg', 'Thành công')
                            print(f"{Color.G}──────────────────────────────────────────────────")
                            print(f"{Color.G}NHẬN XU: {Color.Y}+{xu_them} {Color.G}| {msg}")
                            print(f"{Color.G}TỔNG XU: {Color.Y}{total_xu}")
                            print(f"{Color.G}──────────────────────────────────────────────────")
                            delay(3, "Nghỉ ngơi chút")
                else:
                    print(f"{Color.R}[X] Lỗi cache nhiệm vụ: {job_id}")
        else:
            delay(5, "Không tìm thấy nhiệm vụ, đang load lại")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print(f"\n{Color.R}Đã dừng tool!")
        sys.exit()