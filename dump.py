import requests,random,sys,json,os,re,datetime,socket,pprint
from time import sleep as slp
from os import system as cmd
import os
totaldmp = 0
count = 0
try:
	os.mkdir('Data')
except:
	pass
try:
	os.remove('temp.txt')
except:
	pass
head = {"user-agent": "Mozilla/5.0 (Linux; Android 6.0.1; Redmi 4A Build/MMB29M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.92 Mobile Safari/537.36","referer": "https://www.facebook.com/","host": "business.facebook.com","origin": "https://business.facebook.com","upgrade-insecure-requests" : "1","accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7","cache-control": "max-age=0","accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8","content-type":"text/html; charset=utf-8"}
logo = """____________ MR JADUGAR____________
_____________________________________
github   : not found                                
Facebook : Kashif Baloch                     
YouTube  : Mr Jadugar Gamers           
Whatsapp : not found                            
                                                 [DEAD USER]
_____________________________________ """
def Jadu():
	os.system("clear")
	os.system("xdg-open https://youtube.com/channel/UCrfVEu_7ylJI8XiVBrg4gmw")
	print(logo)
    
	print("its only for fun")
	print("_____________________________________")
	print(" [1] login with cookies")
	p = input(" Select An Option : ")
	if p in ['1','01']:
			main()

def login():
    mkdir_data_login()
    print(logo)
    print('\n%s[%s•%s] %sInput Cookies %s!'%(M,P,M,P,M))
    cookie = str(input('%s[%s•%s] %sCookies %s: %s'%(J,P,J,P,J,P)))
    try:
        token = clotox(cookie)
        coki = {'cookie':cookie} 
        open('login/cookie.txt','w').write(cookie)
        open('login/token.txt','w').write(token)
        jam()
    except requests.exceptions.ConnectionError:print('\n   %s[%s•%s] %sNo Internet %s!%s\n'%(M,P,M,P,M,P));exit()
    except (KeyError,IOError,AttributeError):print('\n   %s[%s•%s] %sCookies Invalid %s!%s\n'%(M,P,M,P,M,P));exit()

def mkdir_data_login():
    # Make Directory Login Data
    try:os.mkdir("login")
    except:pass
    # Make Directory Dump
    try:os.mkdir("dump")
    except:pass
    # Delete Cookies
    try:os.remove('login/cookie.txt')
    except:pass
    # Delete Token
    try:os.remove('login/token.txt')
    except:pass


def clotox(cookie):
    with requests.Session() as xyz:
        get_tok = xyz.get(url_businness+'/business_locations',headers = {
            "user-agent":ua_business,
            "referer": web_fb,
            "host": "business.facebook.com",
            "origin": url_businness,
            "upgrade-insecure-requests" : "1",
            "accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7",
            "cache-control": "max-age=0",
            "accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
            "content-type":"text/html; charset=utf-8"},cookies = {"cookie":cookie})
        return (re.search("(EAAG\w+)", get_tok.text).group(1))

url_businness = "https://business.facebook.com"
ua_business = "Mozilla/5.0 (Linux; Android 8.1.0; MI 8 Build/OPM1.171019.011) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.86 Mobile Safari/537.36"
kata_dev = 'Lu Ganteng Banget Bang. Gw Mau Recode SClu, Soalnya Gw Goblok Soal Coding'
web_fb = "https://www.facebook.com/"
m_fb = "https://m.facebook.com/"
mbasic = "https://mbasic.facebook.com/"
header_grup = {"user-agent": "Dalvik/1.6.0 (Linux; U; Android 4.4.2; NX55 Build/KOT5506) [FBAN/FB4A;FBAV/106.0.0.26.68;FBBV/45904160;FBDM/{density=3.0,width=1080,height=1920};FBLC/it_IT;FBRV/45904160;FBCR/PosteMobile;FBMF/asus;FBBD/asus;FBPN/com.facebook.katana;FBDV/ASUS_Z00AD;FBSV/5.0;FBOP/1;FBCA/x86:armeabi-v7a;]"}
###
def grep(f):
	o = input('\033[0;97m[->] Save As : \033[1;32;1m')
	print(47*"\033[1;37;1m-")
	try:
		ask_link = int(input('[>>] Enter Grip ID Limit : \033[1;32;1m'))
		print(47*"\033[1;37;1m-")
	except:
		ask_link = 1
		completed = 0
	for links in range(ask_link):
		li = input('[✓] Separate Object : \033[1;32;1m')
		os.system('cat '+f+' | grep "'+li+'" >> '+o)
	print(47*"\033[1;37;1m-")
	print("[>>] Separating Successful ")
	print("[>>] New File Save \033[1;32;1m" + o)
	print(47*"\033[1;37;1m-")
	input("[>>] Press Inter to go Back < ")
	main()
