import time
import os
import getpass
from bs4 import BeautifulSoup
from urllib2 import urlopen
#from Adafruit_CharLCDPlate import Adafruit_CharLCDPlate
#lcd = Adafruit_CharLCDPlate()

#lcd.clear()

def scancode():
    os.system("clear")
#    lcd.clear()
#    lcd.backlight(lcd.VIOLET)
    print("So... You found something awesome?")
    print("Please Scan Your Awesomeness")
#    lcd.message("Please Scan Your\n")
#    lcd.message("  Awesome Item")
#    bcode = str(raw_input())
    bcode = str(getpass.getpass(prompt=""))
    baseurl = ("http://ipac.lafayette.lib.la.us:8080/ipac20/ipac.jsp?term=%s&index=BC" % bcode)
    html = urlopen(baseurl)
    soup = BeautifulSoup(html)
#    print(soup)
    title = soup.findAll("a",{"class" : "largeAnchor"})
#    print(title)
#    print("================")
    for i in title:
        text = ''.join(i.findAll(text=True))
        data = text.strip()
        print("I agree! %sis awesome!" % data[:-1])
    print("================")
#    print("I agree, %s is awesome!" % title)
#    print("http://ipac.lafayette.lib.la.us:8080/ipac20/ipac.jsp?term=%s&index=BC" % bcode)
    print("Hit enter to scan again")
    raw_input()

try:
    while True:
        scancode()
except:
    print("exiting")
    lcd.clear()
    lcd.backlight(lcd.OFF)
