import urllib2
from bs4 import BeautifulSoup
from datetime import datetime
import os

day_of_year = datetime.now().timetuple().tm_yday

file_name = str(day_of_year) + ".html"

page = urllib2.urlopen('http://www.listenersbible.com/devotionals/biy').read().decode('ascii','ignore')
# Found that I had to decode it with ascii to prevent the errors from utf-8
soup = BeautifulSoup(page,'html.parser')

list = soup.findAll('div', attrs={'id':'tabla1'})

f = open(file_name, 'w')
f.write(' '.join(map(str,list)))
f.close()

os.startfile(file_name)

# Found this to work with python 2.7 
