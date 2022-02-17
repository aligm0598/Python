#Author: John
#Date: feburary 15 2022
# This program is about dates
from datetime import datetime, timedelta

today = datetime.now()
one_day = timedelta(days=1)
yesterday = today - one_day 
print('Today is: ' + str(today))
print('Yesterday was: ' + str(yesterday))

try:
    birthday = input('When is your birthday (dd/mm/yyyy)? ')
    birthday_date = datetime.strptime(birthday, '%d/%m/%Y')
    print ('Birthday: ' +str(birthday_date) +' '+ str(birthday_date.strftime('%A')))
except ValueError as e:
    print('Please put vaild date in correct format (dd/mm/yyyy)')
finally:
    print('Finished')
