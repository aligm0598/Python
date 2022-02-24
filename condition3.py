#Author: John
#Date: February 23 2022
# This program is about how to use multiple conditions
country = input('What country are you from? ')

if country.lower() == ('canada'):
    province = input('What province are you from? ')
    if province.lower() in('alberta', 'nunavut', 'yukon'):
        tax = 0.05 
    elif province.lower() == "ontario": 
        tax = 0.13
    else:
        tax = 0.15 
    print('Since you are from ' + str(province.lower()) + ' your tax is ' + str(tax))
else:
    tax=0
    print('Since you are not from canada your tax is ' + str(tax))
