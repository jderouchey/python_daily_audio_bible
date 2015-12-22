#This file just downloads one file a day
#Thaks to this site: http://stackoverflow.com/questions/22676/how-do-i-download-a-file-over-http-using-python
import urllib2

from datetime import datetime
day_of_year = datetime.now().timetuple().tm_yday
print ("Today is the %s of the year" % day_of_year)

base_url = "http://www.listenersbible.com/sites/default/files/assets/audio/"
prefix = "Day_"
postfix= ".mp3"
url = base_url + prefix + str(day_of_year) + postfix


# url = "http://download.thinkbroadband.com/10MB.zip"

file_name = url.split('/')[-1]
u = urllib2.urlopen(url)
f = open(file_name, 'wb')
meta = u.info()
file_size = int(meta.getheaders("Content-Length")[0])
print "Downloading: %s Bytes: %s" % (file_name, file_size)

file_size_dl = 0
block_sz = 8192
while True:
    buffer = u.read(block_sz)
    if not buffer:
        break

    file_size_dl += len(buffer)
    f.write(buffer)
    status = r"%10d  [%3.2f%%]" % (file_size_dl, file_size_dl * 100. / file_size)
    status = status + chr(8)*(len(status)+1)
    print status,

f.close()
