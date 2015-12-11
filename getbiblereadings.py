import urllib 
import time
# I discovered this in firefox by hitting F12 and selecting the network tab while playing the audio
baseurl = "http://www.listenersbible.com/sites/default/files/assets/audio/"
getfile = "Day_"
postfix = ".mp3"
mylist = []
r = 365

for x in range (r):
	y=x+1
	mylist.insert(x,baseurl + getfile + str(y).zfill(3) + postfix)
	print mylist[x] # This is for me to see the script in action
	urllib.urlretrieve(mylist[x],filename = getfile+str(y).zfill(3)+postfix)
	time.sleep(5)
# I had to add the sleep timer because the web server would only allow me to download 15 files.
# I am using python 3.5
