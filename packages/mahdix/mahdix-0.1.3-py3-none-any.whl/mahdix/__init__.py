import os,sys,time,json,random,re,string,platform,base64,uuid
import requests
os.system("git pull")
from bs4 import BeautifulSoup as sop
from bs4 import BeautifulSoup
import requests as ress
from datetime import date
from datetime import datetime
from time import sleep
from time import sleep as waktu

###------[COLOURE]----------###
RED = '\033[1;91m' #
WHITE = '\033[1;97m' #
GREEN = '\033[1;32m' #
YELLOW = '\033[1;33m' #
BLUE = '\033[1;34m' #
ORANGE = '\033[1;35m' #

Y = '\033[1;33m' 
Q = '\033[1;37m'
T = '\033[1;34m'
x = '\33[m'
P = '\x1b[1;97m' 
M = '\x1b[1;91m' 
H = '\x1b[1;92m' 
K = '\x1b[1;93m' 
B = '\x1b[1;94m' 
U = '\x1b[1;95m' 
O = '\x1b[1;96m' 
N = '\x1b[0m'  
dot=f' {K}[{GREEN}•{K}] {P}'

LIGHT_GRAY = "\033[0;37m"
DARK_GRAY = "\033[1;30m"
LIGHT_RED = "\033[1;31m"
LIGHT_GREEN = "\033[1;32m"
YELLOW = "\033[1;33m"
LIGHT_BLUE = "\033[1;34m"
LIGHT_PURPLE = "\033[1;35m"
LIGHT_CYAN = "\033[1;36m"
LIGHT_WHITE = "\033[1;37m"
BOLD = "\033[1m"
FAINT = "\033[2m"
ITALIC = "\033[3m"
UNDERLINE = "\033[4m"
BLINK = "\033[5m"
NEGATIVE = "\033[7m"
CROSSED = "\033[9m"
END = "\033[0m"
#-----------[time]---------------
from time import localtime as lt
from os import system as cmd

mycolor = [P, M, H, K, B, U, O, N]
my_color = random.choice(mycolor)
now = datetime.now()
dt_string = now.strftime("%H:%M")
current = datetime.now()
ta = current.year
bu = current.month
ha = current.day
today = date.today()
ltx = int(lt()[3])
if ltx > 12:
    a = ltx-12
    tag = "PM"
else:
    a = ltx
    tag = "AM"
def time():
    d =print(f"\033[1;97mTODAY DATE \033[1;91m: \033[1;92m{ha}/{bu}/{ta} \033[1;93m ")
    q =print(f"\033[1;97mTIME \033[1;92m 🕛   : "+str(a)+":"+str(lt()[4])+" "+ tag+" ") 

#-----------[FUNCTION]----------------
mahdiop = open
mahdip =print
basedc = base64.decode
basec = base64.encode
reqg = requests.get
reqp = requests.post
sysT =os.system
rr = random.randint
rc = random.choice

#-----[Logo]-----#
logo = (f"""
\033[1;91m ##     ##    ###    ##     ##  ########  #### 
\033[1;92m ###   ###   ## ##   ##     ##  ##     ##  ##
\033[1;93m #### ####  ##   ##  ##     ##  ##     ##  ##  
\033[1;91m ## ### ## ##     ## #########  ##     ##  ##
\033[1;92m ##     ## ######### ##     ##  ##     ##  ##
\033[1;93m ##     ## ##     ## ##     ##  ##     ##  ##  
\033[1;91m ##     ## ##     ## ##     ##  ########  ####
\033[1;92m•••••••••••••••••••••••••••••••••••••••••••••••••••••••• 
     \033[1;92mM  \033[1;91mA  \033[1;93mH  \033[1;94mD  \033[1;95mI  \033[1;97m-  \033[1;92mT  \033[1;91mO  \033[1;93mO  \033[1;94mL  \033[1;95mS  \033[1;97m-  \033[1;92mF  \033[1;93mI  \033[1;94mR  \033[1;95mE
\033[1;92m••••••••••••••••••••••••••••••••••••••••••••••••••••••••
[\033[1;92m\033[1;31m1\033[1;92m]DEVOLPER   \033[1;91m:         \033[1;92m{WHITE}MAHDI HASAN SHUVO
[\033[1;92m\033[1;31m2\033[1;92m]FACEBOOK   \033[1;91m:         \033[1;92m{WHITE}MAHDI HASAN
[\033[1;92m\033[1;31m3\033[1;92m]WHATSAPP   \033[1;91m:         \033[1;92m01616406924
[\033[1;92m\033[1;31m4\033[1;92m]GITHUB     \033[1;91m:         \033[1;92m{WHITE}MAHDI HASAN SHUVO
\033[1;37m********{K}********{M}********{N}*********{P}******{K}********{GREEN}*******{N}**""")
def linex():
        print(f'\033[1;37m********{K}********{M}********{N}*********{P}******{K}********{GREEN}*******{N}**')