def main():
	fbidz = []
	os.system("clear")
	print(logo)
	try:
		fbcokis = open("data/cookie.txt", "r").read()
		token = open('data/token.txt','r').read()
		ftoken = requests.get("https://business.facebook.com/business_locations", headers=head, cookies = {"cookie":fbcokis}).text
		eaag = re.search("(EAAG\w+)",str(ftoken))
	except:
		slp(1)
		login()
	global totaldmp,count
	try:
		token=open('data/token.txt','r').read()
		fbcokis = open("data/cookie.txt", "r").read()
	except FileNotFoundError:
		print("[*] Login Not Found")
		slp(1)
		cmd('rm -rf data/token.txt')
		login()
	try:
		cmd('clear')
		os.system("clear")
		print(logo)
		now = datetime.datetime.now()
		print("Date and Time ")
		print(now.strftime("%y-%m-%d %H:%M:%S"))
		hostnm = socket.gethostname()
		ipaddress = socket.gethostbyname(hostnm)
		print("ip address is :", ipaddress)
		print("_____________________________________")
		try:
			print("cookies already login")
			fbbuid = input("[->] Enter Public ID Link : ")
			dmp = requests.get("https://graph.facebook.com/"+fbbuid+"?fields=friends.limit(5000)&access_token="+token,cookies = {"cookie":fbcokis}).json()
			for idnm in dmp['friends']['data']:
				totaldmp+=1
				fbidz.append(idnm['id'])
		except KeyError:
			print("[*] Public ID Not Found")
			main()
		filepath = input("[>>] Enter File Path : ")
		print("")
		print(47*"\033[1;37;1m-")
		apnd = open(filepath,'w')
		for fbuid in fbidz:
			count += 1
			try:
				dmp = requests.get("https://graph.facebook.com/"+fbuid+"?fields=friends.limit(5000)&access_token="+token,cookies = {"cookie":fbcokis}).json()
				for idnm in dmp['friends']['data']:
					apnd.write(idnm['id']+"|"+idnm['name']+'\n')
				print("\x1b[1;92m[>>] Dumping UID From : " + fbuid)
			except KeyError:
				print('\x1b[1;91m[>>] Dumping UID From : ' + fbuid)
		apnd.close()
		print(47*"\033[1;37;1m-")
		ch_x1 = input("[->] DoYou Want to Use DuplicateID Cuter (n/y) : ")
		if ch_x1 in ["yes","Yes","YES","Y","y"]:
			newfile = input("[->] File Without Duplicate ID Save As : ")
			os.system('sort -r '+filepath+' | uniq > '+newfile)
			ch_x2 = input("[->] DoYou Want to Use ID Separator (n/y) : ")
			if ch_x2 in ["yes","Yes","YES","Y","y"]:
				grep(newfile)
			else:
				print(47*"-")
				print (f"\x1b[0;37m Your Dump File Save As :\x1b[1;92m {newfile} \x1b[0;37m")
				print(47*'-')
				input("[>>] Press Inter to go Back < ")
				menu()
		else:
			print('\n')
			ch_x2 = input("[->] Do You Want to Use ID Separator (n/y) : \033[1;32;1m")
			if ch_x2 in ["yes","Yes","YES","Y","y"]:
				grep(filepath)
			else:
				print(47*'\033[1;37;1m-')
				print (f"\x1b[0;37m Total ID Dump :\x1b[1;92m {totaldmp}")
				print (f"\x1b[0;37m Your Dump File Save As :\x1b[1;92m {filepath} ")
				print(47*'\033[1;37;1m-')
				input("[>>] Press Inter to go Back < ")
				menu()
	except Exception as e:
		print("[>>] Error : %s"%e)
		exit("")
if __name__ == '__main__':
	Jadu()
