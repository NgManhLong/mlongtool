
den = "\033[1;90m"
luc = "\033[1;32m"
trang = "\033[1;37m"
red = "\033[1;31m"
vang = "\033[1;33m"
tim = "\033[1;35m"
lamd = "\033[1;34m"
lam = "\033[1;36m"
hong = "\033[1;95m"
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
##### Cài Thư Viện #####
from pystyle import Add, Center, Anime, Colors, Colorate, Write, System
import requests, json
import os
import sys
from sys import platform
from time import sleep
from datetime import datetime
from colorama import Fore, init
from time import strftime
total = 0
may = 'mb' if platform[0:3] == 'lin' else 'pc'

def banner():
    os.system('cls' if os.name=='nt' else 'clear')
    tool = "traodoisub TikTok"
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
banner()
# =======================[ NHẬP KEY ]=======================
 

def bongoc(so):
	for i in range(so):
		print(red+'────', end = '' )
	print('')
class TraoDoiSub_Api (object):
	def __init__ (self, token):
		self.token = token
	
	def main(self):
		try:
			main = requests.get('https://traodoisub.com/api/?fields=profile&access_token='+self.token).json()
			try:
				return main['data']
			except:
				False
		except:
			return False
	def run(self, user):
		try:
			run = requests.get(f'https://traodoisub.com/api/?fields=tiktok_run&id={user}&access_token={self.token}').json()
			try:
				return run['data']
			except:
				return False
		except:
			return False
	#tiktok_like, tiktok_follow
	def get_job(self, type):
		try:
			get = requests.get(f'https://traodoisub.com/api/?fields={type}&access_token={self.token}')
			return get
		except:
			return False
	
	def cache(self, id, type):
#TIKTOK_LIKE_CACHE, TIKTOK_FOLLOW_CACHE
		try:
			cache = requests.get(f'https://traodoisub.com/api/coin/?type={type}&id={id}&access_token={self.token}').json()
			try:
				cache['cache']
				return True
			except:
				return False
		except:
			return False

	def nhan_xu(self, id, type):
		try:
			nhan = requests.get(f'https://traodoisub.com/api/coin/?type={type}&id={id}&access_token={self.token}')
			try:
				xu = nhan.json()['data']['xu']
				msg = nhan.json()['data']['msg']
				job = nhan.json()['data']['job_success']
				xuthem = nhan.json()['data']['xu_them']
				global total
				total+=xuthem
				bongoc(14)
				print(f' {lam}Thành Công {Fore.BLUE}[{vang}{msg}{Fore.BLUE}] {Fore.BLUE}[{luc}Tổng {vang}{xu} {luc}Xu{Fore.BLUE}]')
				bongoc(14)
				if job == 0:
					return 0
			except:
				if '"code":"error","msg"' in nhan.text:
					hien = nhan.json()['msg']; print(red+hien, end = '\r'); sleep(2); print(' '*len(hien), end = '\r')
				else:
					print(red+' Nhận Xu Thất Bại !', end = '\r'); sleep(2); print('                                                       ', end = '\r')
				return False
		except:
			print(red+' Nhận Xu Thất Bại !', end = '\r'); sleep(2); print('                                                       ', end = '\r')
			return False
def delay(dl):
  try:
    for i in range(dl, -1, -1):
       print(f'\033[1;35m \033[1;35m[{lam}QT\033[1;35m]\033[1;35m[{luc}TOOL-VIP\033[1;35m]\033[1;35m[{trang}'+str(i)+vang+'\033[1;35m]     ',end='\r')
       sleep(1)
  except:
     sleep(dl)
     print(dl,end='\r')

def chuyen(link, may):
	if may == 'mb':
		os.system(f'xdg-open {link}')
	else:
		os.system(f'cmd /c start {link}')



