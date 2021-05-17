#                                        GNU AGPL V3
#
# Script by Port007
# Scraped Results from scamalytics
# I'm not responsible for any commericial or unlawful usage of this tool, Buy their API if u want it.
#
#


import requests
from bs4 import BeautifulSoup
import sys
import os


def validIPAddress(IP):
    """
    :type IP: str
    :rtype: str
    """

    def isIPv4(s):
        try:
            return str(int(s)) == s and 0 <= int(s) <= 255
        except:
            return False

    def isIPv6(s):
        if len(s) > 4:
            return False
        try:
            return int(s, 16) >= 0 and s[0] != '-'
        except:
            return False

    if IP.count(".") == 3 and all(isIPv4(i) for i in IP.split(".")):
        return "IPv4"
    if IP.count(":") == 7 and all(isIPv6(i) for i in IP.split(":")):
        return "IPv6"
    return "Neither"

versionfo = r'''
    ______                     __   ________ 
   / ____/________ ___  ______/ /  /  _/ __ \
  / /_  / ___/ __ `/ / / / __  /   / // /_/ /
 / __/ / /  / /_/ / /_/ / /_/ /  _/ // ____/ 
/_/   /_/   \__,_/\__,_/\__,_/  /___/_/     
                                             
         by Port007 -- v0.01
'''
print(versionfo)
i = 1
while i == 1:
    try:
        try:
            ip = str(sys.argv[1])
        except IndexError:
            ip = input("Enter IP Address: ")
        if ip == "127.0.0.1":
            print("Loopback detected, please enter a valid IP Address")
            os.system("pause")
            sys.exit()
        endpoint = f"https://scamalytics.com/ip/{ip}"
        IPresult = validIPAddress(f"{ip}")
        if IPresult == "Neither":
            raise TypeError
        else:
            i = 2
    except TypeError:
        print("Invalid value, Please try again.")
try:
    r = requests.get(endpoint)
    htmlresponse = r.text
    soup = BeautifulSoup(htmlresponse, 'html.parser')
    coderet = soup.find_all(class_="panel_title high_risk")
    finalstuff = str(coderet)
    amb = str(finalstuff.split("\">")[1].split("</")[0])
    print(amb)

    coderet = str(soup.find_all(class_="panel_body"))
    print(coderet.replace('[<div class="panel_body">','').replace('<b>','').replace('</b>','').replace('Scamalytics','We').replace('</div>]','').replace('  ',' '))


except:
    try:
        if (finalstuff.find("private IP address.")):
            print(
                "The IP Address you provided is local and not a public one. Please refer to https://www.h3xed.com/web-and-internet/whats-the-difference-between-external-and-local-ip-addresses for more info")
        else:
            print("Connection Error, This program needs internet to function.")
            
            
    except:
        print("Unknown Error Ocurred, Possibly Network Restrictions.")
        


os.system('pause')
sys.exit()
