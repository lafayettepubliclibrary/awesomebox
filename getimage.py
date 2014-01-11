import time
import os
import getpass
from bs4 import BeautifulSoup
from urllib2 import urlopen

def getimage():
    os.system("clear")
    print("Scan the item you want the image for:")
    bcode = str(getpass.getpass(prompt=""))
    print("Getting image...")
    baseurl = ("http://ipac.lafayette.lib.la.us:8080/ipac20/ipac.jsp?term=%s&index=BC" % bcode)
    html = urlopen(baseurl)
    soup = BeautifulSoup(html)

###Begin code to download and save the image from IPAC
    imageinfo = soup.findAll("img",{"alt" : "View full image"})
    file = "image.jpg"
    for i in imageinfo:
        imageurl = i['src']
    imgresponse = urlopen(imageurl)
    fh = open(file, "w")
    fh.write(imgresponse.read())
    fh.close()
    os.system("cp ./image.jpg /var/www/")
    print("Hit enter to scan again")
    raw_input()


getimage()