def main():
	dem=0
	banner()
	while True:
		if os.path.exists('configtds.txt'):
			with open('configtds.txt', 'r') as f:
				token = f.read()
			tds = TraoDoiSub_Api(token)
			data = tds.main()
			try:
				print(f'{vang}[{trang}1{vang}] {luc}Vào Tài Khoản '+vang+ data['user'] )
				print(f'{vang}[{trang}2{vang}] {luc}Nhập Access_Token TDS Mới')
				chon = input(f' {luc}Nhập Yêu Cầu: {vang}')
				if chon == '2':
					os.remove('configtds.txt')
				elif chon == '1':
					pass
				else:
					print(red+' Lựa chọn không xác định !!!');bongoc(14)
					continue 
			except:
				os.remove('configtds.txt')
		if not os.path.exists('configtds.txt'):
			token = input(f' {luc}Nhập Access_Token TDS: {vang}')
			with open('configtds.txt', 'w') as f:
				f.write(token)
		with open('configtds.txt', 'r') as f:
			token = f.read()
		tds = TraoDoiSub_Api(token)
		data = tds.main()
		try:
			xu = data['xu']
			xudie = data['xudie']
			user = data['user']
			print(lam+' Đăng Nhập Thành Công ')
			os.system("cls" if os.name == "nt" else "clear")
			break
		except:
			print(red+' Access Token Không Hợp Lệ! Xin Thử Lại ')
			os.remove('configtds.txt')
			continue 
	bongoc(14)
	
	
		
