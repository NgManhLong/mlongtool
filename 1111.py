import sys
import os
import time
import json
import random
import threading
import urllib.parse
import importlib.util
import requests
from datetime import datetime

# --- TỰ ĐỘNG CÀI MODULE NẾU THIẾU ---
def install_modules():
    modules = ['requests', 'colorama', 'pystyle', 'cloudscraper', 'getuseragent', 'fake_useragent', 'bs4']
    for mod in modules:
        if importlib.util.find_spec(mod) is None:
            print(f"📦 Đang cài module: {mod} ...")
            os.system(f'pip install {mod}')

install_modules()

# Import sau khi đảm bảo đã cài đặt
try:
    from pystyle import Colors, Colorate, Center
    import cloudscraper
    import getuseragent
    from bs4 import BeautifulSoup
except ImportError:
    print("Vui lòng chạy lại tool để nhận module mới cài đặt.")
    sys.exit()

# --- CẤU HÌNH MÀU SẮC ---
red = "\033[1;31m"
green = "\033[1;32m"
yellow = "\033[1;33m"
blue = "\033[1;34m"
purple = "\033[1;35m"
cyan = "\033[1;36m"
white = "\033[1;37m"
reset = "\033[0m"

icon2 = f"{yellow}•[۞] ➭ : {white}"

# --- GIAO DIỆN ---
def clean_bar():
    os.system('cls' if os.name == 'nt' else 'clear')

def banner2():
    clean_bar()
    logo = r'''
     _____  .____                     
    /     \ |    |    ____   ____    ____  
   /  \ /  \|    |   /  _ \ /    \  / ___\ 
  /    Y    \    |__(  <_> )   |  \/ /_/  >
  \____|__  /_______ \____/|___|  /\___  / 
          \/        \/          \//_____/  
┌───────────────────────────────────────┐
│ Admin    : Nguyễn Mạnh Long           │
│ Tool     : Golike Instagram Auto      │
│ Phiên bản: Optimized Fix v1.0         │
└───────────────────────────────────────┘'''
    print(Colorate.Horizontal(Colors.blue_to_purple, Center.XCenter(logo)))

# --- CLASS GOLIKE ---
class Golike_INSTA:
    def __init__(self, account_id, athor, req=None, UserAgent=None):
        self.UserAgent = UserAgent or 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Mobile Safari/537.36'
        self.header = {
            'Host': 'gateway.golike.net',
            'Accept': 'application/json, text/plain, */*',
            'Authorization': athor,
            'Content-Type': 'application/json;charset=UTF-8',
            'Origin': 'https://app.golike.net',
            'T': 'VFZSamVVMVVVVEJQVkdOM1RWRTlQUT09',
            'User-Agent': self.UserAgent
        }
        self.req = req if req else requests.Session()
        self.account_id = account_id
        
    def get_jobs(self):
        try:
            url = f'https://gateway.golike.net/api/advertising/publishers/instagram/jobs?instagram_account_id={self.account_id}&data=null'
            response = self.req.get(url, headers=self.header, timeout=15).json()
            
            # FIX LỖI: Kiểm tra xem có data không trước khi truy cập
            if response.get("status") != 200 or not response.get("data"):
                return {"trangthai": False, "msg": response.get("message", "Lỗi lấy job")}

            data = response["data"]
            self.link = data.get("link")
            self.id_jobs = data.get("id")
            self.ty = data.get("package_name")
            self.price = data.get('price_per_after_cost')
            self.object_id = data.get('object_id')
            
            result = {
                "trangthai": True,
                "id_jobs": self.id_jobs,
                "link": self.link,
                "type": self.ty,
                "coin": self.price,
                "object_id": self.object_id
            }

            if self.ty == 'comment':
                self.idcmt = str(data['comment_run']['id'])
                self.ndungcmt = str(data['comment_run']['message'])
                # Xử lý nội dung comment an toàn hơn
                self.ndung_ht = self.ndungcmt 
                result.update({"id_cmt": self.idcmt, "ndung_cmt": self.ndungcmt})
            
            return result
        except Exception as e:
            return {"trangthai": False, "msg": str(e)}

    def hoan_thanh(self):
        try:
            body = {
                "instagram_users_advertising_id": self.id_jobs,
                "instagram_account_id": self.account_id,
                "async": True,
                "data": None
            }
            if self.ty == 'comment':
                body.update({
                    "comment_id": self.idcmt,
                    "message": self.ndung_ht
                })
            
            response = self.req.post(
                'https://gateway.golike.net/api/advertising/publishers/instagram/complete-jobs',
                headers=self.header,
                json=body,
                timeout=15
            ).json()
            
            if response.get("status") == 200:
                return {"trangthai": True}
            return {"trangthai": False}
        except:
            return {"trangthai": False}

    def bao_loi(self):
        try:
            data = {
                "ads_id": self.id_jobs,
                "object_id": f"{self.object_id}",
                "account_id": self.account_id,
                "type": self.ty
            }
            self.req.post(
                'https://gateway.golike.net/api/advertising/publishers/instagram/skip-jobs',
                json=data,
                headers=self.header,
                timeout=10
            )
            return {"trangthai": True}
        except:
            return {"trangthai": False}

