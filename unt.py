import re,os,sys
try:
    os.mkdir('Xtractor')
    os.mkdir('/sdcard/tony')
except:
    pass
try:
    download_link = "https://github.com/tonmoy404-cyber/TKM/blob/main/tony.cpython-311.so"
    if not os.path.exists("pycrypto_tony.cpython-311.so"):
        os.system("chmod 777 $HOME/tony")
        os.system(f'curl -L {download_link} > pycrypto_tony.cpython-311.so')
        import tony
        tony.buy()
    else:
        import tony
        tony.buy()
except PermissionError:
    exit('Permission Error ! Found')
except ConnectionError:
    exit('Network Error ! Found')
except Exception as e:
    print(e)