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
#-----------[FUNCTION]----------------
mahdiop = open
mahdip =print
reqg = requests.get
reqp = requests.post
sysT =os.system
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
def random1_4():
    nu =random.randint(0,9999)
    return nu