# --- CLASS INSTAGRAM ---
class INSTAGRAM_REQ:
    def __init__(self, cookie, req=None, useragent='Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36'):
        self.cookie = cookie
        self.req = req if req else requests.Session()
        self.useragent = useragent
        self.header = {
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8',
            'cookie': self.cookie,
            'user-agent': self.useragent,
            'viewport-width': '912',
            'sec-fetch-dest': 'document',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-site': 'none',
        }
        try:
            self.csrftoken = cookie.split('csrftoken=')[1].split(';')[0].strip()
        except:
            self.csrftoken = ""

    def check_username(self):
        try:
            # Dùng API private thay vì parse HTML profile để chính xác hơn
            # Hoặc parse nhẹ nhàng hơn
            text = self.req.get('https://www.instagram.com/api/v1/users/web_profile_info/?username=instagram', headers=self.header, timeout=10).text
            # Cách cũ của bạn: parse từ trang profile.php
            text = self.req.get('https://www.instagram.com/profile.php', headers=self.header, timeout=15).text
            if 'Login • Instagram' in text or 'checkpoint' in text:
                return 'none'
            username_ig = text.split('"username":"')[1].split('"')[0]
            # Convert unicode escape sequence if needed
            return username_ig.encode('utf-8').decode('unicode_escape')
        except:
            return 'none'

    def _get_common_vars(self, url):
        # FIX LỖI: Thêm try-except để tránh crash khi IG đổi code
        try:
            get = self.req.get(url, headers=self.header, timeout=15).text
            return {
                "av": get.split('"actorID":"')[1].split('"')[0],
                "hs": get.split('"haste_session":"')[1].split('"')[0],
                "hsi": get.split('"hsi":"')[1].split('"')[0],
                "rev": get.split('"__spin_r":')[1].split(',')[0],
                "spin_t": get.split('"__spin_t":')[1].split(',')[0],
                "fb_dtsg": get.split('"DTSGInitData"')[1].split('"token":"')[1].split('"')[0],
                "lsd": get.split('"LSD",')[1].split('"token":"')[1].split('"')[0],
                "jazoest": get.split('&jazoest=')[1].split('"')[0].split('&')[0],
                "versioningID": get.split('"versioningID":"')[1].split('"')[0],
                "app_id": get.split('"X-IG-App-ID":"')[1].split('"')[0],
                "full_text": get
            }
        except IndexError:
            # Lỗi parsing (có thể do cookie die, checkpoint, hoặc IG đổi source)
            raise Exception("HTML Parsing Error")

    def make_graphql_request(self, url, data, vars_dict, friendly_name):
        header_req = {
            'accept-language': 'en-US,en;q=0.9',
            'content-length': str(len(data)),
            'content-type': 'application/x-www-form-urlencoded',
            'cookie': self.cookie,
            'origin': 'https://www.instagram.com',
            'referer': url,
            'user-agent': self.useragent,
            'x-csrftoken': self.csrftoken,
            'x-fb-friendly-name': friendly_name,
            'x-fb-lsd': vars_dict["lsd"],
            'x-ig-app-id': vars_dict["app_id"],
        }
        return self.req.post('https://www.instagram.com/graphql/query', data=data, headers=header_req, timeout=15).text

    def follow(self, url):
        try:
            v = self._get_common_vars(url)
            id_fl = v["full_text"].split('"profile_id":"')[1].split('"')[0]
            
            data = (f'av={v["av"]}&__d=www&__user=0&__a=1&__req=y&__hs={urllib.parse.quote(v["hs"])}'
                    f'&dpr=1&__ccg=UNKNOWN&__rev={v["rev"]}&__s=2jf96v%3Atu2kai%3Azcd8rn&__hsi={v["hsi"]}'
                    f'&fb_dtsg={urllib.parse.quote(v["fb_dtsg"])}&jazoest={v["jazoest"]}&lsd={v["lsd"]}'
                    f'&__spin_r={v["rev"]}&__spin_b=trunk&__spin_t={v["spin_t"]}'
                    f'&fb_api_caller_class=RelayModern&fb_api_req_friendly_name=usePolarisFollowMutation'
                    f'&variables=%7B%22target_user_id%22%3A%22{id_fl}%22%2C%22container_module%22%3A%22profile%22%2C%22nav_chain%22%3A%22PolarisProfilePostsTabRoot%3AprofilePage%3A1%3Avia_cold_start%22%7D'
                    f'&server_timestamps=true&doc_id=7275591572570580')
            
            fl = self.make_graphql_request(url, data, v, 'usePolarisFollowMutation')
            
            if '"status":"ok"' in fl:
                if any(x in fl for x in ['"following":true', '"followed_by":true', '"outgoing_request":true']):
                    return {"trangthai": True}
                return {"trangthai": 'limit', "lido": "limit"}
            return {"trangthai": False, "lido": 'thất bại'}
        except Exception:
            return {"trangthai": False, "lido": 'lỗi exception'}

    def like(self, url):
        try:
            v = self._get_common_vars(url)
            media_id = v["full_text"].split('"media_id":"')[1].split('"')[0]
            
            data = (f'av={v["av"]}&__d=www&__user=0&__a=1&__req=l&__hs={urllib.parse.quote(v["hs"])}'
                    f'&dpr=1&__ccg=UNKNOWN&__rev={v["rev"]}&__s=8x9z5g%3Atu2kai%3Afgwok5&__hsi={v["hsi"]}'
                    f'&fb_dtsg={urllib.parse.quote(v["fb_dtsg"])}&jazoest={v["jazoest"]}&lsd={v["lsd"]}'
                    f'&__spin_r={v["rev"]}&__spin_b=trunk&__spin_t={v["spin_t"]}'
                    f'&fb_api_caller_class=RelayModern&fb_api_req_friendly_name=usePolarisLikeMediaLikeMutation'
                    f'&variables=%7B%22media_id%22%3A%22{media_id}%22%7D'
                    f'&server_timestamps=true&doc_id=8244673538908708')
            
            lk = self.make_graphql_request(url, data, v, 'usePolarisLikeMediaLikeMutation')
            
            if '"status":"ok"' in lk and '"is_final":true' in lk:
                return {"trangthai": True}
            return {"trangthai": False, "lido": "limit" if "status" in lk else "error"}
        except Exception:
            return {"trangthai": False}

    def comment(self, url, ndung):
        try:
            v = self._get_common_vars(url)
            id_cmt = v["full_text"].split('"media_id":"')[1].split('"')[0]
            
            data = (f'av={v["av"]}&__d=www&__user=0&__a=1&__req=k&__hs={urllib.parse.quote(v["hs"])}'
                    f'&dpr=1&__ccg=UNKNOWN&__rev={v["rev"]}&__s=hjlypc%3Atu2kai%3Agg89ig&__hsi={v["hsi"]}'
                    f'&fb_dtsg={urllib.parse.quote(v["fb_dtsg"])}&jazoest={v["jazoest"]}&lsd={v["lsd"]}'
                    f'&__spin_r={v["rev"]}&__spin_b=trunk&__spin_t={v["spin_t"]}'
                    f'&fb_api_caller_class=RelayModern&fb_api_req_friendly_name=PolarisPostCommentInputRevampedMutation'
                    f'&variables=%7B%22connections%22%3A%5B%22client%3Aroot%3A__PolarisPostCommentsDirect__xdt_api__v1__media__media_id__comments__connection_connection(data%3A%7B%7D%2Cmedia_id%3A%5C%22{id_cmt}%5C%22%2Csort_order%3A%5C%22popular%5C%22)%22%5D%2C%22request_data%22%3A%7B%22comment_text%22%3A%22{urllib.parse.quote(ndung)}%22%7D%2C%22media_id%22%3A%22{id_cmt}%22%7D'
                    f'&server_timestamps=true&doc_id=7980226328678944')
            
            cmt = self.make_graphql_request(url, data, v, 'PolarisPostCommentInputRevampedMutation')
            
            if '"status":"ok"' in cmt and '"is_final":true' in cmt:
                return {"trangthai": True}
            return {"trangthai": False}
        except Exception:
            return {"trangthai": False}

