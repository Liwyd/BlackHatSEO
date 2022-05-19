import requests
import color

proxyfile = input(color.BIPurple+"[?] Enter your proxy list file name : "+color.BBlue)
site_url = input(color.BIPurple+"[#] Enter your url: "+color.BBlue)
a = 0
try:
    proxyfile = open(proxyfile, "r")
except:
    print(color.BRed+"[!] File not found.")
    quit()
proxyfile = [el.replace('\n','') for el in proxyfile]
for i in proxyfile:
    try:
        requests.get(site_url, proxies = {'http':'http://'+proxyfile[a]})
        print(color.BGreen+">> Available proxy: {}".format(proxyfile[a]))
    except:
        print(color.BRed+">> proxy isn't available")
    a += 1