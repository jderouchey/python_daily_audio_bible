#Script to play the scripture for the year
import os,sys
from datetime import datetime
day_of_year = datetime.now().timetuple().tm_yday
mp3_file = "C:\\Users\\joel\\Music\\bible\\Day_" + str(day_of_year)  + ".mp3"
os.system(mp3_file) 
# This works with windows 8.1 also change path to the the folder that has the mp3's