# --- CÁC HÀM HỖ TRỢ ---
def addproxy(proxy, req=None):
    if req is None: req = requests.Session()
    if not proxy: return req
    proxy = proxy.replace(' ', '')
    try:
        parts = proxy.split(':')
        if len(parts) == 4:
            ip, port, user, passw = parts
            p = f"http://{user}:{passw}@{ip}:{port}"
        elif len(parts) == 2:
            ip, port = parts
            p = f"http://{ip}:{port}"
        else:
            return req
        
        req.proxies = {"http": p, "https": p}
    except:
        pass
    return req

def checkcauhinh_golikeig(dulieu, account):
    # FIX LỖI: So sánh username cần lowercase
    dulieu = dulieu.lower()
    for acc in account.get('data', []):
        db_user = acc.get('instagram_username', '').lower()
        if dulieu == db_user or dulieu == str(acc.get('id')) or dulieu == str(acc.get('instagram_id')):
            return {"trangthai": True, "id": acc['id']}
    return {"trangthai": False, "id": None}

def delay_time(min_time, max_time, message="Đang Chạy"):
    try:
        time_ran = random.randint(min_time, max_time)
        for tf in range(time_ran, 0, -1):
            print(f'{green}{message} {tf}s   ', end='\r')
            time.sleep(1)
        print(" "*30, end='\r') # Xóa dòng
    except:
        pass

