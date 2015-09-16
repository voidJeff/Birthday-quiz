"""
birthday.py
Author: Jeff
Credit: None
Assignment:

Your program will ask the user the following questions, in this order:

1. Their name.
2. The name of the month they were born in (e.g. "September").
3. The year they were born in (e.g. "1962").
4. The day they were born on (e.g. "11").

If the user's birthday fell on October 31, then respond with:

  You were born on Halloween!

If the user's birthday fell on today's date, then respond with:

  Happy birthday!

Otherwise respond with a statement like this:

  Peter, you are a winter baby of the nineties.

Example Session

  Hello, what is your name? Eric
  Hi Eric, what was the name of the month you were born in? September
  And what year were you born in, Eric? 1972
  And the day? 11
  Eric, you are a fall baby of the stone age.
"""

from datetime import datetime
from calendar import month_name
todaymonth = datetime.today().month
todaydate = datetime.today().day

name = input("Hello, what is your name? ")
month = input("Hi {0}, what was the name of the month you were born in? ".format(name))
year = int(input("And what year were you born in, {0}? ".format(name)))
date = int(input("And the day? "))
month_ = month_name[todaymonth]


if month == "December" or month == "January" or month == "February":
    season = "winter"
elif month == "March" or month == "April" or month == "May":
    season = "spring"
elif month == "June" or month == "July" or month == "August":
    season = "summer"
elif month == "September" or month == "October" or month == "November":
    season = "fall"
else:
    print("Wrong spelling!")

if year < 1980:
    age = "stone age"
elif year >= 1980 and year <= 1989:
    age = "eighties"
elif year > 1989 and year <= 1999:
    age = "nineties"
else:
    age = "two thousands"
    
if month == "October" and date == 31:
  print("You were born on Halloween!")
elif month == month_ and date == todaydate:
    print("Happy birthday!")
else: 
    print("{0}, you are a {1} baby of the {2}.".format(name, season, age)) 
    
                   
    
     
    