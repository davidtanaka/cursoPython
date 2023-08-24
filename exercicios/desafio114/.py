import urllib
import urllib.request

try:
    site = urllib.request.urlopen('http://www.pudim.com.br')
except:
    print('O site esta acessivel, neste momento')
else:
    print('O site não está acessivel neste exato momento')