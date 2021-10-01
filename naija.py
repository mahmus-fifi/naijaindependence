#program to subtract dates (Happy birthday Naija)
#written by Mahmud Shuaib
#2021-10-01
from datetime import datetime #import the datetime module
year_days = 365
nija_birthday = datetime(1960, 10, 1, 12, 0, 0)
date_diff = datetime.now() - nija_birthday
#print the result using an f-string
print(f"Happy Birthday Naija, you are {date_diff} days old!") 
#other stuff
#using date_diff.days to return int value for days and divide by 365 to get the year
#rounding the value of the year to Zero significant figures using the round method 
print(f"Wow Naija, if you are {date_diff.days} days old\n,\
      that means you are now {round((date_diff.days/year_days),0)} years old")