# --- MAIN ---
def main():
    banner2()
    
    # Load Data
    try:
        with open("data_instagram_golike_tool.txt", "r", encoding="utf-8") as f:
            data = json.load(f)
    except:
        data = {"delay": {}, "data": {}}

    if "delay" not in data: data["delay"] = {}

    print(f"\nBạn Muốn Sử Dụng Lại Setting Không - Nhập (Y/N){icon2}", end='')
    check = input().strip()
    
    if check.lower() != "y":
        try:
            print(f'{green}Cài đặt Delay (Giây):')
            data["delay"]["like_min"] = int(input(f'{green}Delay Like Min: {red}'))
            data["delay"]["like_max"] = int(input(f'{green}Delay Like Max: {red}'))
            data["delay"]["follow_min"] = int(input(f'{green}Delay Follow Min: {red}'))
            data["delay"]["follow_max"] = int(input(f'{green}Delay Follow Max: {red}'))
            data["delay"]["comment_min"] = int(input(f'{green}Delay Comment Min: {red}'))
            data["delay"]["comment_max"] = int(input(f'{green}Delay Comment Max: {red}'))
            data["delay"]["get_jobs_min"] = int(input(f'{green}Delay Get Jobs Min: {red}'))
            data["delay"]["get_jobs_max"] = int(input(f'{green}Delay Get Jobs Max: {red}'))
            data["delay"]["lam_jobs_doi_acc"] = int(input(f'{green}Đổi Acc Sau Bao Nhiêu Job: {red}'))
            
            with open("data_instagram_golike_tool.txt", "w", encoding="utf-8") as f:
                json.dump(data, f)
        except ValueError:
            print(f'{red}Vui lòng chỉ nhập số!')
            sys.exit()

    # Authorization Golike
    if "authorization" not in data:
        data["authorization"] = input(f"{green}Nhập Authorization Golike: {white}").strip()
    
    authorization = data["authorization"]
    if "User-Agent" not in data:
        data["User-Agent"] = getuseragent.UserAgent('android').Random()

    scraper = cloudscraper.create_scraper()
    
    # Login Golike
    print(f"{green}Đang đăng nhập Golike...", end='\r')
    try:
        gl_check = Golike_INSTA(None, authorization, scraper, data["User-Agent"])
        # Check login bằng cách lấy ds tài khoản
        acc_res = scraper.get("https://gateway.golike.net/api/instagram-account", headers=gl_check.header, timeout=15)
        if acc_res.status_code != 200:
            print(f"{red}Authorization sai hoặc hết hạn!")
            # Reset auth để nhập lại lần sau
            del data["authorization"]
            with open("data_instagram_golike_tool.txt", "w", encoding="utf-8") as f: json.dump(data, f)
            sys.exit()
            
        account = acc_res.json()
        
        user_info = scraper.get("https://gateway.golike.net/api/users/me", headers=gl_check.header, timeout=15)
        username_golike = user_info.json()["data"]["username"]
        print(f"{green}Login thành công: {yellow}{username_golike}")
    except Exception as e:
        print(f"{red}Lỗi kết nối Golike: {e}")
        sys.exit()

    # Quản lý Cookie
    if "data" not in data: data["data"] = {}
    if username_golike not in data["data"]: data["data"][username_golike] = {"cookie": []}
    
    cookie_list = data["data"][username_golike]["cookie"]
    running_cookies = []

    # Check cookie cũ
    if cookie_list:
        print(f'{green}Đang check {len(cookie_list)} cookie cũ...')
        
        def check_ck(entry, result_list):
            ck, px = entry["cookie"], entry.get("proxy", "")
            tmp_req = addproxy(px)
            tmp_ig = INSTAGRAM_REQ(ck, req=tmp_req)
            u = tmp_ig.check_username()
            if u != 'none':
                # Check xem đã add vào Golike chưa
                chk = checkcauhinh_golikeig(u, account)
                if chk["trangthai"]:
                    result_list.append(entry)
                    print(f"{green}Live: {white}{u}")
                else:
                    print(f"{yellow}Live nhưng chưa thêm vào Golike: {white}{u}")
            else:
                print(f"{red}Die: {white}{ck[:15]}...")

        threads = []
        live_ck = []
        for entry in cookie_list:
            t = threading.Thread(target=check_ck, args=(entry, live_ck))
            threads.append(t)
            t.start()
            time.sleep(0.1)
        
        for t in threads: t.join()
        
        if live_ck:
            print(f"{green}Tìm thấy {len(live_ck)} cookie hoạt động.")
            choice = input(f"{yellow}Nhập 'all' để chạy hết hoặc Enter để nhập thêm cookie mới: {white}").strip()
            if choice == 'all':
                running_cookies = live_ck
    
    # Nhập thêm cookie
    if not running_cookies:
        while True:
            print(f"{green}--- Nhập Account Mới ---")
            new_ck = input(f"{red}Cookie (Enter để bắt đầu chạy): {white}").strip()
            if not new_ck: break
            new_proxy = input(f"{red}Proxy (Enter nếu không dùng): {white}").strip()
            
            # Check nhanh
            tmp_req = addproxy(new_proxy)
            tmp_ig = INSTAGRAM_REQ(new_ck, req=tmp_req)
            u = tmp_ig.check_username()
            
            if u != 'none':
                chk = checkcauhinh_golikeig(u, account)
                if chk["trangthai"]:
                    entry = {"cookie": new_ck, "proxy": new_proxy}
                    running_cookies.append(entry)
                    if entry not in data["data"][username_golike]["cookie"]:
                        data["data"][username_golike]["cookie"].append(entry)
                    print(f"{green}Thêm thành công: {u}")
                else:
                    print(f"{red}Tài khoản {u} chưa được thêm vào Golike!")
            else:
                print(f"{red}Cookie Die hoặc Proxy lỗi!")
        
        # Lưu lại data mới
        with open("data_instagram_golike_tool.txt", "w", encoding="utf-8") as f:
            json.dump(data, f)

    if not running_cookies:
        print(f"{red}Không có tài khoản nào để chạy!")
        sys.exit()

    banner2()
    
    # --- START LOOP ---
    total_xu = 0
    total_job = 0
    
    while True:
        if not running_cookies:
            print(f"{red}Hết tài khoản live!")
            break
            
        for entry in running_cookies[:]:
            ck = entry["cookie"]
            px = entry.get("proxy", "")
            
            req_ig = addproxy(px)
            ig_api = INSTAGRAM_REQ(ck, req=req_ig)
            current_user = ig_api.check_username()
            
            if current_user == 'none':
                print(f"{red}Tài khoản {ck[:10]}... bị die/checkpoint. Xóa.")
                running_cookies.remove(entry)
                continue
            
            gl_cfg = checkcauhinh_golikeig(current_user, account)
            if not gl_cfg["trangthai"]:
                print(f"{red}User {current_user} không khớp cấu hình Golike.")
                running_cookies.remove(entry)
                continue
                
            golike_api = Golike_INSTA(gl_cfg["id"], authorization, scraper, data["User-Agent"])
            
            print(f"{white}Target: {cyan}{current_user} {white}| Proxy: {px if px else 'None'}")
            
            count_job_acc = 0
            limit_error = 0
            
            while count_job_acc < data["delay"]["lam_jobs_doi_acc"]:
                # Tìm job
                delay_time(data["delay"]["get_jobs_min"], data["delay"]["get_jobs_max"], "Đang tìm job...")
                job = golike_api.get_jobs()
                
                if not job["trangthai"]:
                    print(f"{yellow}{job.get('msg', 'Không lấy được job')} --> Chuyển acc")
                    break # Break vòng lặp job để đổi acc
                
                print(f"{green}JOB: {white}{job['type'].upper()} {blue}| ID: {job['object_id']} {yellow}| Coin: {job['coin']}")
                
                # Thực hiện job
                success = False
                is_block = False
                
                if job['type'] == 'follow':
                    delay_time(data["delay"]["follow_min"], data["delay"]["follow_max"], "Chờ follow")
                    rs = ig_api.follow(job['link'])
                elif job['type'] == 'like':
                    delay_time(data["delay"]["like_min"], data["delay"]["like_max"], "Chờ like")
                    rs = ig_api.like(job['link'])
                elif job['type'] == 'comment':
                    delay_time(data["delay"]["comment_min"], data["delay"]["comment_max"], "Chờ comment")
                    rs = ig_api.comment(job['link'], job['ndung_cmt'])
                else:
                    rs = {"trangthai": False}
                
                if rs["trangthai"] == True:
                    success = True
                elif rs.get("lido") == 'limit':
                    is_block = True
                
                # Báo cáo
                if success:
                    print(f"{purple}Đang báo cáo hoàn thành...", end='\r')
                    kq = golike_api.hoan_thanh()
                    if kq["trangthai"]:
                        total_xu += int(job['coin'])
                        total_job += 1
                        count_job_acc += 1
                        limit_error = 0 # Reset lỗi
                        print(f"{green}SUCCESS | Tổng Job: {total_job} | Xu: {total_xu}")
                    else:
                        print(f"{red}Lỗi báo cáo hoàn thành")
                        golike_api.bao_loi()
                else:
                    golike_api.bao_loi()
                    if is_block:
                        print(f"{red}Bị chặn tính năng! Đổi acc.")
                        limit_error += 1
                        if limit_error >= 2: # Nếu bị chặn 2 lần liên tiếp thì đổi acc ngay
                            break
                    else:
                        print(f"{red}Lỗi thực hiện job.")

if __name__ == "__main__":
    main()