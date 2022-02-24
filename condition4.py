#Author: John
#Date: February 24 2022
# This program is about complex conditions 
gpa = float(input('What is your grade point average? '))
lowest = float(input('What is your lowest grade? '))

if gpa >= .85 and lowest >= .70:
    honour_roll = True
else:
    honour_roll = False 

if honour_roll == True: 
    print('You made the honour roll ')
else:
    print('You did not make the honuor roll')