#while True:
	#cookie=input('Nhập Cookie Tiktok: ')
	#try:
		#headers={'Host':'www.tiktok.com','sec-ch-ua':'";Not A Brand";v="99", "Chromium";v="94"','sec-ch-ua-mobile':'?1','user-agent':'Mozilla/5.0 (Linux; Android 11; vivo 1904) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.56 Mobile Safari/537.36','sec-ch-ua-platform':'"Android"','accept':'*/*','sec-fetch-site':'same-origin','sec-fetch-mode':'cors','sec-fetch-dest':'empty','referer':'https://www.tiktok.com/foryou?is_from_webapp=v1&is_copy_url=1','accept-language':'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5','cookie':cookie}
		#info = requests.post(f'https://www.tiktok.com/passport/web/account/info/?aid=1459&app_language=vi-VN&app_name=tiktok_web&battery_info=0.79&browser_language=vi-VN&browser_name=Mozilla&browser_online=true&browser_platform=Linux%20aarch64&browser_version=5.0%20%28Linux%3B%20Android%2011%3B%20vivo%201904%29%20AppleWebKit%2F537.36%20%28KHTML%2C%20like%20Gecko%29%20Chrome%2F94.0.4606.56%20Mobile%20Safari%2F537.36&channel=tiktok_web&cookie_enabled=true&device_id=7126951839819712002&device_platform=web_mobile&focus_state=true&from_page=fyp&history_len=28&is_fullscreen=false&is_page_visible=true&os=android&priority_region=VN&referer=&region=VN&screen_height=772&screen_width=360&tz_name=Asia%2FSaigon&webcast_language=vi-VN',headers=headers).json()
		#id_tikok=info['data']['user_id_str']
		#user_tiktok=info['data']['username']
		#name_tiktok=info['data']['screen_name']
		#print('User Tiktok:',user_tiktok)
		#sleep(1)
		#break
	#except:
		#print('Kiểm Tra Lại Cookie')

	banner()
	print(f' {luc}Tài Khoản: {vang}{user} ')
	print(f' {luc}Xu Hiện Tại: {vang}{xu}')
	while True:
		ntool=0
		bongoc(14)
		print(f'{red}[{vang}1{red}] {luc}Nhiệm Vụ Tim')
		print(f'{red}[{vang}2{red}] {luc}Nhiệm Vụ Follow')
		print(f'{red}[{vang}3{red}] {luc}Nhiệm Vụ Follow Tiktok Now')
		nhiem_vu=input(f' {luc}Nhập Lựa Chọn: {vang}')
		dl = int(input(f' {luc}Nhập Delay: {vang}'))
		while True:
			if ntool == 2:
				break
			ntool = 0
			bongoc(14)
			nv_nhan=int(input(f' {luc}Sau Bao Nhiêu Nhiệm Vụ Thì Nhận Xu: {vang}'))
			if nv_nhan < 8:
				print(red+' Trên 8 Nhiệm Vụ Mới Được Nhận Tiền!')
				continue
			if nv_nhan > 15:
				print(red+' Nhận Xu Dưới 15 Nhiệm Vụ Để Tránh Lỗi')
				continue
			user_cau_hinh=input(f' {luc}Nhập User Name Tik Tok Cần Cấu Hình: {vang}')
			cau_hinh=tds.run(user_cau_hinh)
			if cau_hinh != False:
				user=cau_hinh['uniqueID']
				id_acc=cau_hinh['id']
				bongoc(14)
				print(f' {luc}User: {vang}{user}')
				bongoc(14)
			else:
				print(f' {red}Cấu Hinh Thất Bại User: {vang}{user_cau_hinh} ')
				continue 
			while True:
				if ntool==1 or ntool==2:break
				if '1' in nhiem_vu:
					listlike = tds.get_job('tiktok_like')
					if listlike == False:
						print(red+'Không Get Được Nhiệm Vụ Like              ', end = '\r');sleep(2); print('                                                        ', end = '\r')
					elif 'error' in listlike.text:
						if listlike.json()['error'] == ' Thao tác quá nhanh vui lòng chậm lại':
							coun = listlike.json()['countdown']
							print(f' {red}Đang Get Nhiệm Vụ Like, COUNTDOWN: {str(round(coun, 3))} ', end = '\r'); sleep(2); print('                                                       ', end = '\r')
						elif listlike.json()['error'] == ' Vui lòng ấn NHẬN TẤT CẢ rồi sau đó tiếp tục làm nhiệm vụ để tránh lỗi!':
							nhan = tds.nhan_xu('TIKTOK_LIKE_API', 'TIKTOK_LIKE') #TIKTOK_LIKE, TIKTOK_FOLLOW, TIKTOK_COMMENT
						else:
							print(red+listlike.json()['error'] , end ='\r');sleep(2); print('                                                        ', end = '\r')
					else:
						try:
							listlike = listlike.json()['data']
						except:
							print(red+' Hết Nhiệm Vụ Like                             ', end = '\r');sleep(2); print('                                                        ', end = '\r')
							continue
						if len(listlike) == 0:
							print(red+' Hết Nhiệm Vụ Like                             ', end = '\r');sleep(2); print('                                                        ', end = '\r')
						else:
							print(f' {luc}Tìm Thấy {vang}{len(listlike)} {luc}Nhiệm Vụ Like                       ', end = '\r');sleep(2); print('                                                        ', end = '\r')
							for i in listlike:
								id = i['id']
								link = i['link']
								chuyen(link, may)

								
								cache = tds.cache(id, 'TIKTOK_LIKE_CACHE')
								if cache != True:
									tg=datetime.now().strftime('%H:%M:%S')
									hien = f'{vang}[{red}X{vang}] \033[1;35m=> {Fore.BLUE}[{lam}SUCCESS{Fore.BLUE}] \033[1;35m=> {Fore.BLUE}[{Colorate.Horizontal(Colors.yellow_to_red, "TIM")}{Fore.BLUE}] \033[1;35m=> {Fore.BLUE}[{lam}{tg}{Fore.BLUE}]'; print(hien, end = '\r');sleep(1); print('                                                                                        ', end = '\r')
								else:
									dem+=1
									tg=datetime.now().strftime('%H:%M:%S')
									print(f'{vang}[{trang}{dem}{vang}] \033[1;35m=> {Fore.BLUE}[{lam}SUCCESS{Fore.BLUE}] \033[1;35m=> {Fore.BLUE}[{Colorate.Horizontal(Colors.yellow_to_red, "TIM")}{Fore.BLUE}] \033[1;35m=> {Fore.BLUE}[{lam}{tg}{Fore.BLUE}]')
									delay(dl)
									if dem % nv_nhan == 0:
										nhan = tds.nhan_xu('TIKTOK_LIKE_API', 'TIKTOK_LIKE')
										if nhan == 0:
											print(luc+'Nhận Xu Thất Bại Acc Tiktok Của Bạn Ổn Chứ ') 
											print(f' {luc}Nhập {red}[{vang}1{red}] {luc}Để Thay Nhiệm Vụ ')
											print(f' {luc}Nhập {red}[{vang}2{red}] {luc}Thay Acc Tiktok ')
											print(f' {luc}Nhấn {red}[{vang}Enter{red}] {luc}Để Tiếp Tục')
											chon=input(f' {luc}Nhập: {vang}')
											if chon == '1':
												ntool=2
												break
											elif chon =='2':
												ntool = 1
												break
											bongoc(14)
				if ntool==1 or ntool==2:break
				if '2' in nhiem_vu:
					listfollow = tds.get_job('tiktok_follow')
					if listfollow == False:
						print(red+'Không Get Được Nhiệm Vụ Follow              ', end = '\r');sleep(2); print('                                                        ', end = '\r')
					elif 'error' in listfollow.text:
						if listfollow.json()['error'] == ' Thao tác quá nhanh vui lòng chậm lại':
							coun = listfollow.json()['countdown']
							print(red+f'Đang Get Nhiệm Vụ Follow, COUNTDOWN: {str(round(coun, 3))} ', end = '\r'); sleep(2); print('                                                       ', end = '\r')
						elif listfollow.json()['error'] == ' Vui lòng ấn NHẬN TẤT CẢ rồi sau đó tiếp tục làm nhiệm vụ để tránh lỗi!':
							nhan = tds.nhan_xu('TIKTOK_FOLLOW_API', 'TIKTOK_FOLLOW') #TIKTOK_LIKE, TIKTOK_FOLLOW, TIKTOK_COMMENT
						else:
							print(red+listfollow.json()['error'] , end ='\r');sleep(2); print('                                                        ', end = '\r')
					else:
						try:
							listfollow = listfollow.json()['data']
						except:
							print(red+'Hết Nhiệm Vụ Follow                             ', end = '\r');sleep(2); print('                                                        ', end = '\r')
							continue
						if len(listfollow) == 0:
							print(red+'Hết Nhiệm Vụ Follow                             ', end = '\r');sleep(2); print('                                                        ', end = '\r')
						else:
							print(luc+f' Tìm Thấy {vang}{len(listfollow)} {luc}Nhiệm Vụ Follow                       ', end = '\r');sleep(2); print('                                                        ', end = '\r')
							for i in listfollow:
								id = i['id']
								link = i['link']
								chuyen(link, may)
								cache = tds.cache(id, 'TIKTOK_FOLLOW_CACHE')
								if cache != True:
									tg=datetime.now().strftime('%H:%M:%S')
									hien = f'{vang}[{red}X{vang}] \033[1;35m=> {Fore.BLUE}[{lam}SUCCESS{Fore.BLUE}] \033[1;35m=> {Fore.BLUE}[{Colorate.Horizontal(Colors.yellow_to_red, "FOLLOW")}{Fore.BLUE}] \033[1;35m=> {Fore.BLUE}[{lam}{tg}{Fore.BLUE}]'; print(hien, end = '\r');sleep(1); print('                                                                                        ', end = '\r')
								else:
									dem+=1
									tg=datetime.now().strftime('%H:%M:%S')
									print(f'{vang}[{trang}{dem}{vang}] \033[1;35m=> {Fore.BLUE}[{lam}SUCCESS{Fore.BLUE}] \033[1;35m=> {Fore.BLUE}[{Colorate.Horizontal(Colors.yellow_to_red, "FOLLOW")}{Fore.BLUE}] \033[1;35m=> {Fore.BLUE}[{lam}{tg}{Fore.BLUE}]')
									delay(dl)
									if dem % nv_nhan == 0:
										nhan = tds.nhan_xu('TIKTOK_FOLLOW_API', 'TIKTOK_FOLLOW')
										if nhan == 0:
											print(luc+'Nhận Xu Thất Bại Acc Tiktok Của Bạn Ổn Chứ ') 
											print(f' {red}[{vang}1{red}] {luc}Đổi Nhiệm Vụ ')
											print(f' {red}[{vang}2{red}] {luc}Thay Acc Tiktok ')
											print(f' {red}[{vang}Enter{red}] {luc}Tiếp Tục')
											chon=input(f' {luc}Nhập Lựa Chọn{trang}: {vang}')
											if chon == '1':
												ntool=2
												break
											elif chon =='2':
												ntool = 1
												break
											bongoc(14)
				if ntool==1 or ntool==2:break
				if '3' in nhiem_vu:
					listfollow = tds.get_job('tiktok_follow')
					if listfollow == False:
						print(red+' Không Get Được Nhiệm Vụ Follow              ', end = '\r');sleep(2); print('                                                        ', end = '\r')
					elif 'error' in listfollow.text:
						if listfollow.json()['error'] == ' Thao tác quá nhanh vui lòng chậm lại':
							coun = listfollow.json()['COUNTDOWN']
							print(f' {lam}Đang Get Nhiệm Vụ Follow, COUNTDOWN: {str(round(coun, 3))} ', end = '\r'); sleep(2); print('                                                       ', end = '\r')
						elif listfollow.json()['error'] == ' Vui lòng ấn "NHẬN TẤT CẢ" rồi sau đó tiếp tục làm nhiệm vụ để tránh lỗi!':
							nhan = tds.nhan_xu('TIKTOK_FOLLOW_API', 'TIKTOK_FOLLOW') #TIKTOK_LIKE, TIKTOK_FOLLOW, TIKTOK_COMMENT
						else:
							print(red+listfollow.json()['error'] , end ='\r');sleep(2); print('                                                        ', end = '\r')
					else:
						try:
							listfollow = listfollow.json()['data']
						except:
							print(red+' Hết Nhiệm Vụ Follow                             ', end = '\r');sleep(2); print('                                                        ', end = '\r')
							continue
						if len(listfollow) == 0:
							print(red+' Hết Nhiệm Vụ Follow                             ', end = '\r');sleep(2); print('                                                        ', end = '\r')
						else:
							print(f' {luc}Tìm Thấy {vang}{len(listfollow)} {luc}Nhiệm Vụ Follow                       ', end = '\r');sleep(2); print('                                                        ', end = '\r')
							for i in listfollow:
								id = i['id']
								uid = id.split('_')[0] 
								link = i['link']
								que = i['uniqueID']
								if may == 'mb':
									chuyen(f'tiktoknow://user/profile?user_id={uid}', may)
								else:
									chuyen(f'https://now.tiktok.com/@{que}', may)
								cache = tds.cache(id, 'TIKTOK_FOLLOW_CACHE')
								if cache != True:
									tg=datetime.now().strftime('%H:%M:%S')
									hien = f'{vang}[{red}X{vang}] \033[1;35m=> {Fore.BLUE}[{lam}SUCCESS{Fore.BLUE}] \033[1;35m=> {Fore.BLUE}[{Colorate.Horizontal(Colors.yellow_to_red, "FOLLOW tiktok NOW")}{Fore.BLUE}] \033[1;35m=> {Fore.BLUE}[{lam}{tg}{Fore.BLUE}]'; print(hien, end = '\r');sleep(1); print('                                                                                        ', end = '\r')
								else:
									dem+=1
									tg=datetime.now().strftime('%H:%M:%S')
									print(f'{vang}[{trang}{dem}{vang}] \033[1;35m=> {Fore.BLUE}[{lam}SUCCESS{Fore.BLUE}] \033[1;35m=> {Fore.BLUE}[{Colorate.Horizontal(Colors.yellow_to_red, "FOLLOW tiktok NOW")}{Fore.BLUE}] \033[1;35m=> {Fore.BLUE}[{lam}{tg}{Fore.BLUE}]')
									delay(dl)
									if dem % nv_nhan == 0:
										nhan = tds.nhan_xu('TIKTOK_FOLLOW_API', 'TIKTOK_FOLLOW')
										if nhan == 0:
											print(luc+'Nhận Xu Thất Bại Acc Tiktok Của Bạn Ổn Chứ ') 
											print(f' {luc}Nhập {red}[{vang}1{red}] {luc}Để Thay Nhiệm Vụ ')
											print(f' {luc}Nhập {red}[{vang}2{red}] {luc}Thay Acc Tiktok ')
											print(f' {luc}Nhấn {red}[{vang}Enter{red}] {luc}Để Tiếp Tục')
											chon=input(f' {luc}Nhập Lựa Chọn: {vang}')
											if chon == '1':
												ntool=2
												break
											elif chon =='2':
												ntool = 1
												break
											bongoc(14)
main()
