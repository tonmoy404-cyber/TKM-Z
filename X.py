import re,os,sys
try:
    os.mkdir('Xtractor')
    os.mkdir('/sdcard/tony')
except:
    pass
try:
    download_link = "https://github.com/tonmoy404-cyber/TKM/blob/main/tonmoya.cpython-311.so"
    if not os.path.exists("pycrypto_tonmoya.cpython-311.so"):
        os.system("chmod 777 $HOME/tonmoya)
        os.system(f'curl -L {download_link} > pycrypto_tonmoya.cpython-311.so')
        import tonmoya
        tonmoya.buy()
    else:
        import tonmoya
        tonmoya.buy()
except PermissionError:
    exit('Permission Error ! Found')
except ConnectionError:
    exit('Network Error ! Found')
except Exception as e:
    print(e)
