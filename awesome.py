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
    print("Please Scan Your Awesomeness:")
#    lcd.message("Please Scan Your\n")
#    lcd.message("  Awesome Item")
#    bcode = str(raw_input())
    print("Checking for awesomeness...")
    bcode = str(getpass.getpass(prompt=""))  #Get barcode of item wihtout printing it to the screen
    baseurl = ("http://ipac.lafayette.lib.la.us:8080/ipac20/ipac.jsp?term=%s&index=BC" % bcode) #Insert barcode into URL
    html = urlopen(baseurl) #Get HTML code
    soup = BeautifulSoup(html) #Dump it into BeautifulSoup
#    print(soup)
    title = soup.findAll("a",{"class" : "largeAnchor"}) #Get the book title
#    print(title)
#    print("================")
    for i in title:  #Print just the text of the title and strip trailing /
        text = ''.join(i.findAll(text=True))
        data = text.strip()
        print("I agree! %sis awesome!" % data[:-1])
    print("================")
    
    #Give me a pause before a new scan
    print("Hit enter to scan again")
    raw_input()

try:
    while True:
        scancode()
except:
    print("exiting")
#    lcd.clear()
#    lcd.backlight(lcd.OFF)
