import os, platform 

try:

        import requests

except:

        os.system('pip2 install requests')

bit = platform.architecture()[0]

if bit == "64bit":

        from tony import random

        random()

elif bit == "32bit":

        os.system('python tony3.py')
