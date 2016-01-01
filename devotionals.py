import shutil
import urllib3
import os
from bs4 import BeautifulSoup
from datetime import datetime
#Function
def gethttp_data(base_url,filename):
    c = urllib3.PoolManager()
    with c.request('GET',base_url+filename, preload_content=False) as resp, open(filename, 'wb') as out_file:
        shutil.copyfileobj(resp, out_file)

day_of_year = str(datetime.now().timetuple().tm_yday).zfill(3)

print ("Today is day %s of the year" % day_of_year)

base_url = "http://www.listenersbible.com/sites/default/files/assets/audio/"
prefix = "Day_"
postfix= ".mp3"
filename = prefix+str(day_of_year)+postfix
gethttp_data(base_url,filename)
os.startfile(filename)

#Setting up html file now
filename = str(day_of_year) + ".html"
base_url = "http://www.listenersbible.com/devotionals/biy"
gethttp_data(base_url,filename)



#parse the routine
#      Reads the file on the disk
with open((os.getcwd() + '\\' + filename),'r',encoding='UTF8') as infile:
    data = infile.read()
soup = BeautifulSoup(data,'html.parser')
list = soup.findAll('div', attrs={'id':'tabla1'})
f = open(filename, 'w')
f.write(' '.join(map(str,list)))
f.close()

os.startfile(filename) # starts the html file