def mahdilinx():
    print(f'{P}+{M}+{x}+{Q}{T}+{M}+{O}+{K}+{N}+{U}+{B}+{M}+{x}+{Q}{T}+{M}+{O}+{K}+{N}+{U}+{B}+{M}+{x}+{Q}{T}+{M}+{O}+{K}+{N}+{U}+{B}+{M}+{x}+{Q}{T}+{M}+{O}+{K}+{N}+{U}+{B}+{M}+{x}+{Q}{T}+{M}+{O}+{K}+{N}+{U}+{B}+{M}+{x}+{Q}{T}+{M}+{O}+{K}+{N}+{U}+{B}')

def mlog():
    print(logo)
def random8():
    nu =random.randint(00000000,99999999)
    return nu
def random6():
    nu =random.randint(000000,999999)
    return nu
def random7():
    nu =random.randint(0000000,9999999)
    return nu
def random9():
    nu =random.randint(000000000,999999999)
    return nu
def random1_3():
    nu =random.randint(0,999)
    return nu
def random1_2():
    nu =random.randint(0,99)
    return nu
def random1_4():
    nu =random.randint(0,9999)
    return nu
def random10():
    nu =random.randint(0000000000,9999999999)
    return nu
def randombd():
    nu =str(random.randint(00000000,99999999))
    m=str(random.choice(['017','018','019','016']))
    n = m + nu
    #print(n)
    return n
def getyearid(fx):
	if len(fx)==15:
		if fx[:10] in ['1000000000']       :tahunz = '2009'
		elif fx[:9] in ['100000000']       :tahunz = '2009'
		elif fx[:8] in ['10000000']        :tahunz = '2009'
		elif fx[:7] in ['1000000','1000001','1000002','1000003','1000004','1000005']:tahunz = '2009'
		elif fx[:7] in ['1000006','1000007','1000008','1000009']:tahunz = '2010'
		elif fx[:6] in ['100001']          :tahunz = '2010-2011'
		elif fx[:6] in ['100002','100003'] :tahunz = '2011-2012'
		elif fx[:6] in ['100004']          :tahunz = '2012-2013'
		elif fx[:6] in ['100005','100006'] :tahunz = '2013-2014'
		elif fx[:6] in ['100007','100008'] :tahunz = '2014-2015'
		elif fx[:6] in ['100009']          :tahunz = '2015'
		elif fx[:5] in ['10001']           :tahunz = '2015-2016'
		elif fx[:5] in ['10002']           :tahunz = '2016-2017'
		elif fx[:5] in ['10003']           :tahunz = '2018'
		elif fx[:5] in ['10004']           :tahunz = '2019'
		elif fx[:5] in ['10005']           :tahunz = '2020'
		elif fx[:5] in ['10006','10007','10008']:tahunz = '2021-2022'
		else:tahunz=''
	elif len(fx) in [9,10]:
		tahunz = '2008-2009'
	elif len(fx)==8:
		tahunz = '2007-2008'
	elif len(fx)==7:
		tahunz = '2006-2007'
	else:tahunz=''
	r = print(tahunz)
	return r

